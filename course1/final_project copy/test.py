#!/usr/bin/env python3

import csv
import pdb
from sys import argv 
import sys
import statistics 

f = open("LBMA-GOLD_final.csv", "rU")
data= csv.reader(f)
print (data)

def test(year):
	list_year=[year]
	for row in data:
		row=[float(x) for x in row[1:5]]
		row[0]=int(row[0])
		if year==row[0]:
			list_year.append(row[2])
	length=len(list_year)-1
	total=sum(list_year[1:length])
	avg=total/length
	#stand_dev=statistics.stdev(list_year[1:length])
	max_price=max(list_year[1:length]) 
	print('Year '+str(year)+' - '+'Avg. Price: $'+str(avg)+' | Max. Price: $'+str(max_price))

if __name__ =="__main__":
    year=sys.argv[1]
    test(year)

'''
    print('Year '+str(year)+' - '+'Avg. Price: $'+str(avg)+' | '+'Std. Dev: '+str(stand_dev)+' | Max. Price: $'+str(max_price))

#data= [row for row in f]
#data=[[ str(row[0]), eval(row[1]), eval(row[2]), eval(row[3])] for row in data]

data1 = [[str(row[0]), eval(row[2]), eval(row[3]), eval(row[3])-eval(row[2])] for row in data]
date= [str(row[0]) for row in data1]
diff= [int(row[3]) for row in data1]
d = {'a': [], 'b': []}
d['a'].append(date)
d['a'].append(diff)
print (d['a'])

max_diff= max([sublist[-1] for sublist in data1])
date = [row for row in data1 if max_diff in row[3]]
for row in data1:
	#if max_diff in data1[int(row[3])]:
		#print (data1.index[row])
	#else print("didn't work")

#for row in data1:
	#if row[3]==max_diff 
	#return row[0]
	#print row[0]
print(max_diff) 
print (date)


years= set()
for row in data1:
	years.add(int(row[1]))
	#print (years) 
print(data1)

#for row in data1:
	#if row[0]==years
'''		
