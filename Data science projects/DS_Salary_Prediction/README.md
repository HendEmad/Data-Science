This is an educational project I made to practice the machine learning project steps.


# Project Overview
- Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
- Scraped over 1000 job descriptions from glassdoor using python and selenium
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

# Code and Resources Used:

**Python Version:** 3.8

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium

**Scraper Github:**
https://github.com/arapfaik/scraping-glassdoor-selenium

**Scraper Article:**
https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

# Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

# Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
    - Python
    - R
    - Excel
    - AWS
    - Spark
    - Column for simplified job title and Seniority
    - Column for description length

# EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![salary_by_job_title](https://user-images.githubusercontent.com/91827137/168488155-fd824549-5ef0-4ab9-a6b0-1272e70886ea.png)

![positions_by_state](https://user-images.githubusercontent.com/91827137/168488164-a2e68576-3919-4157-b004-f78136eab501.png)

![correlation_visual](https://user-images.githubusercontent.com/91827137/168488167-26a882c0-86d9-44b8-ba38-2426bc1cee58.png)
