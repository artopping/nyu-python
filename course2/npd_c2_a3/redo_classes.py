#!/usr/bin/env python3

import sys
import math

#class Shape:
#    def __init__(self, name):
       
class Triangle:
    """equilateral triangle class"""

    def __init__(self, name):
        """creating triangle"""
        self.name= name
        self.shape_type ='Triangle'
        #self.edge_length=2
        self.triangle_perimeter=0
        self.edge_length=2
        self.sides=3
        self.allies= ['Circle']
        self.enemies= ['Square']
        self.role= ['aggressive']
 
    def area(self):
        """creating method for area"""
        self.area = ((3**0.5)/4)* self.edge_length**2
        return self.area 

    def perimeter(self):
        """creating method for perimeter"""
        self.triangle_perimeter += self.sides  * self.edge_length
        #return self.set_perimeter
        #self.triangle_perimeter += self.set_perimeter
        return self.triangle_perimeter

    def update_edge_length(self, change):
        """updating edge length"""
        self.edge_length += change

    def add_ally (self, shape_object):
        """adding ally shape"""
        if shape_object not in self.allies:
            self.allies.append(shape_object)

    def add_enemy (self, shape_object):
        """adding enemy"""
        if shape_object not in self.enemies:
            self.enemies.append(shape_object)
if __name__== "__main__":
        a= Triangle('Tom')
        a.add_ally('Circle')
        a.add_enemy('Square')
        print (a.triangle_perimeter)
        print (a.shape_type)
        print (a.allies)
        print (str(a.name) + " is a " + str(a.shape_type)+". Its enemies are "+ str(','.join(a.enemies))+" and its allies are " + str(','.join(a.allies))+".")  

class Square:
    """Square class"""
    shape_type ='Square'
    edge_length=2
    sides=4
    allies= []
    enemies= []
    role= ['complacent']

    def __init__(self, name):
        """creating triangle"""
        self.name= name

    def area(self):
        """creating method for area"""
        self.area = self.__class__.edge_length**2
        return self.area

    def perimeter(self):
        """creating method for perimeter"""
        self.perimeter= self.sides * self.__class__.edge_length
        return self.perimeter

    def update_edge_length(self, change):
        """updating edge length"""
        self.__class__.edge_length += change

    def add_ally (self, shape_object):
        """adding ally shape"""
        if shape_object not in self.__class__.allies:
            self.__class__.allies.append(shape_object)

    def add_enemy (self, shape_object):
        """adding enemy"""
        if shape_object not in self.__class__.enemies:
            self.__class__.enemies.append(shape_object)

class Circle:
    """Circle class"""
    shape_type ='Circle'
    edge_length=2
    sides=1
    allies= []
    enemies= []
    name= []
    role= ['wise']

    def __init__(self, name):
        """creating triangle"""
        self.name= name
    def area(self):
        """creating method for area"""
        self.area = math.pi*self.__class__.edge_length**2
        return self.area

    def perimeter(self):
        """creating method for perimeter"""
        self.perimeter= 2 * math.pi * self.__class__.edge_length
        return self.perimeter

    def update_edge_length(self, change):
        """updating edge length"""
        self.__class__.edge_length += change

    def add_ally (self, shape_object):
        """adding ally shape"""
        if shape_object not in self.__class__.allies:
            self.__class__.allies.append(shape_object)

    def add_enemy (self, shape_object):
        """adding enemy"""
        if shape_object not in self.__class__.enemies:
            self.__class__.enemies.append(shape_object)
 
