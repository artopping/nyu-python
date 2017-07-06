#!/usr/bin/env python

import csv 

with open("LBMA-GOLD.csv") as myfile:
    head = [next(myfile) for x in xrange(180)]
print head



#N=180
#with open("LBMA-GOLD.csv") as file:
#    for i in range(N):
#       break 
#       print file.next()
