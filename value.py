def q_learning_value_function(old_q_val, move_reward, next_q_vals, alpha, gamma):
  return old_q_val + alpha * (move_reward + gamma * max(next_q_vals) - old_q_val)