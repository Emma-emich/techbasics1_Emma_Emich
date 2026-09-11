ELL_SIZE = 28 #pixels per maze cell
MAX_MAZE_WIDTH = 380

GHOST_COLORS = ["#ff4444", "3ff0ff", "#ff9edb", "#ffa552"] #red, cyan, pink, orange

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
                cells_html += '<div class="cell player"></div>'
            elif enemy_here is not None:
                if enemy_here.get("is trap"):
                    cells_html += '<div class="cell trap"></div>'
                else:
                    color = GHOST_COLORS[enemy_index % len(GHOST_COLORS)] #each enemy gets its own color, based on its position % - means the color just repeat if there were ever more than 4 enemies
                    cells_html += f'<div class="cell ghost" style="--ghost-color:{color}"></div>' #anything with two dashes is a custom property - a variable i can define myself - python sets a different value for it on every single wall <div> depending on the level that is currently loaded
            elif symbol == "#":
                cells_html += f'<div class="cell wall" style="--wall-color:{wall_color}"></div>' #building a string - every single cell in the maze gets exactly one piece of html like this and get glued together into one big string
            elif symbol == "o":
                cells_html += '<div class="cell dot"></div>'
            else:
                cells_html += '<div class="cell path"></div>'

    maze_style = f"grid-template_columns: repeat({num_cols}, {cell_size}px); grid-template_rows: repeat({num_rows}, {cell_size}px);--wall-color:{wall_color};" #turns a flat list of <div> into a proper num_cols and num_rows grid shape
    return f'<div class="maze" style="{maze_style}">{cells_html}</div>'

def get_wall_color(level_index):
    return WALL_COLORS[level_index % len(WALL_COLORS)]

