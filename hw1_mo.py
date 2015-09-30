'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('~Mo/Mo_Git/SF_DAT_17/hw/data/police-killings.csv')

#examine the data
killings.describe
killings.columns
# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings = killings.rename(columns = {'lawenforcementagency': 'agency'} )
killings = killings.rename( columns ={'raceethnicity':'race'})

# 2. Show the count of missing values in each column
killings.isnull().sum()


# 3. replace each null value in the dataframe with the string "Unknown"
killings.fillna(value = 'Unknown')
killings = pd.read_csv('~Mo/Mo_Git/SF_DAT_17/hw/data/police-killings.csv', na_filter = False)
killings.isnull().sum #had to rename the columns again, why? anyway around that?

# 4. How many killings were there so far in 2015?
killings.shape
#answer: 467 killings total (one per row)

# 5. Of all killings, how many were male and how many female?
killings.gender.value_counts()
# answer: 445 male, 22 female


# 6. How many killings were of unarmed people?
killings.armed.value_counts()
#killings.armed.value_counts('No') ##why doesn't this one work?
#answer: 102 No


# 7. What percentage of all killings were unarmed?


# 8. What are the 5 states with the most killings?
killings.state.value_counts().order(ascending = False).head()

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

# 10. Display a histogram of ages of all killings
import matplotlib.pyplot as plt
killings.age.hist()


# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex= True, sharey = True)
killings.age.hist(by=killings.race, sharex = True)

# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
killings.month.value_counts() #to explore data
killings.month.value_counts().plot(kind = 'bar', title = 'Deaths Counts per Month')


###################
### Less Morbid ###
###################

majors = pd.read_csv('~Mo/Mo_Git/SF_DAT_17/hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
majors.columns
del majors['Employed_full_time_year_round']
del majors['Major_code']

# 2. Show the count of missing values in each column
majors.isnull().sum()
#no missing values?

# 3. What are the top 10 highest paying majors?
majors.columns
majors.head(5) #tosee the data/means of column names
majors.groupby('Major').Median.mean().order(ascending = False).head(5)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
top_majors = majors.groupby('Major').Median.mean().order(ascending = False).head(5)
top_majors

# 5. What is the average median salary for each major category?
majors.groupby('Major_category').Median.mean().order(ascending = False)

# 6. Show only the top 5 paying major categories
majors.groupby('Major_category').Median.mean().order(ascending = False).head(5)

# 7. Plot a histogram of the distribution of median salaries
majors.Median.hist(bins=20)

# 8. Plot a histogram of the distribution of median salaries by major category
majors.Median.hist(by=majors.Major_category, sharex = True, sharey = False, bins=20)
### why doesn't the above work?
#majors.groupby('Major_category').Median.hist(bins = 20)

# 9. What are the top 10 most UNemployed majors?
majors.groupby('Major').Unemployed.mean().order(ascending = False).head(10)
#if you want in sheer numbers

# What are the unemployment rates?
majors.groupby('Major').Unemployment_rate.mean().order(ascending = False).head(10)



# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
 majors.groupby('Major_category').Unemployed.mean().order(ascending = False).head(10)
# What are the unemployment rates?
 majors.groupby('Major_category').Unemployment_rate.mean().order(ascending = False).head(10)

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors['sample_employment_rate'] = majors['Employed'] / majors['Total']
majors.columns
majors.head(2)
#to check
# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_unemployment_rate_1'] = majors['Unemployed'] / majors['Total']
majors['sampled_unemployement_rate_2'] = 1-majors['sample_employment_rate']
majors.head(2)
#why are these not the same? should't they be?
