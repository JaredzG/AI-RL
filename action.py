
def find_possible_actions(state, agent):
  '''
  Based on the current position, find the positions that can be taken. Can't move in direction of wall if next to one, can't move into cell occupied by other agent.
  '''
  moves = ['up', 'down', 'left', 'right', 'forward', 'backward']
  agent_pos = []
  other_agent_pos = []
  
  if agent == 'm':
    agent_pos = state.representation['male_position']['coords']
    other_agent_pos = state.representation['female_position']['coords']
  else:
    agent_pos = state.representation['female_position']
    other_agent_pos = state.representation['male_position']
  print(agent_pos, other_agent_pos)
  
  if agent_pos[0] - other_agent_pos[0] == -1 and (agent_pos[1] == other_agent_pos[1] and agent_pos[2] == other_agent_pos[2]):
    if moves.count('up'):
      print('Removing up due to other agent')
      moves.remove('up')
  elif agent_pos[0] - other_agent_pos[0] == 1 and (agent_pos[1] == other_agent_pos[1] and agent_pos[2] == other_agent_pos[2]):
    if moves.count('down'):
      print('Removing down due to other agent')
      moves.remove('down')
  elif agent_pos[1] - other_agent_pos[1] == -1 and (agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
    if moves.count('backward'):
      print('Removing backward due to other agent')
      moves.remove('backward')
  elif agent_pos[1] - other_agent_pos[1] == 1 and (agent_pos[0] == other_agent_pos[0] and agent_pos[2] == other_agent_pos[2]):
    if moves.count('forward'):
      print('Removing forward due to other agent')
      moves.remove('forward')
  elif agent_pos[2] - other_agent_pos[2] == -1 and (agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
    if moves.count('right'):
      print('Removing right due to other agent')
      moves.remove('right')
  elif agent_pos[2] - other_agent_pos[2] == 1 and (agent_pos[0] == other_agent_pos[0] and agent_pos[1] == other_agent_pos[1]):
    if moves.count('left'):
      print('Removing left due to other agent')
      moves.remove('left')
  
  if agent_pos[0] == 0:
    if moves.count('down'):
      print('Removing down due to wall')
      moves.remove('down')
  elif agent_pos[0] == 2:
    if moves.count('up'):
      print('Removing up due to wall')
      moves.remove('up')
  if agent_pos[1] == 0:
    if moves.count('forward'):
      print('Removing forward due to wall')
      moves.remove('forward')
  elif agent_pos[1] == 2:
    if moves.count('backward'):
      print('Removing backward due to wall')
      moves.remove('backward')
  if agent_pos[2] == 0:
    if moves.count('left'):
      print('Removing left due to wall')
      moves.remove('left')
  elif agent_pos[2] == 2:
    if moves.count('right'):
      print('Removing right due to wall')
      moves.remove('right')
  
  return moves

# def main():
#     moves = find_possible_actions({'male_position': [0, 1, 2], 'female_position': [1, 1, 2], 'male_carrying': False, 'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}, 'm')
#     print(moves)

# if __name__ == "__main__" :
#     main();
  