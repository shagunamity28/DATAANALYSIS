#!/usr/bin/env python
# coding: utf-8

# # DATA CLEANING

# In[2]:


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("Diwali Sales Data.csv" , encoding = "unicode_escape")


# In[51]:


df.head(10)


# In[52]:


df.info()


# In[53]:


df.drop(['Status', 'unnamed1'], axis =1, inplace = True)


# In[54]:


df.info()


# In[55]:


pd.isnull(df)


# In[56]:


pd.isnull(df).sum()


# In[58]:


df.shape


# In[59]:


df.dropna(inplace = True) #drop null values 


# In[60]:


df.shape


# In[66]:


#creating a test dataframe using lists
data_frame = [['shagun' , '22'], ['ginni' , '23'], ['gopi',]]
df_test = pd.DataFrame(data_frame, columns = ['name' ,'Age'])


# In[67]:


df_test


# In[68]:


df_test.dropna(inplace = True)


# In[69]:


df_test


# In[71]:


#changing the datatype of any enity
df['Amount'] = df['Amount'].astype('int')


# In[72]:


df.head


# In[73]:


df.head(10)


# In[75]:


df['Amount'].dtype


# In[77]:


df.min()


# In[78]:


df.max()


# In[80]:


df.rename(columns = {'Marital_Status':'Shaadi'})


# In[81]:


df.describe()


# In[82]:


df[['Age','Orders','Amount']].describe()


# In[83]:


df['Age'].min()


# In[84]:


df['Orders'].max()


# # EXPLORATORY DATA ANALYSIS

# In[ ]:





# # Gender

# In[11]:


df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending = True)


# In[14]:


ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
    


# In[15]:


sales_gen = df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by= 'Amount', ascending = False)


# In[21]:


sns.barplot(x= 'Gender',y= 'Amount',data= sales_gen)



# In[24]:


df.columns


# In[25]:


#age_factor = df.groupby(['Age Group'], as_index =False)['Orders'].sum().sort_values(by= 'Orders', ascending= True)


# # Age

# In[36]:


ax = sns.countplot(x= 'Age Group', data = df, hue = 'Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)


# # State

# In[50]:


sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by= 'Orders',ascending = False).head(12)
sns.set(rc= {'figure.figsize':(20,5)})
sns.barplot(x= 'State', y= 'Orders', data = sales_state)


# frorm this we can infer that most of the orders were placed by uttar pradesh and maharashtra and least from jharkhand bihar etc 

# # marital status

# In[61]:


ax = sns.countplot(x= 'Marital_Status',  data = df)
sns.set(rc={'figure.figsize':(3,5)})
for bars in ax.containers:
            ax.bar_label(bars)


# In[65]:


sales_state = df.groupby(['Marital_Status', 'Gender'],as_index = False)['Amount'].sum().sort_values(by='Amount', ascending = False)
sns.set(rc={'figure.figsize':(4,5)})
sns.barplot(x= 'Marital_Status',y= 'Amount' , data = sales_state, hue = 'Gender')


# from the above graph we can say that unmarried females have majorly contributed in the purchase 

# # Occupation

# In[6]:


sns.set(rc={'figure.figsize':(15,5)})
ax =sns.countplot(x= 'Occupation', data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# from the above graph we can infer that most of the people are in IT sector

# In[7]:


sales_state = df.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending  = False)


# In[9]:


sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='Occupation', y= 'Amount', data=sales_state)


# from the above graph we can infer that IT sector has the largest production

# # product category

# In[12]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x='Product_Category', data= df)


# from the above graph we can infer that highest selling products are from the clothing and apparel industry

# In[23]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by=['Amount'], ascending = False)
sns.barplot(x='Product_Category', y= 'Amount', data=sales_state)


# from the above graph we can infer that highest expensive products are from the food category

# # product_ID

# In[5]:


sales_state = df.groupby(['Product_ID'], as_index = False)['Orders'].sum().sort_values(by='Orders', ascending  = False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID', y= 'Orders', data = sales_state )


# from the above graph we can infer that product with product ID P00265242  were the highest selling 

# # CONCLUSION

# Unmarried women in the age group 26-35 from UP, MH , and KARNATAKA working in IT , HEALTHCARE AND AVIATION  are more likley to buy  products from  Food , clothing and electronic category

# In[ ]:




