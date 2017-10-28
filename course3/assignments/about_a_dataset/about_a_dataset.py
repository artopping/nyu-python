# about a dataset using pandas and numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
	# 94% of students were up to date in the 2013-2014 school year 
	# In January 2014 parents had to be counseled by a healthcare professional
	# of declare religious exemption, many of these students have neither
	# because they were entered into the system in the pre-Jan PBE time 
mean_2013= df_2013.groupby('CATEGORY')['PERCENT'].mean()
a= mean_2013.plot.bar()
plt.savefig('Figure1_2013')


df_2014 = df[df['SCHOOL YEAR'] == '2014-2015']
print df_2014.groupby('CATEGORY')['PERCENT'].mean()
	# from metadata, PBE started in Jan 2014. 
	# 96.5% of students are up to date
	# we see the the split of the PBE: 3% of students have PBE
		# 1.9% were counseled by a healtcare professional
		# 1.5% declared religious exemption 
		# the rest <0.01% where declared permanent medical exemption
mean_2014= df_2014.groupby('CATEGORY')['PERCENT'].mean()
b= mean_2014.plot.bar()
plt.savefig('Figure1_2014')


df_2015 = df[df['SCHOOL YEAR'] == '2015-2016']
print df_2015.groupby('CATEGORY')['PERCENT'].mean()
	# up to date declines slightly to 96% 
	# similar breakdown of religious/health care counseled PBE 
	# new field for overdue 0.7%
mean_2015= df_2015.groupby('CATEGORY')['PERCENT'].mean()
c=mean_2015.plot.bar()
plt.savefig('Figure1_2015')



# looking at it a little differently, up to date by year

df_uptodate = df[df['CATEGORY'] == 'Up-To-Date']
mean_uptodate= df_uptodate .groupby('SCHOOL YEAR')['PERCENT'].mean()
d= mean_uptodate.plot.bar()
d.set_ylim(.9,1)
plt.savefig('Figure1_uptodate')


# school type analysis 

df_uptodate_private = df[df['SCHOOL TYPE'] == 'PRIVATE']
mean_uptodate_private= df_uptodate_private.groupby('CATEGORY')['PERCENT'].mean()
print mean_uptodate_private

df_uptodate_public = df[df['SCHOOL TYPE'] == 'PUBLIC']
mean_uptodate_public= df_uptodate_private.groupby('CATEGORY')['PERCENT'].mean()
print mean_uptodate_public

# not seeing anything here : / 




