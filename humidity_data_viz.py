#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


db_name="IoT_DataBase.db"
conn=sqlite3.connect(db_name)
curs = conn.cursor()


# In[3]:


sql='''SELECT * FROM Humidity_Data'''
curs.execute(sql)
data=curs.fetchall()


# In[4]:


def data_processing(data):
    processed_data = []
    sum_temperature_values_per_minute = 0
    current_minute = data[0][2].split(":")[1]
    counter = 0
    for i in range(len(data)):
        if data[i][2].split(":")[1] == current_minute:
            sum_temperature_values_per_minute += data[i][3]
            counter += 1
            #print(current_minute)
            #print(sum_temperature_values_per_minute)
            #print(counter)
        else:
            temperature_avg = sum_temperature_values_per_minute/counter
            processed_data.append((data[i-1][2].split(":")[0]+":"+data[i-1][2].split(":")[1], temperature_avg))
            current_minute = data[i][2].split(":")[1]
            #print(current_minute)
            sum_temperature_values_per_minute = 0
            counter = 0
            #print(sum_temperature_values_per_minute)
            #print(counter)
    temperature_avg = sum_temperature_values_per_minute/counter
    processed_data.append((data[i-1][2].split(":")[0]+":"+data[i-1][2].split(":")[1], temperature_avg))
    return processed_data

# In[5]:


processed_data = data_processing(data)
date_time_per_minute=[]
humidity_val=[]
humidityDescription=[]
for i in range(len(processed_data)):
    date_time_per_minute.append(processed_data[i][0])
    humidity_val.append(processed_data[i][1])
    #humidityDescription.append(data[i][-1])

for i in range(len(data)):
    humidityDescription.append(data[i][-1])

# In[6]:


time = np.array(date_time_per_minute)
humidity = np.array(humidity_val)

fig, ax = plt.subplots()
ax.plot(time, humidity)

ax.set(xlabel='date time per minute', ylabel='Humditiy',
       title='Temperature °C')
ax.grid()

fig.savefig("temperature_viz.png")
plt.show()

# In[7]:


prcnt=[]
prcnt.append(humidityDescription.count('LOW')*len(humidity_val)/100)
prcnt.append(humidityDescription.count('MEDUIM')*len(humidity_val)/100)
prcnt.append(humidityDescription.count('HIGH')*len(humidity_val)/100)


# In[8]:


labels = ['low','medium', 'high']
sizes = prcnt
explode = (0, 0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
