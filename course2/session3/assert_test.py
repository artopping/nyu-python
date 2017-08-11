#!/usr/bin/env python3

#types of tests:
#class testing
	#unittesting
#integration tests
#performance tests/ profiling 
# if you want to turn debugging off then run "python3 -O" in command line

#doc tests- you set up command line shell scripting in your .py 
#and if it matches then it passes, but if not it throws an error 

  
def example(param):
	"""param must be greater than 0"""
	assert param >0
	#if __debug__:
	#	if not param >0 
	#		raise AssertionError 
	# do stuf here...

if __name__ == '__main__':
	#__debug__= False 
	example(-1)