MAZE_CSS = """
<style> 
    .maze {
        display: grid; #tells browser to arrange the boxes into a proper grid of rows and columns
        gap: 0; #not spacing between cells - walls connect seamlessly 
        border: 4px solid var(--wall--color, #2222dd); #outline around the maze 
        margin: 10px auto; 
        width: fit-content;   #forces the boxes to shrink down to exactly the size of what's actually inside of it - without stretching the entire page 
    }
    .cell { width: 100%; height: 100%; position: relative;} #correct position for the dot/player/ghost shapes inside their cell 
    .wall { background: var(--wall-color, #2222dd); border: 2px solid var(--wall--color, #2222dd); filter: brightness(1.3); box-sizing: border-box;}
    .path { background: #0a0a0a; } 
    .dot { background: 0a0a0a: }
    .dot :: after { #creates an extra shape glued onto an element
        content: ""; #not text required only a shape 
        position: absolute; top: 50%; left: 50%; #positions the dot slightly off center on the top left corner of the cell
        width: 6px; height: 6px: background: #ffd54a;
        border-radius: 50%; transform: translate(-50%, -50%); #shifts the dot back, landing at the center of the cell , #border-radius 50% turn any square into a circle 
        }
    .player { background: #0a0a0a; }    
    player::after {
        content:"";
        position: absolute; top: 12%; left: 12%;
        width: 76%; height: 76%;
        background: radial-gradient(circle at 35% 35%,#fff9d, #fffd400 70%); #blends between two colors 
        border-radius: 50%;
        clip-path: polygon(100% 74%, 44% 50%, 100% 26%, 100% 0, 0 0, 0 100%, 100% 100%); #only shows the part of the element inside the shape and cuts away everything else , lists a series of corner points that trace out the shape to keep 
        }
        .ghost { background. #0a0a0a; }
        .ghost::after { 
            content: "";
            position: absolute; top: 14%; left: 14%;
            width: 72%; height: 72%;
            background: var(--ghost-color, #ff4444);  
            border-radius: 50% 50% 8% 8%; #rounds each corner separately - here it rounds the top two corners into a full dome shape but the bottom two only very slightly - producing the ghost silhouette  
        }
        .trap { background: #0a0a0a; }
        .trap::after {
            content: "X";
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            color: #ff3b3b; font-family: monospace; font_weight: bold; font-size: 16xp;
        }
        .mini-icon { width: 34xp; height: 34xp; position: relative; display: inline-block; }
        .mini-icon.player:: after {
            content: "";
            position: absolute; top: 8%; left: 8%; width: 84%; height: 84%;
            background: radial-gradient(circle at 35% 35%, #fff59d, #ffd400 70%);
            border-radius: 50% 
            clip-path: polygon(100% 74%, 44% 50%, 100% 26%, 100% 0, 0 0, 0 100%, 100% 100%); 
        }
        .mini-icon.ghost ::after {
            content: "";
            position: absolute; top: 10%; left: 10%; width: 80%; height: 80%;
            background: var(--ghost-color, #ff4444);  
            border-radius: 50% 50% 8% 8%;
        }
        .mini-icon.star ::after {
            content: "";
            position: absolute; top:0; left:0; width: 100%; height: 100%;
            display: flex; align_items:center: justify-content: center; 
            color: var(--star-color, #ffea00); font-size: 26px;
        }
        .corner-deco {
            position: absolute;
            width: 34px; height: 34px;
        }
        .title-wrap {position: relative; min-height: 140px; }
        
        .trophy-wrap {test-align: center; margin: 10px 0 20px 0;}
        .trophy-cup {
            width: 90px; height: 70px;
            margin: 0 auto;
            background: linear-gradient(180deg, #fff3b0, #ffd400 60%, #c98f00); #a straight line color blend - top-to-bottom, moving through three different color stops 
            border-radius: 10px 10px 40px 40px / 10px 10px 60px 60px; #conrer rounding property: the numbers before the slash control horizontal curve, the numbers after control the vertical curve 
            position: relative;
            box-shadow: 0 0 18px 2px rgba(255,212,0,0.6); #a soft glow(shadow) around the shape, rgba as a normal color and the fourth number controlling transparency 
        }
        .trophy-handle {
            width: 26px; height: 34px;
            border: 6px solid #ffd400
            border-right: none;
            border-radius: 50% 0 0 50%;
            position: absolute;
            top: 10px;
        }
        .trophy-handle.left {left: -24px; } 
        .trophy-handle.right {right: -24px; transform: scaleX(-1); } #scale flipped horizontally and multiplied by -1
        .trophy-stem {
            width: 14px; height: 22px;
            background: #ffd400;
            margin: 0 auto;
        }
        .trophy-base { 
            width: 56px; height. 12px;
            background: #e0a800;
            margin: 0 auto;
            border-radius: 3px;
        }                         
        .trophy-star {
            position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
            color: #fff59d; font-size: 22px: text-shadow; 0 0 8px #ffd400;
        }                
</style>
"""
#styles the rest of the Streamlit page separately from the maze itself, so they stay independent of each other
RETRO_STYLE = """
<style>
    .stApp { background-color: #0a0a0a; } 
    h1, h2, h3, p, label, stMarkdown {color: #39ff14 !important; font-family: monospace; }
    .stButton button {
        background-color: #0a0a0a;
        color: #39ff14;
        border: 2px solid #39ff14,
        font-family: monospace;
        font-weight: bold; 
    }
</style> 
"""

def render_title_decorations(): #returns html for the 4 corner caricatures on the title screen
    return (
        '<div class="corner-deco" style="top:0; left:0:"><div class="mini-icon player"></div></div>'
        '<div class="corner-deco" style="top:0; right:0:"><div class="mini-icon ghost" style="--ghost-color.#3ff0ff"></div></div>'
        '<div class="corder-deco" style="bottom:o; left:0;"><div class="mini-icon ghost" style="--ghost-color: #ff9edb"></div></div>'
        'div class="corner-deco" style="bottom:0; right:0;"><div class="mini-icon star" style="--star-color:#ffea00"></div></div>'
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


