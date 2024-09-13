def my_algorithm(timestamp, elev_pop, floor_population, floors, elevator_floor, t_floor):
    
    # Simulations always start at floor 1, so if people are in the lift initially, head up, as far as required (take the max).
    if elev_pop and elevator_floor == 1:
        return min(max(elev_pop), floors) # Use min in case returned floor is > floors.

    # If people are in the lift, keep going if target floor not reached yet.
    if elev_pop and elevator_floor != t_floor:
        return t_floor

    # If people are in the lift, and the target floor has now been reached, head back down, as far as required (take the min).
    if elev_pop and elevator_floor == t_floor:
        return max(min(elev_pop), 1) # Use max in case returned floor is < 1.

    # If there's nobody in the lift...
    if not elev_pop:

        # ...and if there's nobody waiting on any floor, then...
        if all(x == 0 for x in floor_population):

            # ...if it's morning or post-lunch, head to floor 1, since most people will probably want to enter the building...
            if timestamp.hour < 10 or 13 <= timestamp.hour < 14:
                return 1

            # ...otherwise head to the top floor, given most people will probably want to exit the building...
            else:
                return floors

        # ...but if there are people waiting on different floors, then...
        elif elevator_floor == t_floor:

            # ...head to the floor with the most people waiting
            most_desired_floor = floor_population.index(max(floor_population))
            return most_desired_floor

    # In all other cases, keep heading to the target floor.
    return t_floor
