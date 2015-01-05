#import libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

#read the data file, as per my mentor I'm using the file used in Logistic Regression
loansdata = pd.read_csv('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/Unit2/MultivariateAnalysis/loansData_clean.csv')
loansdata.dropna(inplace=True)

#Using monthly income instead of annual income as they are similar
intrate = loansdata['Interest.Rate']
mincome = loansdata['Monthly.Income']

#model income and interest rate
y = np.matrix(intrate).transpose()
x1 = np.matrix(mincome).transpose()
X = sm.add_constant(x1)
model = sm.OLS(y,X)
f = model.fit()
print(f.params)

'''f.params[0] = slope = 1.29928557e+01, f.params[1] = intercept = 1.36340866e-05. Thus, the equation of the line is
y = 1.29928557e+01x + 1.36340866e-05'''

#Add home ownership (home_ownership) and income to the model.
homeownership = loansdata['Home.Ownership']
homeownership = [4 if x=='OWN' else 3 if x=='MORTGAGE' else 2 if x=='RENT' else 1 if x=='OTHER' else 0 for x in homeownership]
x2 = np.matrix(homeownership).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()
print(f.params)

'''1.41859602e+01   2.23592646e-05  -4.74734171e-01 are the params value. So, slope of x1 = 1.41859602e+01, slope of x2 = 2.23592646e-05 and intercept = -4.74734171e-01. Thus, the equation of the linear equation is y = -4.74734171e-01 + 1.41859602e+01*monthly_income + 2.23592646e-05*homeownership

#add just home-ownership to the model
X = sm.add_constant(x2)
model = sm.OLS(y, X)
f = model.fit()
print(f.params)

'''14.27096089  -0.4586451 are the param values. Thus, y = 14.27096089*homeownership - 0.4586451 is the equation of the line. 
In each of the three models, the coefficients are changing significantly.''' 






