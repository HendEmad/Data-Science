import glassdoor_web_scraping as gs 
import pandas as pd 

path = "C:/Users/Data/Documents/DS_Salary_Proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)