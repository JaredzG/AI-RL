
def find_possible_actions(state, agent):
  '''
  Based on the current position, find the positions that can be taken. Can't move in direction of wall if next to one, can't move into cell occupied by other agent.
  '''
  moves = ['up', 'down', 'left', 'right', 'forward', 'backward']
  agent_pos = []
  other_agent_pos = []
  
  if agent == 'm':
    agent_pos = state['male_position']
    other_agent_pos = state['female_position']
  else:
    agent_pos = state['female_position']
    other_agent_pos = state['male_position']
  
  if (abs(agent_pos[0] - other_agent_pos[0]) == 1):
    if (agent_pos[0] - other_agent_pos[0] < 0):
      if moves.count('up'):
        moves.remove('up')
    else:
      if moves.count('down'):
        moves.remove('down')
  elif (abs(agent_pos[1] - other_agent_pos[1]) == 1):
    if (agent_pos[1] - other_agent_pos[1] < 0):
      if moves.count('backward'):
        moves.remove('backward')
    else:
      if moves.count('forward'):
        moves.remove('forward')
  elif (abs(agent_pos[2] - other_agent_pos[2]) == 1):
    if (agent_pos[2] - other_agent_pos[2] < 0):
      if moves.count('right'):
          moves.remove('right')
      else:
        if moves.count('left'):
          moves.remove('left')
  
  if agent_pos[0] == 0:
    if moves.count('down'):
      moves.remove('down')
  elif agent_pos[0] == 2:
    if moves.count('up'):
      moves.remove('up')
  if agent_pos[1] == 0:
    if moves.count('forward'):
      moves.remove('forward')
  elif agent_pos[1] == 2:
    if moves.count('backward'):
      moves.remove('backward')
  if agent_pos[2] == 0:
    if moves.count('left'):
      moves.remove('left')
  elif agent_pos[2] == 2:
    if moves.count('right'):
      moves.remove('right')
  
  return moves

# def main():
#     moves = find_possible_actions({'male_position': [0, 1, 2], 'female_position': [1, 1, 2], 'male_carrying': False, 'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}, 'm')
#     print(moves)

# if __name__ == "__main__" :
#     main();
  