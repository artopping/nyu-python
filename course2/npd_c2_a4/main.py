#!/usr/bin/env python3

import os
import csv 
import json
import yaml 

import numpy
from numpy import loadtxt


file_name_json = 'input.json'
file_name_yaml = 'input.yaml'
file_name_csv = 'input.csv'


def input():
    with open(file_name_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        dict_list=[]
        for row in reader:
            #print(row)
            dict_list.append(row)
            csv_dict={} 
            csv_dict['csv']=dict_list
            print(csv_dict)
            with open('output.csv', 'w') as f:
                w=csv.writer(f)
                w.writerow(csv_dict.keys())
                w.writerow(csv_dict.values())
                
            with open(file_name_json, 'w') as f_json:
                json.dump(dict_list, f_json)
            json_dict={}
            json_dict['json']=dict_list    
            print(json_dict) 
            with open('output.json', 'w') as fj:
                json.dump(json_dict, fj)
    
            with open(file_name_yaml, 'w') as f_yaml:
                output= yaml.dump(dict_list, default_flow_style=False, explicit_start=True)
                yaml.dump (output, f_yaml)
            yaml_dict={}
            yaml_dict['yaml']=dict_list
            print(yaml_dict)
            with open ('output.yaml', 'w') as fy:
                output= yaml.dump(yaml_dict, default_flow_style=False, explicit_start=True)
                yaml.dump (output, fy)

if __name__=="__main__":
    input()




















