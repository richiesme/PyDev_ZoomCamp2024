#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd


# In[67]:


pd.__version__


# In[68]:


df = pd.read_csv("yellow_tripdata_2021-01.csv", nrows = 100)


# In[69]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[70]:


from sqlalchemy import create_engine


# In[71]:


engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")


# In[72]:


engine.connect()


# In[73]:


print(pd.io.sql.get_schema(df, name="yellow_tripdata_2021-01", con=engine))


# In[74]:


df_iter = pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=100000)


# In[75]:


df = next(df_iter)


# In[76]:


len(df)


# In[77]:


df_iter


# In[78]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[79]:


df


# In[80]:


df.head(n=0).to_sql(name="yellow_tripdata_2021-01", con=engine, if_exists="replace")


# In[81]:


get_ipython().run_line_magic('time', 'df.to_sql(name="yellow_tripdata_2021-01", con=engine, if_exists="append")')


# In[82]:


from time import time


# In[83]:


while True:
    t_start = time()
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name="yellow_tripdata_2021-01", con=engine, if_exists="append")

    t_end = time()
    print("inserted another chunk..., took %.3f seconds" % (t_end - t_start))
    


# In[ ]:





# In[ ]:




