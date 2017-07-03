#!/usr/bin/env python

#import pdb; pdb.set_trace() 

def to_fahrenheit(degrees_celsius):
    #degrees_celsius=int(raw_input("Enter a temprature in celsius: "))
    degrees_fahrenheit=(9.0/5.0 * degrees_celsius + 32)
    return degrees_fahrenheit
#print to_fahrenheit(0)

#to_fahrenheit ()

def to_celsius(degrees_fahrenheit):
    degrees_celsius= (degrees_fahrenheit - 32) * 5.0/9.0
    return degrees_celsius
#print to_celsius(32)

import math 

def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8
    fall_time = math.sqrt((2 * height) / acceleration_by_gravity)
    # replace with logic of above equation
    return fall_time
#print get_fall_time(70)

#last function
def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = math.sqrt((2 * tower_height) / 9.8) 

    tower_range = time_in_air * muzzle_velocity
    
    delta_x = tower_x - target_x  # difference between tower_x and target_x
    delta_y = tower_y - target_y  # difference between tower_y and target_y

    separation =math.sqrt((delta_x*delta_x) + (delta_y*delta_y)) 
# the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return separation
    else:
        print("The target is further than the tower range, what should we return?")
        return separation
print isVulnerable(70, 20, 20, 10, 15)

