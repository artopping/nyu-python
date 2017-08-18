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

#pdb.set_trace()
 
USD = list(zip(USAM, USPM))
USD1 = USD[:]
USD2 = list(USD)
print USD2

if __name__ == "__main__":
    print len(USAM)
    print len(USPM)
    print USD2
