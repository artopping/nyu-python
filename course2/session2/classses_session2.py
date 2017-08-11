#!/usr/bin/env python3

#Classes: storage of data and set of functions that define the class
# class has a function and data (local to itself)
# when you want to use it< instance= MyClass()>

class MyClass:
	pass 

#obect my_circle as instance of Class circle
# think of class as bucket...lot of room, for data storage and defs
#
class Circle:
	pi = 3.14159
	def __init__(self, radius=1): #self is container that everything is placed in 
		self.radius=radius
	
	def area(self):
		#return self.radius**2  *3.14159
		return self.radius**2 * Circle.pi #using the global class 

if __name__=='__main__':
	my_circle = Circle(2)
	print (my_circle.area())
	my_circle.radius=10
	print (2*3.14159*my_circle.radius)
	
 
