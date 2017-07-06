#!/usr/bin/env python

import csv
import pdb

f = csv.reader(open("LBMA-GOLD.csv", "rU"))

USAM = []
USPM = []
for row in f:
    USAM.append(row[2])
    USPM.append (row[3])
print len(USAM)
print len(USPM)


#USAM=[]
#for row in f:
#    USAM.append(row[2])
   # print(row)
#print USAM
#print len(USAM)
#f = csv.reader(open("LBMA-GOLD.csv", "rU"))

#USPM=[]
#for row in f:
#    USPM.append(row[3])
   # print(row)
#print USPM
#print len(USPM)
