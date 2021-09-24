from copy import deepcopy
import numpy as np, math
from AI_Movement import free_cells, move
from AI_Heuristics import heuristics

# The Depth limit constant. You might change this if you want
# Keep in mind that your AI search might be pretty slow if you use too high depth
DEPTH = 5

def maximize(grid, depth=0):
  '''
  Maximize function for the max (AI) of the MiniMax Algorithm
  If you want to change the depth of the search tree, try to 
  implement some conditions for the "early stopping" at minimize
  or set up your own limit constant.
  '''
  # TODO: Replace the value of the best_score
  # If you are not sure, check the implementation we talked about in week 2
  best_score = "change this"
  best_move = None

  # TODO: Implement maximize function here
  
  return best_move, best_score

def minimize(grid, depth=0):
  '''
  Minimize function for the min (Computer) of the Minimax Algorithm
  Computer put new 2 tile (with 90% probability) or 
  4 tile (with 10% probability) at one of empty spaces
  '''
  empty_cells = free_cells(grid)
  num_empty = len(empty_cells)

  if depth > DEPTH:
    return heuristics(grid, num_empty)

  if num_empty == 0:
    _, new_score = maximize(grid, depth+1)
    return new_score

  # TODO: (Optional) Implement conditions to stop the searching earlier 
  # Would implement it after finish implementing Heuristics and MiniMax
  # ex) If there are enough empty spaces, we will proceed by skipping last two nodes
  # if num_empty >= 6 and depth >= 3:
  #  return heuristics(grid, num_empty)

  sum_score = 0

  for c, r in empty_cells:
    for v in [2, 4]:
      new_grid = deepcopy(grid)
      new_grid[c][r] = v

      _, new_score = maximize(new_grid, depth+1)

      if v == 2:
        new_score *= (0.9 / num_empty)
      else:
        new_score *= (0.1 / num_empty)

      sum_score += new_score

  return sum_score