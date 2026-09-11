I had some issues with committing the coding history directly from pycharm, that I couldn't fix, which is why I'm uploading it directly here and document my progress step by step. 

Documentation: 
Maze Muncher: 
A pac-man inspired game built with streamlit. The mazeis rendered as a grid of colored HTML/CSS blocks - no images used.

How to run:
1. pip install streamlit 
2. streamlit run main.py

How to play:
You use the up/down/left/right buttons to move around in the maze, collecting dots while trying to avoid the ghost(s). You need to collect every dot to win the level. The advanced more has multiple ghosts hunting at one.

project structure:
- game_logic.py - movement, collision and win/lose rules --> done 
- levels.py - maze layouts and level settings (1 of several levels so far)
- render.py - will turn the game into the colored maze display (not started) 
- main.py - will be the actual app/game: screens and button handling (not started) 

Developments:
Day1 
What has been done already: 
- the core game logic --> movement, dot collection, enemy AI, win/lose 
- first level data 

It's not yet runnable because the main.py hasn't been built yet. coming next ...

Day2
What has been done:
- I added the rest of the beginner levels (2-6) and both advanced levels. The difficulty increases gradually through maze size, wall density, dot count and enemy speed/count.


Day3
What has been done:
- built the render.py: the maze, player and enemies as a styled grid of HTML/CSS elements, including CSS concepts --> CSS grid, pseudo-elements, clip-path, CSS custom properties
- designed colored blocks - a blocky, retro arcade-style maze, with different wall colors per level, each enemy also getting an own color 
- CSS for all the styling - the player, ghosts, the title screen, the price and decorations 
- CSS techniques used: 
- CSS grid to arrange every maze cell into an actual row/column layout 
- ::after elements to draw the dot, pac-man and ghost shapes inside the cell boxes 
- clip-path: polygon(...) to cut the pac-man's mouth shape out of a plain circle 
- border-radius(50% 50% 8% 8%) to round only the top two corners of the ghost much and the bottom corners less
- CSS custom properties (--wall-color, --ghost-color) so one single .wall/.ghost rule could produce 8 different level colors and 4 different ghost colors 
- radial-gradient(pac-man's shading) and linear-gradient (the trophy cup) for soft, non-flat coloring 
- box-shadow for the trophy's glow effect

Day4
What has been done:
I built the main.py: the title screen, the playing screen (buttons, maze display, score), win/lose handling and screen navigation between all three
This is where session_state was actually needed for the first time - streamlit reruns the entire script on every click, so session_state is what lets the game remember the player's position, score and current screen between clicks instead of resetting every time.
Now the three previously separated files - gmae_logic.py, levels.py and render.py - were actually run together 
  

AI Usage:
- AI was used to help and explain concepts that we haven't touched upon in class yet, especially CSS concepts, and also for debugging of the CSS layout issues encountered. 
