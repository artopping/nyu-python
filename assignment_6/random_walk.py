#!/usr/bin/env python

import random 
import sys
import math 

def get_random_direction():
    #global direction 
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

def get_direction_displacement():
    #global displacement
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }
    displacement = displacements.get(get_random_direction())
    return displacement

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()
        displacement = get_direction_displacement()
        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]
        current_location[0] += delta_x
        current_location[1] += delta_y 
    return current_location
        # UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update
        # current_location

def take_all_walks(steps, runs):
    endpoints = []
    for run_index in range(runs):
        end_location = take_walk(steps)
        endpoints.append(end_location)
    return endpoints
    return end_location
    print endpoints

def average_final_distance(endpoints):
    total_distance = 0
    for coords in endpoints:
        dx = coords[0]
        dy = coords[1]

        #use the Pythagorean theorem to get distance like last session
        distance = math.sqrt(dx*dx + dy*dy)
        total_distance += distance 
    return total_distance / len(endpoints)

if  __name__ == "__main__":
    #get_random_direction()
    #get_direction_displacement()
    steps = 10
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])
    runs = 1
    if len(sys.argv) > 2:
        runs = int(sys.argv[2])
    
    # REPLACE take_walk WITH take_all_walks
    end_locations = take_all_walks(steps, runs)
    current_location = take_walk(steps)
    #if len(sys.argv) > 1:
        #steps = int(sys.argv[1])
    #print("Done with walk, printing end location: ")
    #print(current_location)
    print end_locations

    average_displacement = average_final_distance(end_locations)
    print(average_displacement)

