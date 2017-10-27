# about a dataset using pandas and numpy

import pandas as pd
import numpy as np

df= pd.read_csv ('school_immunizations.csv')
df= df.dropna()

#print df.head(100)

#had to change PERCENT from object to numeric with this code 
df['PERCENT']= pd.to_numeric (df['PERCENT'])
print df.info()
print df.groupby('CATEGORY')['PERCENT'].mean()
	# 95% of all 7th graders are up to date on their immunizations. 

# School Year Analysis 

df_2013 = df[df['SCHOOL YEAR'] == '2013-2014']
print df_2013.groupby('CATEGORY')['PERCENT'].mean()

# School Year Analysis 

df_2014 = df[df['SCHOOL YEAR'] == '2014-2015']
print df_2014.groupby('CATEGORY')['PERCENT'].mean()

# School Year Analysis 

df_2015 = df[df['SCHOOL YEAR'] == '2015-2016']
print df_2015.groupby('CATEGORY')['PERCENT'].mean()


