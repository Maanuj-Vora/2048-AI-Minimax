# 2048-AI

This is the starter code for 2048 AI project for IEEE Fall 2021
1. User_game: The traditional one-human-player 2048 game
2. AI_game: Run one-AI-player 2048 game
3. AI_Move: the basic tile move/merge logic based on 2048 rules
4. AI_Minimax: Minimax algorithm for 2048 tree. Max is the AI playing the game, and Min is the computer which generates new 2 or 4 tile randomly
5. AI_Heuristics: The heuristics function to rank/compare possible branch grids. This will be used to collect the best possible move in AI_Minimax

## How to run/test your AI

This AI is built based on the 2048 pypi package made by user 'quantum'. If you don't have this package on your laptop, run <code> pip install 2048 </code> in your terminal.

Then, in the directory, run <code> py AI_game.py </code> to test your AI performance.

The GUI will automatically pops up, and AI will start search.

## Todo

- [x] AI_Minimax.py
- [x] AI_Heuristics.py
