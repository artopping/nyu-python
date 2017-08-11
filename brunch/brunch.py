#!/usr/bin/env python3

import sys 
import math 

def usr_input():
	print ("Lets Brunch!")
	while True:
		try:
			number= int(input("How many people are coming?: "))
			break 
		except ValueError:
			print ("Woops! Please enter a number only, no letters")
	while True: 
		try:
			booze= int(input("Perfect, what level of boozy are you looking for? \n (Pick a number 1 to 5: 1=not really interested in drinking 5=wanna get day drunk):"))
			break
		except ValueError:
			print ("Woops! Please enter a number only, no letters")
	if (booze>5) or (booze<1):
		print ("Please pick a number between 1 and 5"
	booze= booze += int(input ("Perfect, what level of boozy are you looking for? \n (Pick a number 1 to 5: 1=not really interested in drinking 5=wanna get day drunk):"))
	while True: 
		try: 
			price= int(input("How much are you looking to spend per person?"))
			break 
		except ValueError:
			print ("Woops! Please enter a number only, no letters")
	print ("Great! Here are you top three choices") 
	return (number, booze, price) 

if __name__== "__main__":
	usr_input()


