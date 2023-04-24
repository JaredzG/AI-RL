 # if cells[chosen_action]['type'] == 'pickup' and world_state.representation['pickup_cell_blocks'][tuple(cells[chosen_action]['coords'])] > 0:
    #   if chosen_agent.type == 'm':
    #     if world_state.representation['male_carrying'] == False:
    #       blocks_picked_up += 1
    #   else:
    #     if world_state.representation['female_carrying'] == False:
    #       blocks_picked_up += 1
    # if cells[chosen_action]['type'] == 'dropoff' and world_state.representation['dropoff_cell_blocks'][tuple(cells[chosen_action]['coords'])] > 0:
    #   if chosen_agent.type == 'm':
    #     if world_state.representation['male_carrying'] == True:
    #       blocks_picked_up += 1
    #   else:
    #     if world_state.representation['female_carrying'] == True:
    #       blocks_picked_up += 1