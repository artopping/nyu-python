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

data = dict()

with open(file_name_csv, 'r') as csvfile:
    d_reader = csv.DictReader(csvfile)
    dict_list = []

    headers = d_reader.fieldnames
    print(headers)

    for x in d_reader:
        dict_list.append(x)

    with open(file_name_json, 'w') as f_json:
        json.dump(dict_list,f_json)

    with open(file_name_yaml, 'w') as f_yaml:
        output = yaml.dump(dict_list, default_flow_style=False, explicit_start=True)
        yaml.dump(output,f_yaml)


with open(file_name_yaml, 'r') as f_yaml:
    yaml_str = yaml.load(f_yaml)
    print(type(yaml_str))
