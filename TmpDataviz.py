#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


db_name="IotDatabase.db"
conn=sqlite3.connect(db_name)
curs = conn.cursor()


# In[3]:


sql='''SELECT * FROM Temperature_Data '''
curs.execute(sql)
data=curs.fetchall()


# In[4]:


index=[]
tmpValue=[]
tmpDescription=[]
for i in range(len(data)):
    index.append(data[i][0])
    tmpValue.append(data[i][3])
    tmpDescription.append(data[i][-1])


# In[9]:


i = np.array(index)
temp = np.array(tmpValue)

fig, ax = plt.subplots()
ax.plot(i, temp)

ax.set(xlabel='Temperature', ylabel='index',
       title='Temperature')
ax.grid()

fig.savefig("test.png")
plt.show()


# In[6]:


prcnt=[]
prcnt.append(tmpDescription.count('very cold')*len(tmpDescription)/100)
prcnt.append(tmpDescription.count('cold')*len(tmpDescription)/100)
prcnt.append(tmpDescription.count('normal')*len(tmpDescription)/100)
prcnt.append(tmpDescription.count('hot')*len(tmpDescription)/100)
prcnt.append(tmpDescription.count('very hot')*len(tmpDescription)/100)


# In[7]:


labels = ['very cold','cold', 'normal', 'hot', 'very hot']
sizes = prcnt
explode = (0, 0.1, 0, 0,0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()

