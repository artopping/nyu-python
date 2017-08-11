#!/usr/bin/env python3

import sys
import math 

#class notes for class3: 
#reviewing classes- variables with __init___ are private...only accesible within the def 
# when you say property; you are saying getter/setter on a field/variable
# we're going to call this property "temp"

class Temperature: 
	def __init__(self): #__init__ is the constructor
		self._temp_fahr=0
	def __del__(self): # __del__ is the destructor
		print('In dtor')
#is used for closing connections 

	@property
	def temp(self):
		return (self._temp_fahr - 32)* 5 /9
	
	@temp.setter
	def temp (self, new_temp):
		self._temp_fahr= new_temp * 9/5 + 32

#you can call/create a subclass by doing 
class Weather(Temperature):



if __name__=='__main__':
	t= Temperature()
	print (t._temp_fahr)
	print (t.temp)
	t.temp=34
	print (t.temp)
	print (t._temp_fahr)



 

 
