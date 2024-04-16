import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')

'''
#######Steps########
- Choose relevant columns
- Get Dummy data (for Categorical Data)
- train test split
- models:
    1. multiple linear regression
    2. Lasso regression
    we use 'lasso regression' because this data set is
    going to be so sparse with all these dummy variables
    that actually helps us normalize that.
    3. Random forest --> so we will have a tree based 
    model to compare to our linear models.
- Tune models using GridsearchCV
- Test ensembles
'''

# 1. Choose relevant columns
df.columns
df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'num_comp', 'hourly', 'employer_provided', 'job_state', 'same_state', 'age', 'python_yn', 'spark', 'aws', 'job_simp', 'seniority', 'desc_len']]

# 2. Get Dummy data (for Categorical Data)
# Using OneHotEncoder
df_dummies = pd.get_dummies(df_model)

# 3. train test split
from sklearn.model_selection import train_test_split
x = df_dummies.drop('avg_salary', axis = 1)
y = df_dummies.avg_salary.values #recommended to be used
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#4. Models
# 4.1 Multiple Linear regression
import statsmodels.api as sm
x_sm = sm.add_constant(x)
model = sm.OLS(y, x_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score 

lm = LinearRegression()
lm.fit(x_train, y_train)

np.mean(cross_val_score(lm, x_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

# 4.2 Lasso Regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l, x_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
