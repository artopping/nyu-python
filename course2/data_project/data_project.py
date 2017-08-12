#!/usr/bin/env python3

import os
import csv 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('/vagrant/course2/data_project/jira_dataset.csv')
#print (df)
#print(df.head())

#overall charts and trends
def aggregate():
    """aggregating data by team and component"""
    applications= ['jevans', 'jhoule', 'mpuello', 'kyang']
    development= ['rdw', 'ysaxena', 'scarnes']
    infrastructure= ['smeltzer', 'tpenn', 'awestfall']
    df_break= df.loc[(df.component=='break/fix')]
    #print (df_break.head())
    df_component= df.groupby(df.component)
    df_component_time= df_component.aggregate({'time_spent':np.sum})
    print(df_component_time)
    
    df_app= df.loc[df.person.isin(applications)]
    df_dev= df.loc[df.person.isin(development)]
    df_inf= df.loc[df.person.isin(infrastructure)]

    df_app_component=df_app.groupby(df_app.component)
    df_app_component_time= df_app_component.aggregate({'time_spent':np.sum})
    print (df_app_component_time)
    app_time=df_app_component_time.nlargest(10,'time_spent')
    app_time.plot(kind='barh')
    plt.show()
    #plt.bar(df_app_component_time.time_spent, df_app_component_time.component, align='center', alpha=0.5)
    #df_app_component_time[:10].sort(ascending=0).plot(kind='barh')

    df_dev_component= df_dev.groupby(df_dev.component)
    df_dev_component_time= df_dev_component.aggregate({'time_spent':np.sum})
    print (df_dev_component_time)
    
    df_inf_component=df_inf.groupby(df_inf.component)
    df_inf_component_time= df_inf_component.aggregate({'time_spent': np.sum})
    print (df_inf_component_time)
    
    return df_app_component_time
    return df_dev_component_time
    return df_inf_component_time
'''    df_project= df.groupby(df.project)
    #print(df_project)
    df_project_worklogs= df_project.sum()
    df_project_time= df_project.aggregate({'time_spent':np.sum})
    #print(df_project_time)
    df_project_worklogs= df_project.aggregate({'worklog_id':pd.nunique})
    #print(df_project_worklogs)
    df_project_worklogs= df.groupby(['project']).agg({'worklog_id':lambda x:x.count()})
    #print(df_project_worklogs)
    df_project_empl= df.groupby(['project']).apply({'person':lambda x:x.nunique()})
    df_project_empl= df.apply(pd.Series.nunique)
    #print(df_project_empl)
   ''' 
def plots(df_app_component_time):
    df_time = df.drop(['worklog_id','issue_id', 'project', 'person', 'component', 'component_description', 'time_spent', 'date'], axis=1)
    exclude_time= ['issue_id', 'project', 'person', 'component', 'component_description', 'time_spent', 'date']
    #df.ix[:,df.columns.difference(exclude_time)].plot(kind='bar')
    #print(df_time.head())
    #time= df (mdates.date2num(df_time))
    #plt.hist(time.values)
    #plt.savefig(time.png)
    #plt.show
    
    df_app_component_time[:10].sort(ascending=0).plot(kind='barh')
     
    #df['time'].hist(by=df['project'])
    #print (p)


#creating a Team class that gives metrics by office/team
class Team:
    def __init__(self, team_name):
        self.team_name=team_name
        d1=df.query ('project== "team_name"')
        return team_name

    def work(self):
        d1['worklog_count']= d1.groupby(['project'].transform(lambda x:x[x.str.contains(team_name).count()]))
        print(d1)

    def time(self):
        return none
        
if __name__== "__main__":
    aggregate()
    #plots()

