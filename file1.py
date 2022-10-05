#!/usr/bin/env python
# coding: utf-8

# In[2]:


import jovian


# In[3]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# In[4]:


# Run the next line to install Pandas
get_ipython().system('pip install pandas --upgrade')


# In[5]:


import pandas as pd


# In this assignment, we're going to analyze an operate on data from a CSV file. Let's begin by downloading the CSV file.

# In[6]:


from urllib.request import urlretrieve

urlretrieve('https://gist.githubusercontent.com/aakashns/28b2e504b3350afd9bdb157893f9725c/raw/994b65665757f4f8887db1c85986a897abb23d84/countries.csv', 
            'countries.csv')


# Let's load the data from the CSV file into a Pandas data frame.

# In[7]:


countries_df = pd.read_csv('countries.csv')


# In[8]:


countries_df


# **Q1: How many countries does the dataframe contain?**
# 
# Hint: Use the `.shape` method.

# In[10]:


num_countries = countries_df.shape[0]


# In[11]:


print('There are {} countries in the dataset'.format(num_countries))


# In[12]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q2: Retrieve a list of continents from the dataframe?**
# 
# *Hint: Use the `.unique` method of a series.*

# In[15]:


continents = countries_df['continent'].unique()


# In[16]:


continents


# In[17]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q3: What is the total population of all the countries listed in this dataset?**

# In[18]:


total_population = countries_df['population'].sum()


# In[19]:


print('The total population is {}.'.format(int(total_population)))


# In[20]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) What is the overall life expectancy across in the world?**
# 
# *Hint: You'll need to take a weighted average of life expectancy using populations as weights.*

# In[22]:


overall_life_exp=(countries_df['life_expectancy']*countries_df['population']).sum()/countries_df['population'].sum()


# In[23]:


overall_life_exp


# In[24]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q4: Create a dataframe containing 10 countries with the highest population.**
# 
# *Hint: Chain the `sort_values` and `head` methods.*

# In[25]:


most_populous_df = countries_df.sort_values('population',ascending=False).head(10)


# In[26]:


most_populous_df


# In[27]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q5: Add a new column in `countries_df` to record the overall GDP per country (product of population & per capita GDP).**
# 
# 

# In[28]:


countries_df['gdp'] =countries_df['population']*countries_df['gdp_per_capita']


# In[29]:


countries_df


# In[30]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.**

# In[33]:


lowest_gdp_per_capita=countries_df.query('population>100000000').sort_values(by='gdp_per_capita').head(10)


# In[34]:


lowest_gdp_per_capita


# In[35]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q6: Create a data frame that counts the number countries in each continent?**
# 
# *Hint: Use `groupby`, select the `location` column and aggregate using `count`.*

# In[36]:


country_counts_df = countries_df.groupby('continent')['location'].count()


# In[37]:


country_counts_df


# In[38]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q7: Create a data frame showing the total population of each continent.**
# 
# *Hint: Use `groupby`, select the population column and aggregate using `sum`.*

# In[39]:


continent_populations_df = countries_df.groupby('continent')['population'].sum()


# In[40]:


continent_populations_df


# In[41]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's download another CSV file containing overall Covid-19 stats for various countires, and read the data into another Pandas data frame.

# In[42]:


urlretrieve('https://gist.githubusercontent.com/aakashns/b2a968a6cfd9fbbb0ff3d6bd0f26262b/raw/b115ed1dfa17f10fc88bf966236cd4d9032f1df8/covid-countries-data.csv', 
            'covid-countries-data.csv')


# In[43]:


covid_data_df = pd.read_csv('covid-countries-data.csv')


# In[44]:


covid_data_df


# **Q8: Count the number of countries for which the `total_tests` data is missing.**
# 
# *Hint: Use the `.isna` method.*

# In[50]:


total_tests_missing = pd.isna(covid_data_df['total_tests']).count()


# In[51]:


print("The data for total tests is missing for {} countries.".format(int(total_tests_missing)))


# In[52]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's merge the two data frames, and compute some more metrics.
# 
# **Q9: Merge `countries_df` with `covid_data_df` on the `location` column.**
# 
# *Hint: Use the `.merge` method on `countries_df`.

# In[53]:


combined_df = countries_df.merge(covid_data_df,on='location',suffixes=(' countries',' covid'))


# In[54]:


combined_df


# In[55]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q10: Add columns `tests_per_million`, `cases_per_million` and `deaths_per_million` into `combined_df`.**

# In[56]:


combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']


# In[57]:


combined_df['cases_per_million'] = combined_df['total_cases']*1e6/combined_df['population']


# In[58]:


combined_df['deaths_per_million'] = combined_df['total_deaths']*1e6/combined_df['population']


# In[59]:


combined_df


# In[60]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q11: Create a dataframe with 10 countires that have highest number of tests per million people.**

# In[61]:


highest_tests_df = combined_df.sort_values('tests_per_million',ascending=False).head(10)


# In[62]:


highest_tests_df


# In[63]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q12: Create a dataframe with 10 countires that have highest number of positive cases per million people.**

# In[64]:


highest_cases_df = combined_df.sort_values('cases_per_million',ascending=False).head(10)


# In[66]:


highest_cases_df


# In[67]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q13: Create a dataframe with 10 countires that have highest number of deaths cases per million people?**

# In[68]:


highest_deaths_df = combined_df.sort_values('deaths_per_million',ascending=False).head(10)


# In[69]:


highest_deaths_df


# In[70]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".**

# In[79]:


feature_both=highest_tests_df.merge(highest_cases_df,on='location').shape[0]


# In[80]:


print('There are {} countries in both the lists of "highest number of tests per million" and "highest number of cases per million"'.format(int(feature_both)))


# In[ ]:





# In[81]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.**

# In[82]:


lowest20_gdp_per_capita=countries_df.query('population>10000000').sort_values(by='gdp_per_capita').head(20)


# In[86]:


lowest_hospital_beds_per_thousand=countries_df.query('population>10000000').sort_values(by='hospital_beds_per_thousand').head(20)


# In[89]:


counted=lowest20_gdp_per_capita.merge(lowest_hospital_beds_per_thousand,on='location').shape[0]
print('There are {}  countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population"'.format(int(counted)))


# In[90]:


import jovian


# In[91]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# ## Submission 
# 
# Congratulations on making it this far! You've reached the end of this assignment, and you just completed your first real-world data analysis problem. It's time to record one final version of your notebook for submission.
# 
# Make a submission here by filling the submission form: https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-3-pandas-practice
# 
# Also make sure to help others on the forum: https://jovian.ai/forum/t/assignment-3-pandas-practice/11225/2

# In[92]:


jovian.commit


# In[ ]:




