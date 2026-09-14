CELL_SIZE = 28 #pixels per maze cell
MAX_MAZE_WIDTH = 380

GHOST_COLORS = ["#ff4444", "#3ff0ff", "#ff9edb", "#ffa552"] #red, cyan, pink, orange

#different wall colors per level, cycled through
WALL_COLORS = [
    "#2222dd", #blue
    "#9b30ff", #purple
    "#22c55e", #green
    "#ff8c1a", #orange
    "#ff2ec5", #pink
    "#00c2c2", #teal
    "#e53935", #red
    "#d4af37", #gold
]

PLAYER_INNER_HTML = (
    '<div class="player-body"></div>'
    '<div class="player-antenna l"><div class="player-antenna-tip"></div></div>'
    '<div class="player-antenna r"><div class="player-antenna-tip"></div></div>'
    '<div class="eye l"><div class="pupil"></div></div>'
    '<div class="eye r"><div class="pupil"></div></div>'
    '<div class="cheek l"></div><div class="cheek r"></div>'
    '<div class="smile"></div>'
)

def render_maze_html(maze, player_row, player_col, enemies, wall_color=None): #builds a html string - a css grid of colored <div> cells representing the maze, the player as pac-maan shape and each enemy as a colored ghost
    num_rows = len(maze)
    num_cols = len(maze[0])
    wall_color = wall_color or WALL_COLORS[0]

    cell_size = min(CELL_SIZE, MAX_MAZE_WIDTH // num_cols) #shrink cells for wider mazes

    cells_html = ""
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            symbol = maze[row_index][col_index]

            is_player_here = (row_index == player_row and col_index == player_col)
            enemy_here = None
            enemy_index = 0
            for i, enemy in enumerate(enemies):
                if enemy["row"] == row_index and enemy["col"] == col_index:
                    enemy_here = enemy
                    enemy_index = i
                    break

            if is_player_here:
                cells_html += f'<div class="cell player">{PLAYER_INNER_HTML}</div>'
            elif enemy_here is not None:
                if enemy_here.get("is_trap"):
                    cells_html += '<div class="cell trap"></div>'
                else:
                    color = GHOST_COLORS[enemy_index % len(GHOST_COLORS)] #each enemy gets its own color, based on its position % - means the color just repeat if there were ever more than 4 enemies
                    ghost_inner = (
                        f'<div class="ghost-body" style="--ghost-color:{color}"></div>'
                        '<div class="g-eye l"><div class="g-pupil"></div></div>'
                        '<div class="g-eye r"><div class="g-pupil"></div></div>'
                        '<div class="g-smile"></div>'
                    )
                    cells_html += f'<div class="cell ghost">{ghost_inner}</div>'
            elif symbol == "#":
                cells_html += f'<div class="cell wall" style="--wall-color:{wall_color}"></div>' #building a string - every single cell in the maze gets exactly one piece of html like this and get glued together into one big string
            elif symbol == "o":
                cells_html += '<div class="cell dot"></div>'
            else:
                cells_html += '<div class="cell path"></div>'

    maze_style = f"grid-template-columns: repeat({num_cols}, {cell_size}px); grid-template-rows: repeat({num_rows}, {cell_size}px);--wall-color:{wall_color};" #turns a flat list of <div> into a proper num_cols and num_rows grid shape
    return f'<div class="maze" style="{maze_style}">{cells_html}</div>'

def wrap_maze_panel(maze_html):
    sparkle_positions = [
        ("top:-6px; left:10px;"), ("top:20px; left:-16px;"), ("bottom:10px; left:-14px;"),
        ("top:-6px; right:10px;"), ("top:30px; right:-16px;"), ("bottom:20px; left:-14px;"),
    ]
    sparkle_html = "".join(f'<div class="sparkle" style="{pos}">&#10022;</div>' for pos in sparkle_positions)
    return f'<div class="panel-wrap">{sparkle_html}<div class="panel">{maze_html}</div></div>'

def render_stat_badges(score, dots_left):
    return (
        '<div class="stats">'
        f'<div class="stat-badge">SCORE: {score}</div>'
        f'<div class="stat-badge">DOTS: {dots_left}</div>'
        '</div>'
    )

def get_wall_color(level_index):
    return WALL_COLORS[level_index % len(WALL_COLORS)]

MAZE_CSS = """
<style> 
    .panel-wrap {position: relative; display: inline-block; margin: 10px auto; }
    .sparkle { position: absolute; color: #ffea00; font-size: 18px; text-shadow: 0 0 6px #ffea00; }
    .panel {
        border: 4px solid #2222dd;
        border-radius: 16px;
        background: #0a0a0a;
        padding: 14px;
        box-shadow: 0 0 20px rgba(34,34,221,0.4);
    }
        
    .maze {
        display: grid; /*tells browser to arrange the boxes into a proper grid of rows and columns*/
        gap: 0; /*not spacing between cells - walls connect seamlessly*/
        border: 3px solid var(--wall-color, #2222dd); /*outline around the maze*/  
        width: fit-content;   /*forces the boxes to shrink down to exactly the size of what's actually inside of it - without stretching the entire page*/ 
    }
    .cell { width: 100%; height: 100%; position: relative;} /*correct position for the dot/player/ghost shapes inside their cell */
    .wall { background: var(--wall-color, #2222dd); border: 2px solid var(--wall-color, #2222dd); filter: brightness(1.3); box-sizing: border-box;}
    .path { background: #0a0a0a; } 
    .dot { background: #0a0a0a; }
    .dot::after { /*creates an extra shape glued onto an element*/
        content: ""; /*not text required only a shape*/ 
        position: absolute; top: 50%; left: 50%; /*positions the dot slightly off center on the top left corner of the cell*/
        width: 6px; height: 6px; background: #ffd54a;
        border-radius: 50%; transform: translate(-50%, -50%); /*shifts the dot back, landing at the center of the cell , #border-radius 50% turn any square into a circle*/ 
        }
        
    .player { background: #0a0a0a; }  
    .player-body {
        position: absolute; top: 8%; left: 8%; width: 84%; height: 84%;
        background: radial-gradient(circle at 35% 30%, #b6f7c1, #4fd67a 75%); 
        border-radius: 50%;
    }
    .player-antenna { position: absolute; width: 3px; height: 8px; background: #4fd67a; top: 2% } 
    .player-antenna.l { left: 32%; transform: rotate(-20deg); }
    .player-antenna.r { left: 62%; transform: rotate(20deg); } 
    .player-antenna-tip { position: absolute; width: 5px; height: 5px; border-radius: 50% ; background: #ffd54a; top: -3px; left: -1px; } 
    .eye { position: absolute; width: 10px; height: 12px; background: #fff; border-radius: 50%; top: 38%; } 
    .eye.l { left: 28%; } 
    .eye.r { left: 58%; } 
    .pupil { position: absolute; width: 5px; height: 6px; background: #213; border-radius: 50%; top: 3px; left: 2.5px; }
    .cheek {position: absolute; width: 7px; height: 12px; background: #ffb3b3; border-radius: 50%; top: 58%; opacity: 0.8; } 
    .cheek.l { left: 18%; }
    .cheek.r { left: 70%; } 
    .smile { position: absolute; width: 10px; height: 5px; border-bottom: 2px solid #204d2a; border-radius: 0 0 10px 10px; top: 64%; left: 38%; }
    
    /*ghost design*/ 
    .ghost { background: #0a0a0a; }
    .ghost-body {
        position: absolute; top: 10%; left: 10%; width: 80%; height: 80%;
        background: var(--ghost-color, #ff4444);
        border-radius: 50% 50% 8% 8%; 
    }
    .g-eye { position: absolute; width: 9px; height: 11px; background: #fff; border-radius: 50%; top: 32%; }
    .g-eye.l { left: 22%; }
    .g-eye.r { left: 56%; }
    .g-pupil { position: absolute; width: 4px; height: 5px; background: #222; border-radius: 50%; top: 3px; left: 2.5px; }
    .g-smile { position: absolute; width: 8px; height: 4px; border-bottom: 2px solid #7a1414; border-radius: 0 0 8px 8px; top: 56%; left: 40%; } 
    
    .trap { background: #0a0a0a; }
    .trap::after {
        content: "X";
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        color: #ff3b3b; font-family: monospace; font-weight: bold; font-size: 16px;
    }
    
    /*stat badges*/
    .stats { display: flex; gap: 10px; justify-content: center; margin-top: 14px; } 
    .stat-badge { 
        border: 2px solid #39ff14; border-radius: 20px; padding: 4px 14px; 
        color: #39ff14; font-size: 13px; font-weight: bold; font-family: monospace; 
    }
    .mini-icon { width: 34px; height: 34px; position: relative; display: inline-block; }
    .mini-icon.player-icon .m-body {
        position: absolute; top: 8%; left: 8%; width: 84%; height: 84%;
        background: radial-gradient(circle at 35% 30%, #b6f7c1, #4fd67a 75%);
        border-radius: 50%; 
    }
    .mini-icon .m-eye { position: absolute; width: 7px; height: 8px; background: #fff; border-radius: 50%; top: 36%; }
    .mini-icon .m-eye.l { left: 26%; }
    .mini-icon .m-eye.r { left: 58%; } 
    .mini-icon .m-pupil { position: absolute; width: 3px; height: 4px; background: #213; border-radius: 50%; top: 2px; left: 2px; } 
    .mini-icon.ghost-icon .m-body { 
        position: absolute; top: 10%; left: 10%; width: 80%; height: 80%;
        background: var(--ghost-color, #ff4444);
        border-radius: 50% 50% 8% 8%; 
    } 
   .mini-icon.star::after {
        content: "\\2605";
        position: absolute; top:0; left:0; width: 100%; height: 100%;
        display: flex; align-items:center; justify-content: center; 
        color: var(--star-color, #ffea00); font-size: 26px;
    } 
    .corner-deco {position: absolute;width: 34px; height: 34px;}
    .title-wrap {position: relative; min-height: 140px; }

/*trophy on prize slide*/        
    .trophy-wrap {text-align: center; margin: 10px 0 20px 0;}
    .trophy-cup {
        width: 90px; height: 70px;
        margin: 0 auto;
        background: linear-gradient(180deg, #fff3b0, #ffd400 60%, #c98f00); /*a straight line color blend - top-to-bottom, moving through three different color stops*/ 
        border-radius: 10px 10px 40px 40px / 10px 10px 60px 60px; /*corner rounding property: the numbers before the slash control horizontal curve, the numbers after control the vertical curve*/ 
        position: relative;
        box-shadow: 0 0 18px 2px rgba(255,212,0,0.6); /*a soft glow(shadow) around the shape, rgba as a normal color and the fourth number controlling transparency*/ 
    }
    .trophy-handle {
        width: 26px; height: 34px;
        border: 6px solid #ffd400;
        border-right: none;
        border-radius: 50% 0 0 50%;
        position: absolute;
        top: 10px;
    }
    .trophy-handle.left {left: -24px; } 
    .trophy-handle.right {right: -24px; transform: scaleX(-1); } /*scale flipped horizontally and multiplied by -1*/
    .trophy-stem {width: 14px; height: 22px; background: #ffd400; margin: 0 auto;}
    .trophy-base { width: 56px; height: 12px; background: #e0a800; margin: 0 auto; border-radius: 3px;}                         
    .trophy-star {
        position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
        color: #fff59d; font-size: 22px; text-shadow: 0 0 8px #ffd400;
    }                
</style>
"""
#styles the rest of the Streamlit page separately from the maze itself, so they stay independent of each other
RETRO_STYLE = """
<style>
    .stApp { background-color: #0a0a0a; } 
    h1, h2, h3, p, label, .stMarkdown {color: #39ff14 !important; font-family: monospace; }
    .stButton button {
        background-color: #0a0a0a;
        color: #39ff14;
        border: 2px solid #39ff14;
        font-family: monospace;
        font-weight: bold; 
    }
</style> 
"""

def render_title_decorations():
    player_icon = '<div class="mini-icon player-icon"><div class="m-body"></div><div class="m-eye l"><div class="m-pupil"></div></div><div class="m-eye r"><div class="m-pupil"></div></div></div>'
    ghost_icon = lambda color: f'<div class="mini-icon ghost-icon"><div class="m-body" style="--ghost-color:{color}"></div><div class="m-eye l"><div class="m-pupil"></div></div><div class="m-eye r"><div class="m-pupil"></div></div></div>'
    return (
        f'<div class="corner-deco" style="top:0; left:0;">{player_icon}</div>'
        f'<div class="corner-deco" style="top:0; right:0;">{ghost_icon("#3ff0ff")}</div>'
        f'<div class="corner-deco" style="bottom:0; left:0;">{ghost_icon("#ff9edb")}</div>'
        '<div class="corner-deco" style="bottom:0; right:0;"><div class="mini-icon star" style="--star-color:#ffea00"></div></div>'
    )
def render_trophy(): #returns html for the trophy graphic shown on the prize screen
    return (
        '<div class="trophy-wrap">'
        '<div class="trophy-cup">'
        '<div class="trophy-star">&#9733;</div>'
        '<div class="trophy-handle left"></div>'
        '<div class="trophy-handle right"></div>'
        '</div>'
        '<div class="trophy-stem"></div>'
        '<div class="trophy-base"></div>'
        '</div>'
    )

