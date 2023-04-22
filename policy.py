import random
def pRandom(carrying, cells):
  for i in cells: 
    if (cells[i]=="pickup" and not carrying) or (cells[i]=="dropoff" and carrying):
      return i
  position = random.randint(0, len(cells) - 1)
  action = (list(cells))[position]
  return action
    
def pExploit(carrying, cells, q_vals):
    max_q_val = float('-inf')
    max_action = ""
    for i in cells: 
      if (cells[i]=="pickup" and not carrying) or (cells[i]=="dropoff" and carrying):
        return i
    for i in q_vals:
      if (q_vals[i] > max_q_val):
        max_q_val = q_vals[i]
        max_action = i

    non_max_actions = []
    for i in cells:
      if (i != max_action):
        non_max_actions.append(i)
    
    actions = [max_action, non_max_actions]
    weight = [0.80, 0.20]
    choice_made = random.choices(actions, k = 1, weights = weight)
    action_chosen = ''
    if (type(choice_made[0]) is list):
      position = random.randint(0, len(choice_made[0]) - 1)
      action_chosen = choice_made[0][position]
    else:
      action_chosen = choice_made[0]
    return action_chosen

def pGreedy(carrying, cells, q_vals):
  max_q_val = float('-inf')
  max_action = ""
  for i in cells: 
    if (cells[i]=="pickup" and not carrying) or (cells[i]=="dropoff" and carrying):
      return i
  for i in q_vals:
    if (q_vals[i] > max_q_val):
      max_q_val = q_vals[i]
      max_action = i
  return max_action

# def main():
#     cells = {'down': 'normal', 'left': 'normal', 'forward': 'normal', 'backward': 'normal'}
#     q_vals = {'down': 3, 'left': 8, 'forward': 2, 'backward': 5}
#     # print(pRandom(False,cells))
#     # print(pExploit(False, cells, q_vals))
#     print(pGreedy(False, cells, q_vals))

# if __name__ == "__main__" :
#     main()