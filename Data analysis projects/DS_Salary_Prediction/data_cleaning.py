import pandas as pd
df = pd.read_csv('glassdoor_data.csv')

'''
What we will do is:
Salary Parsing
Taking company name text only
State field
Age of company
Job description parsing (python, etc.)
'''
# 1. salary parsing

# Removing un-meaningful salaries
df = df[df['Salary Estimate'] != '-1']

# Removing the text unneeded in salary column 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

# Removing the 'K's and '-'  
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

# Creating column for the per hour's salary
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

# Creating column for employer provided's salary
df['emplyer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

# Removing 'per hour' and 'employer provided salary' from salary column
minus_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

# Creating min_salary, max_salary, and avg. salary columns
df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# 2. Taking company name text only
df['Company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# 3. State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# 4.Age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2022 - x)

# 5. Job description parsing (python, etc.)
# df['Job Description'][0]

#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# df.python.value_counts()

#r studio
df['rstudio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
# df['rstudio'].value_counts()

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# df['spark'].value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
# df['aws'].value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# df.excel.value_counts()

# df.columns

# Drop the first un-needed column
df_2 = df.drop(['Unnamed: 0'], axis = 1)

df_2.to_csv('salary_data_cleaned.csv', index = False)
# pd.read_csv('salary_data_cleaned')