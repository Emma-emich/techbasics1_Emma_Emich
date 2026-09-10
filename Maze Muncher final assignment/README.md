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


AI Usage:
- AI was used to help and explain concepts that we haven't touched upon in class yet, especially CSS concepts, also for debugging. 
