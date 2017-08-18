#!/usr/bin/env python3

import os
import csv 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

#import team info for team classification
from team_info import project_teams

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('/vagrant/course2/data_project/jira_dataset.csv')
df['team']= df.person.apply(project_teams)

class Team:    
    def __init__(self,team):
        global df
        self.df= df
        self.team=team
        self.df_team= self.df.loc[(self.df.team==self.team)]
        self.df_team_component= self.df_team.groupby(self.df_team.component)

    def team_worklogs (self):
        worklogs= self.df_team.groupby('team')['worklog_id'].nunique()
        #print(worklogs.iloc[0])
        return worklogs.iloc[0]

    def team_hours (self):
        self.df_team_hours= self.df_team['time_spent'].aggregate(['sum'])
        #print(self.df_team_hours.iloc[0])
        return self.df_team_hours.iloc[0]

    def team_hours_breakfix(self):
        breakfix=self.df_team.loc[(self.df_team.component=='break/fix')]
        breakfix_hours= breakfix['time_spent'].aggregate(['sum'])
        total_hours= self.df_team_hours
        percent_breakfix= (breakfix_hours/total_hours)*100
        return percent_breakfix.iloc[0]

    def team_component_worklogs(self):
        df_team_component_worklog= self.df_team_component['worklog_id'].aggregate(['count'])
        df_team_component_worklog_10=df_team_component_worklog.nlargest(10,'count')
        df_team_component_worklog_10.plot(kind='barh', legend=False)
        plt.ylabel('Component')
        plt.xlabel('Total work logs')
        plt.show()
        #fig.savefig('Figure1_.jpg')

    def team_component_time (self):
        df_team_component_time= self.df_team_component.aggregate({'time_spent':np.sum})
        df_team_component_time_10=df_team_component_time.nlargest(10,'time_spent')
        df_team_component_time_10.plot(kind='barh', legend=False)
        plt.ylabel('Component')
        plt.xlabel('Total hours')
        plt.show()
        #plt.savefig('Figure2_.png')

    def over_time(self):
        self.df_team['date_format']=pd.to_datetime(self.df_team['date'])
        df_over_time= self.df_team.groupby('date_format')[ 'worklog_id'].nunique()
        plt.plot(df_over_time)
        plt.xlabel('Date')
        plt.ylabel('Number of worklog IDs')
        #plt.legend()
        plt.show()
        #savefig('Figure3_.jpg')
        #print(df_time)  

if __name__== "__main__":
    print("Which team's data would you like to look at? (options: applications, development, infratrucutre)")

    team_input= input()
    a=Team(team_input)

    print("You have selected " + str(team_input)+". Here is the team breakdown:")
    b=a.team_worklogs()
    print("The total number of worklogs logged this year is:")
    print(str(b))
    print("See plot for breakdown of worklogs by component")
    a.team_component_worklogs()
    #print(b)
    print("The total number of hours logged this year is:")
    print(str(a.team_hours()))
    print("See plot for breakdown of hours by component")
    a.team_component_time()
    #print(c)
    print('The percentage of hours attributed to break/fix components is:')
    print(str(a.team_hours_breakfix()))
    print("See plot for worklog over time.") 
    a.over_time()


