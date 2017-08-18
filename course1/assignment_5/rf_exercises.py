#!/usr/bin/env python3

import math 
import sys

def get_fall_time():
    height=20
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8
    fall_time = math.sqrt((2 * height) / acceleration_by_gravity)
    # replace with logic of above equation
    return fall_time

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300 
    time_in_air = get_fall_time() #refactored to just use previous function instead of calculation
    tower_range = time_in_air * muzzle_velocity
    
    delta_x = tower_x - target_x  # difference between tower_x and target_x
    delta_y = tower_y - target_y  # difference between tower_y and target_y

    separation =math.sqrt((delta_x**2) + (delta_y**2)) #refactored to use **2 instead of x*x

# the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?\n" + str(separation))
        return separation
    else:
        print("The target is further than the tower range, what should we return?\n" + str(separation))
        return separation
#refactored printing to print separation within a single print function instead of two lines

if __name__=='__main__':
    get_fall_time()
    isVulnerable(50, 10, 20, 10, 15)


