#!/usr/bin/env python3

import os
import csv 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('/vagrant/course2/data_project/jira_dataset.csv')
#print (df)

print(df.head())
