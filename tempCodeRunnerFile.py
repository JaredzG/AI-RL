picked_up_or_dropped_off = False
    if chosen_agent.type == 'm':
      picked_up_or_dropped_off = world_state.update_environment_and_state(world_state.representation['male_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    else:
      picked_up_or_dropped_off = world_state.update_environment_and_state(world_state.representation['female_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    if picked_up_or_dropped_off:
      if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
        agent.pickup_or_dropoff(chosen_agent, cells[chosen_action]['type'])