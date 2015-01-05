#import libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

#read the data file
loansdata = pd.read_csv('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/Unit2/MultivariateAnalysis/LoansData_clean.csv', header=True)

'''read the three required columns -- can't do this, creting tuples. 
annualincome = loansdata['annual_inc']
intrate = loansdata['int_rate']
homeownership = loansdata['home_ownership']
#create the new table using the three required columns
loansdata2 = annualincome, intrate, homeownership'''

'''replace the nan values with zeros -- this works but not going to use
annualincome[np.isnan(annualincome)] = 0
annualincome[np.isnan(intrate)] = 0
annualincome[np.isnan(homeownership)] = 0'''

#create another data file with the required columns
#this doesn't work, not sure why--loansdata2=loansdata['annual_inc', 'int_rate', 'home_ownership']
requiredcolumns = ['annual_inc', 'int_rate', 'home_ownership']
loansdata2 = loansdata[requiredcolumns]

#remove the nan rows
loansdata2 = loansdata2.dropna(inplace=True)

#clean up the intrate column
#intrate = intrate.map(lambda x: x.rstrip('%'))
#print(intrate[0:20])












