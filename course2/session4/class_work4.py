#!/usr/bin/env python3

import sys
import math 
import os

#start reading about design patterns (book Gamma)

cwd= os.getcwd()
file_name= os.path.join(cwd, 'test_file.dat')
file_object= open (file_name, 'r')
line = file_object.readline()
print(line) 
file_object.close()


