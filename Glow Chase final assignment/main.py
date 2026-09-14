import streamlit as st
from levels import BEGINNER_LEVELS, ADVANCED_LEVELS
from game_logic import (
    try_move, collect_dot_if_present, count_remaining_dots, move_enemy_toward_player, check_collision, check_win,
)
from render import render_maze_html, wrap_maze_panel, render_stat_badges, MAZE_CSS, RETRO_STYLE, get_wall_color, render_title_decorations, render_trophy

#browser tab title/icon and css blocks get injected into the page
st.set_page_config(page_title="Maze Muncher", page_icon="\U0001F47B", layout="centered")
st.markdown(RETRO_STYLE, unsafe_allow_html=True)
st.markdown(MAZE_CSS, unsafe_allow_html=True)

def start_level(level_data):
    st.session_state.maze = level_data["maze"].copy() #without copy()  it would point at the exact same list - makes a copy so that levels.py always stays clean
    st.session_state.player_row, st.session_state.player_col = level_data["player_start"]
    st.session_state.enemies = [] #convert enemy info
    for enemy_info in level_data["enemies"]:
        row, col = enemy_info["start"]
        st.session_state.enemies.append({
            "row": row,
            "col": col,
            "moves_every_turn": enemy_info["moves_every_turn"],
            "is_trap": enemy_info.get("is_trap", False),
        })
    st.session_state.score = 0
    st.session_state.turn_count = 0
    st.session_state.game_over_message = None # None = game still in progress

def get_current_levels():
    if st.session_state.mode == "advanced":
        return ADVANCED_LEVELS
    return BEGINNER_LEVELS

def handle_move(direction):
    if st.session_state.game_over_message is not None:
        return

    #moves the player from the function in game_logic.py
    st.session_state.player_row, st.session_state.player_col = try_move(
        st.session_state.maze, st.session_state.player_row, st.session_state.player_col, direction
    )

    if collect_dot_if_present(st.session_state.maze, st.session_state.player_row, st.session_state.player_col):
        st.session_state.score += 1

    st.session_state.turn_count += 1

    #moves enemy according to its own speed
    for enemy in st.session_state.enemies:
        if enemy["is_trap"]:
            continue
        should_move = enemy["moves_every_turn"] or (st.session_state.turn_count % 2 == 0) # fast enemy always moves, slow enemy only on even turn numbers
        if should_move:
            enemy["row"], enemy["col"] = move_enemy_toward_player(
                enemy["row"], enemy["col"],
                st.session_state.player_row, st.session_state.player_col,
                st.session_state.maze,
            )

    #lose check - did enemy land on same cell as player
    for enemy in st.session_state.enemies:
        if check_collision(st.session_state.player_row, st.session_state.player_col, enemy["row"], enemy["col"]):
            st.session_state.game_over_message = "You lose!"
            return

    #win check - only reached if nothing above ended the game
    if check_win(st.session_state.maze):
        st.session_state.game_over_message = "You win!"

if "screen" not in st.session_state:
    st.session_state.screen = "title"
if "current_level_index" not in st.session_state:
    st.session_state.current_level_index = 0

#title screen
if st.session_state.screen == "title":
    title_html = (
        '<div class="title-wrap">'
        + render_title_decorations()
        + "<h1 style='text-align:center;'>WELCOME TO<br>GLOW CHASE</h1>"
        + "<p style='text-align:center;' >-- SELECT YOUR LEVEL --</p>"
        +"</div>"
    )
    st.markdown(title_html, unsafe_allow_html=True)

    if st.button("BEGINNER", use_container_width=True):
        st.session_state.mode = "beginner"
        st.session_state.current_level_index = 0
        start_level(BEGINNER_LEVELS[0])
        st.session_state.screen = "playing"
        st.rerun()

    if st.button("ADVANCED", use_container_width=True):
        st.session_state.mode = "advanced"
        st.session_state.current_level_index = 0
        start_level(ADVANCED_LEVELS[0])
        st.session_state.screen = "playing"
        st.rerun()

#playing screen
elif st.session_state.screen == "playing":
    levels = get_current_levels()
    st.markdown(f"<h3 style='text_align:center;'>Level {st.session_state.current_level_index + 1} / {len(levels)}</h3>", unsafe_allow_html=True)

    #turns the current game state into html maze
    maze_html = render_maze_html(
        st.session_state.maze,st.session_state.player_row,st.session_state.player_col, st.session_state.enemies,
        wall_color=get_wall_color(st.session_state.current_level_index),
    )
    st.markdown(f"<div style='text-align:center:'>{wrap_maze_panel(maze_html)}</div", unsafe_allow_html=True)
    st.markdown(render_stat_badges(st.session_state.score, count_remaining_dots(st.session_state.maze)), unsafe_allow_html=True)

    if st.session_state.game_over_message == "You lose!":
        st.error("Caught! Game over.")
        if st.button("Try again"):
            start_level(levels[st.session_state.current_level_index])
            st.rerun()
        if st.button("Back to Title"):
            st.session_state.screen = "title"
            st.rerun()

    elif st.session_state.game_over_message == "You win!":
        st.success("Level completed")
        is_last_level = st.session_state.current_level_index == len(levels) - 1 #index of the last level in the list
        if is_last_level:
            if st.button("Continue"):
                st.session_state.screen = "prize"
                st.rerun()

        else:
            if st.button("Next Level"):
                st.session_state.current_level_index += 1
                start_level(levels[st.session_state.current_level_index])
                st.rerun()

    else: #shows the direction buttons
        _, up_col, _ = st.columns(3)
        with up_col:
            if st.button("Up", use_container_width=True):
                handle_move("up")
                st.rerun() #refresh immediately so the move shows up right away

        left_col, _, right_col = st.columns(3)
        with left_col:
            if st.button("Left", use_container_width=True):
                handle_move("left")
                st.rerun()
        with right_col:
            if st.button("Right", use_container_width=True):
                handle_move("right")
                st.rerun()

        _, down_col, _ = st.columns(3)
        with down_col:
            if st.button("Down", use_container_width=True):
                handle_move("down")
                st.rerun()

#prize screen
elif st.session_state.screen == "prize":
    st.markdown(render_trophy(), unsafe_allow_html=True)
    prize_art = r"""
    *   .   *   .   *  .  *
        YOU WIN A PRIZE!
    *   .   *   .   *  .  *

"""
    st.text(prize_art)
    st.markdown("<p style='text-align:center; ' >Thanks for playing Glow Chase!</p>", unsafe_allow_html=True)
    if st.button("Back to Title Screen"):
        st.session_state.screen = "title"
        st.rerun()
