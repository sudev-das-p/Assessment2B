#!/usr/bin/env python
# coding: utf-8

# ###### Assessment

# ###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

# ###### import necessary libraries

# In[1]:


import pandas as pd


# ###### merge those two csv files (after getting as dataframes, get them as a single dataframe)

# In[2]:


df1 = pd.read_csv('college_1.csv')
df2 = pd.read_csv('college_2.csv')
df = pd.concat([df1,df2],axis = 0)
df


# ###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo) 
# 

# ###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
# 

# ###### if  10000<codekata score<15000   (Reached_expectations.csv)
# 
# 

# ###### if  7000<codekata score<10000   (Needs_Improvement.csv)
# 

# ###### if  codekate score < 7000        (Unsatisfactory.csv)

# In[4]:


exceeded = df[df['CodeKata Score'] > 15000]
exceeded.to_csv('Exceeded expectations.csv', index=False)

reached = df[(df['CodeKata Score']>10000) & (df['CodeKata Score']<15000)]
reached.to_csv('Reached_expectations.csv',index = False)

reached = df[(df['CodeKata Score']<10000) ]
reached.to_csv('Needs_improvement.csv',index = False)

reached = df[(df['CodeKata Score']<7000) ]
reached.to_csv('Unsatisfactory.csv',index = False)


# In[ ]:





# ###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

# In[5]:


print(df['Previous Geekions'].mean())
print(df['CodeKata Score'].mean())


# ###### No of students participated 

# In[6]:


df['Name'].count()


# ###### #Average completion of python course or my_sql or python english or computational thinking

# In[7]:


print(df['python'].mean())
print(df['mysql'].mean())
print(df['python_en'].mean())
print(df['computational_thinking'].mean())


# ###### rising star of the week (top 3 candidate who performed well in that particular week)

# 

# In[8]:


df['CodeKata Score'].sort_values(ascending = False).head(3)


# ###### Shining stars of the week (top 3 candidates who has highest geekions)

# In[9]:


df['Previous Geekions'].sort_values(ascending = False).head(3)


# ###### Department wise codekata performence (pie chart)

# In[10]:


import matplotlib.pyplot as plt
plt.pie(df['Department'].value_counts(),labels = ['Computer Science and Engineering','Electronics and Communication Engineering','Electronics and Electrical Engineering'])


# ###### Department wise toppers (horizantal bar graph or any visual representations of your choice)

# In[ ]:





# In[12]:


cse_df = df[df["Department"] == "Computer Science and Engineering"]
cse_df = cse_df.sort_values(by="python_en", ascending=False)
plt.barh(cse_df["Name"], cse_df["python_en"])
plt.xlabel("Python Score")
plt.ylabel("Name")
plt.title("Department Wise Toppers (CSE)")
plt.show()


# In[103]:


ece_df = df[df["Department"] == "Electronics and Communication Engineering"]
ece_df = ece_df.sort_values(by="python_en", ascending=False)
plt.barh(ece_df["Name"], ece_df["python_en"])
plt.xlabel("Python Score")
plt.ylabel("Name")
plt.title("Department Wise Toppers (ECE)")
plt.show()


# In[104]:


eee_df = df[df["Department"] == "Electronics and Electrical Engineering"]
eee_df = eee_df.sort_values(by="python_en", ascending=False)
plt.barh(eee_df["Name"], eee_df["python_en"])
plt.xlabel("Python Score")
plt.ylabel("Name")
plt.title("Department Wise Toppers (EEE)")
plt.show()

