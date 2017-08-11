#!/usr/bin/env python3

import os
import csv 
import json
#import yaml 

#import numpy
#from numpy import loadtxt


def input_csv():
    with open("input.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
def output_csv():
    csvfile= open("input.csv", mode='r')
    reader = csv.reader(csvfile)    
    with open("output.csv", mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
        csvfile.seek(0)
        print (mydict)
def input_json():
    #with open('input.json') as data_file:
    with open('input.json', encoding = "ISO-8859-1") as data_file:    
        data = json.load(data_file)
    print (data)

def create_json():
    j = json.dumps({"first_name":'Aaron' , "last_name": 'Morton', "dob_month": 'July', "dob_year": '1987', "color": 'green', "movie":'Top Gun'}, sort_keys=True)
    print (j)


#def input_yaml(): 
    

if __name__=="__main__":
    input_csv()
    output_csv()
    #input_json() 
    create_json()
    #input_yaml()


'''
with open('input.json') as jsonfile:
    data=json.load(jsonfile)
print(data)

 18     cwd = os.getcwd()
 19     file_name = os.path.join(cwd,'input.json')
 20     with open(file_name,'r') as f:
 21         my_data = json.load(f)
 22     print (my_data)


'''
