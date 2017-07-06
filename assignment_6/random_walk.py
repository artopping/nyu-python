#!/usr/bin/env python

import random 
import sys
import math 


def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "west"
    elif 0.25<=probability<0.5:
        direction= "north"
    elif 0.5<= probability<0.75:
        direction= "south" 
    else:
        direction = "east"
    return direction
#print get_random_direction()

def get_direction_displacement(dir_key):
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }

    # access the dictionary
    # UPDATE HERE: how do you use the key to access a dictionary?
        # displacements[1]['west']
        #for key in newdict.keys():
        #print(key)
    # replace None with the answer
    for key in displacements.keys():
        return(key)
    #return dict["displacements"]
    #return dict['displacements'].keys()

# example of state, don't add to your file yet
#example_location = [0, 0]

# if you wanted to simulate moving 1 unit in the negative x
# direction, you would update the values in this list
#change_in_x = -1
#change_in_y = 0
#example_location[0] += change_in_x
#example_location[1] += change_in_y

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()

        displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]

        # UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update
        # current_location

    return current_location
#print take_walk(10)

def take_all_walks(steps, runs):
    endpoints = []
    for run_index in range(runs):
        end_location = take_walk(steps)
        endpoints.append(end_location)
    return endpoints

def average_final_distance(endpoints):
    total_distance = 0
    for coords in endpoints:
        dx = coords[0]
        dy = coords[1]

        # use the Pythagorean theorem to get distance like last session
        distance = math.sqrt(dx*dx + dy*dy)

        total_distance += distance

    return total_distance / len(endpoints)

if __name__ == "__main__":
    steps = 10
    # ADD THESE NEW LINES
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])
    
    # ADD THESE NEW LINES
    runs = 1
    if len(sys.argv) > 2:
        steps = int(sys.argv[2])

    # REPLACE take_walk WITH take_all_walks
    end_locations = take_all_walks(steps, runs)
    current_location = take_all_walks(steps, runs)
    print("Done with walk, printing end location: ")
    print(current_location)
    #print(end_locations)
    average_displacement = average_final_distance(end_locations)
    print(average_displacement)


