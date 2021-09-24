import numpy as np, math
from copy import deepcopy

def heuristics(grid, num_empty):
  '''
  This function scores the grid based on the algorithm implemented
  so that the maximize function of AI_Minimax can decide which branch
  to follow.
  '''
  grid = np.array(grid)
  score = 0

  # TODO: Implement your heuristics here. 
  # You are more than welcome to implement multiple heuristics
  
  # Weight for each score
  return score