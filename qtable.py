import reward
import value
class Qtable:
  def __init__(self):
    self.table = {
      'normal': {
          'up': 5,
          'down': 12,
          'left': 3,
          'right': 8,
          'forward': 4,
          'backward': 7
      },
      'risky': {
          'up': 0,
          'down': 0,
          'left': 0,
          'right': 0,
          'forward': 0,
          'backward': 0
      },
      'pickup': {
          'up': 0,
          'down': 0,
          'left': 0,
          'right': 0,
          'forward': 0,
          'backward': 0
      },
      'dropoff': {
        'up': 5,
        'down': 12,
        'left': 3,
        'right': 8,
        'forward': 4,
        'backward': 7
      }
    }
    
  def update_qtable(self, position, move, next_cell, next_actions, alpha, gamma):
    old_q_val = self.table[position][move]
    move_reward = reward.get_reward(position)
    next_q_vals = self.find_q_vals(next_cell, next_actions)
    next_q_vals_list = []
    for q_val in next_q_vals:
      next_q_vals_list.append(next_q_vals[q_val])
    print('next_q_vals', next_q_vals_list)
    new_q_val = round(value.q_learning_value_function(old_q_val, move_reward, next_q_vals_list, alpha, gamma), 2)
    print('new_q_val ', new_q_val)
    self.table[position][move] = new_q_val
    print('new_q_val in q_table ', self.table[position][move])
    
    

  def find_q_vals(self, position, moves):
    print("position ", position)
    q_vals = {}
    for direction in moves:
      q_vals[direction] = self.table[position][direction]
    return q_vals

# def main():
#     qtable = Qtable()
#     moves = ["up", "down"]
#     dict = {}
#     dict = qtable.find_q_vals("normal", moves)
#     print(dict)

# if __name__ == "__main__" :
#     main();