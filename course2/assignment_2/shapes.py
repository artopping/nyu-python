#!/usr/bin/env python3

import sys
import math

class Triangle:
    """equilateral triangle class"""
    shape_type ='Triangle'
    edge_length=2
    sides=3
    allies= []
    enemies= []
    role= ['aggressive']

    def __init__(self, name):
        """creating triangle"""
        self.name= name
			
    def area(self):
        """creating method for area"""
        self.area = ((3**0.5)/4)* self.__class__.edge_length**2
        return self.area 

    def perimeter(self):
        """creating method for perimeter"""
        self.perimeter= self.__class__.sides  * self.__class__.edge_length
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

if __name__== "__main__":
    a= Triangle('Tom')
    a.add_ally('Circle')
    a.add_enemy('Square')
    print (a.perimeter())
    print (str(a.name) + " is a " + str(a.shape_type)+". Its enemies are "+ str(','.join(a.enemies))+" and its allies are " + str(','.join(a.allies))+".")

    b= Triangle('Ted')
    b.add_ally('Circle')
    b.add_enemy('Square')
    print (str(b.name) + " is a " + str(b.shape_type)+". Its enemies are "+ str(','.join(b.enemies))+" and its allies are " + str(','.join(b.allies))+".")
 
    c= Square('Sam')
    c.add_enemy('Triangle')
    c.add_enemy('Circle')
    print (str(c.name) + " is a " + str(c.shape_type)+". Its enemies are "+ str(','.join(c.enemies))+" and its allies are " + str(','.join(c.allies))+".")

    d= Square('Sir')
    d.add_enemy('Triangle')
    d.add_enemy('Circle')
    print (str(d.name) + " is a " + str(d.shape_type)+". Its enemies are "+ str(','.join(d.enemies))+" and its allies are " + str(','.join(d.allies))+".")

    e= Circle('Cam')
    e.add_enemy('Square')
    e.add_ally('Triangle')
    print (str(e.name) + " is a " + str(e.shape_type)+". Its enemies are "+ str(','.join(e.enemies))+" and its allies are " + str(','.join(e.allies))+".")	

    f= Circle('Cara')
    f.add_enemy('Square')
    f.add_ally('Triangle')
    print (str(f.name) + " is a " + str(f.shape_type)+". Its enemies are "+ str(','.join(f.enemies))+" and its allies are " + str(','.join(f.allies))+".") 
