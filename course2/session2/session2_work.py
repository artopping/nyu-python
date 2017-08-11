#!/usr/bin/env python3

#iterator works on data structures that have mutiplicity
#when you traverse a list, you need an iterator 
#generator functions you can define your iterator
# return value with a yield iterator 
# local variables are saved from one call to the next
# because the compiler looks for the word "yield" 

def four():
	x=0 
	while x < 4:
		print ("in generator, x=", x)
		yield x
		x +=1

#decorators
#functions on functions
# taking a returned variable from a previous function 
# and makes another function out of it 
#function wrapped in another function 

def decorator(func):
	print ('in decorator function, decorating', func.__name__)
	def wrapper_func(*args):
		#print (*args) #this shows you which arguments you're passing into the decorator 
		print('Executing', func.__name__)
		return func(*args)
	return wrapper_func

@decorator #use this before the wrapping function is defined
def myfunction(parameter):
	print(parameter)

if __name__== '__main__':
	#myfunction= decorator(myfunction) ## using @decorate means you don't need this line
	#print (myfunction)
	myfunction("hello")
 
	exit (0)

	
#using a decorator involes two parts
# one inside another ....something about an ampersand
'''
if __name__== "__main__":
	for i in four():  #i is the iterator/ iteration
		print (i) # this is the iteration
'''

