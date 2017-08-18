#!/usr/bin/env python3

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('/vagrant/course2/data_project/jira_dataset.csv')

#overall charts and trends

def project_teams(x):
    if x in ['jevans', 'jhoule', 'mpuello', 'kyang']:
        return 'applications'
    elif x in ['rdw', 'ysaxena', 'scarnes']:
        return 'development'
    elif  x in ['smeltzer', 'tpenn', 'awestfall']:
        return 'infrastructure'
    else:
        return 'other'

df['team']= df.person.apply(project_teams)
print(df.head())

def team_count():
    """getting team info"""
    global df 
    team='applications'
    df_team= df.loc[(df.team==team)]
    #df_team_people= df_team['person'].aggregate(['count'])
    df_team_people= df_team.groupby('team')['person'].nunique()
    print(df_team_people)

if __name__=="__main__":
    #project_teams()
    team_count()
