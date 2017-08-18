    applications= ['jevans', 'jhoule', 'mpuello', 'kyang']
    development= ['rdw', 'ysaxena', 'scarnes']
    infrastructure= ['smeltzer', 'tpenn', 'awestfall']

df_app= df.loc[df.person.isin(applications)]
 51     df_app_break= df_app.loc[df_app.component.isin(break_component)]
 52     df_dev= df.loc[df.person.isin(development)]
 53     df_inf= df.loc[df.person.isin(infrastructure)]
 54 
 55 
 56     df_app_component=df_app.groupby(df_app.component)
 57     df_app_component_time= df_app_component.aggregate({'time_spent':np.sum})
 58     #print (df_app_component_time)
 59     app_time=df_app_component_time.nlargest(10,'time_spent')
 60     app_time.plot(kind='barh')
 61     #plt.show()
 62     #plt.bar(df_app_component_time.time_spent, df_app_component_time.component, align='center', alpha=0.5)
 63     #df_app_component_time[:10].sort(ascending=0).plot(kind='barh')
 64 
 65     df_dev_component= df_dev.groupby(df_dev.component)
 66     df_dev_component_time= df_dev_component.aggregate({'time_spent':np.sum})
 67     #print (df_dev_component_time)
 68     dev_time= df_dev_component_time= df_dev_component_time.nlargest(10, 'time_spent')
 69     dev_time.plot(kind='barh')
 70     #plt.show()
 71 
 72     df_inf_component=df_inf.groupby(df_inf.component)
 73     df_inf_component_time= df_inf_component.aggregate({'time_spent': np.sum})
    

'''

    def component(self, component):
    """getting team component break down"""
        self.component=component
        df_component= df_team.loc(df_team.component==self.component)
        return df_component
    def component_time(self):
        df_team_component_time= df_team_component.aggregate({'time_spent':np.sum})
        #plot
    
        df_team_component_time=df_team_component_time.nlargest(10,'time_spent')
        df_team_component_time.plot(kind='barh')

    def aggregate(self):
        """aggregating data by team and component"""
        #suming the amount of hours spent on break/fixes by teams this year
        df_team= df.loc[(df.team==self.team)
        df_team_component= df_team.loc[(df_team.component==self.component)]
    
        df_team_component_time= df_team_component.aggregate({'time_spent':np.sum})
        df_team_component_time=df_team_component_time.nlargest(10,'time_spent')
        df_team_component_time.plot(kind='barh')
        df_component= df.groupby(df.component)
        df_component_time= df_component.aggregate({'time_spent':np.sum})
                          
