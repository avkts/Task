
# coding: utf-8

# In[20]:


# импортируем нужную библиотеку
import pandas as pd 


# In[21]:


# читаем файл, указываем нужный разделитель 
data_f = pd.read_csv('dataset_Facebook.csv', delimiter=";")


# In[22]:


# проверяем хорошо ли всё считалось
data_f.head()


# In[38]:


# проверим, есть ли неизвестные значений(NaN)
data_df.info()


# ## 1. Вычисление среднего для каждого числового слобца 

# In[47]:


print('Среднее значение')
print('Page total likes: ',data_df["Page total likes"].mean())
print('Category: ',data_df["Category"].mean())
print('Post Month: ',data_df["Post Month"].mean())
print('Post Weekday: ',data_df["Post Weekday"].mean())
print('Post Hour: ',data_df["Post Hour"].mean())
print('Paid: ',data_df["Paid"].dropna().mean())
print('Lifetime Post Total Reach: ',data_df["Lifetime Post Total Reach"].mean())
print('Lifetime Post Total Impressions: ',data_df["Lifetime Post Total Impressions"].mean())
print('Lifetime Engaged Users: ',data_df["Lifetime Engaged Users"].mean())
print('Lifetime Post Consumers: ',data_df["Lifetime Post Consumers"].mean())
print('Lifetime Post Consumptions: ',data_df["Lifetime Post Consumptions"].mean())
print('Lifetime Post Impressions by people who have liked your Page: ',data_df["Lifetime Post Impressions by people who have liked your Page"].mean())
print('Lifetime Post reach by people who like your Page: ',data_df["Lifetime Post reach by people who like your Page"].mean())
print('Lifetime People who have liked your Page and engaged with your post: ',data_df["Lifetime People who have liked your Page and engaged with your post"].mean())
print('comment: ',data_df["comment"].mean())
print('like: ',data_df["like"].dropna().mean())
print('share: ',data_df["share"].dropna().mean())
print('Total Interactions: ',data_df["Total Interactions"].mean())


# ## 2. Вычисление максимального/ минимального значений 

# In[48]:


print('Максимальные значения')
print('Page total likes: ',data_df["Page total likes"].max())
print('Category: ',data_df["Category"].max())
print('Post Month: ',data_df["Post Month"].max())
print('Post Weekday: ',data_df["Post Weekday"].max())
print('Post Hour: ',data_df["Post Hour"].max())
print('Paid: ',data_df["Paid"].dropna().max())
print('Lifetime Post Total Reach: ',data_df["Lifetime Post Total Reach"].max())
print('Lifetime Post Total Impressions: ',data_df["Lifetime Post Total Impressions"].max())
print('Lifetime Engaged Users: ',data_df["Lifetime Engaged Users"].max())
print('Lifetime Post Consumers: ',data_df["Lifetime Post Consumers"].max())
print('Lifetime Post Consumptions: ',data_df["Lifetime Post Consumptions"].max())
print('Lifetime Post Impressions by people who have liked your Page: ',data_df["Lifetime Post Impressions by people who have liked your Page"].max())
print('Lifetime Post reach by people who like your Page: ',data_df["Lifetime Post reach by people who like your Page"].max())
print('Lifetime People who have liked your Page and engaged with your post: ',data_df["Lifetime People who have liked your Page and engaged with your post"].max())
print('comment: ',data_df["comment"].max())
print('like: ',data_df["like"].dropna().max())
print('share: ',data_df["share"].dropna().max())
print('Total Interactions: ',data_df["Total Interactions"].max())


# In[49]:


print('Минимальные значения')
print('Page total likes: ',data_df["Page total likes"].min())
print('Category: ',data_df["Category"].min())
print('Post Month: ',data_df["Post Month"].min())
print('Post Weekday: ',data_df["Post Weekday"].min())
print('Post Hour: ',data_df["Post Hour"].min())
print('Paid: ',data_df["Paid"].dropna().min())
print('Lifetime Post Total Reach: ',data_df["Lifetime Post Total Reach"].min())
print('Lifetime Post Total Impressions: ',data_df["Lifetime Post Total Impressions"].min())
print('Lifetime Engaged Users: ',data_df["Lifetime Engaged Users"].min())
print('Lifetime Post Consumers: ',data_df["Lifetime Post Consumers"].min())
print('Lifetime Post Consumptions: ',data_df["Lifetime Post Consumptions"].min())
print('Lifetime Post Impressions by people who have liked your Page: ',data_df["Lifetime Post Impressions by people who have liked your Page"].min())
print('Lifetime Post reach by people who like your Page: ',data_df["Lifetime Post reach by people who like your Page"].min())
print('Lifetime People who have liked your Page and engaged with your post: ',data_df["Lifetime People who have liked your Page and engaged with your post"].min())
print('comment: ',data_df["comment"].min())
print('like: ',data_df["like"].dropna().min())
print('share: ',data_df["share"].dropna().min())
print('Total Interactions: ',data_df["Total Interactions"].min())


# ## 3. Вычисление медиан 

# In[50]:


print('Значения медиан')
print('Page total likes: ',data_df["Page total likes"].median())
print('Category: ',data_df["Category"].median())
print('Post Month: ',data_df["Post Month"].median())
print('Post Weekday: ',data_df["Post Weekday"].median())
print('Post Hour: ',data_df["Post Hour"].median())
print('Paid: ',data_df["Paid"].dropna().median())
print('Lifetime Post Total Reach: ',data_df["Lifetime Post Total Reach"].median())
print('Lifetime Post Total Impressions: ',data_df["Lifetime Post Total Impressions"].median())
print('Lifetime Engaged Users: ',data_df["Lifetime Engaged Users"].median())
print('Lifetime Post Consumers: ',data_df["Lifetime Post Consumers"].median())
print('Lifetime Post Consumptions: ',data_df["Lifetime Post Consumptions"].median())
print('Lifetime Post Impressions by people who have liked your Page: ',data_df["Lifetime Post Impressions by people who have liked your Page"].median())
print('Lifetime Post reach by people who like your Page: ',data_df["Lifetime Post reach by people who like your Page"].median())
print('Lifetime People who have liked your Page and engaged with your post: ',data_df["Lifetime People who have liked your Page and engaged with your post"].min())
print('comment: ',data_df["comment"].median())
print('like: ',data_df["like"].dropna().median())
print('share: ',data_df["share"].dropna().median())
print('Total Interactions: ',data_df["Total Interactions"].median())


# ## 4. Вычисление моды числовых значений 

# In[51]:


print('Значения моды')
print('Type: ',data_df["Type"].mode())
print('Page total likes: ',data_df["Page total likes"].mode())
print('Category: ',data_df["Category"].mode())
print('Post Month: ',data_df["Post Month"].mode())
print('Post Weekday: ',data_df["Post Weekday"].mode())
print('Post Hour: ',data_df["Post Hour"].mode())
print('Paid: ',data_df["Paid"].dropna().mode())
print('Lifetime Post Total Reach: ',data_df["Lifetime Post Total Reach"].mode())
print('Lifetime Post Total Impressions: ',data_df["Lifetime Post Total Impressions"].mode())
print('Lifetime Engaged Users: ',data_df["Lifetime Engaged Users"].mode())
print('Lifetime Post Consumers: ',data_df["Lifetime Post Consumers"].mode())
print('Lifetime Post Consumptions: ',data_df["Lifetime Post Consumptions"].mode())
print('Lifetime Post Impressions by people who have liked your Page: ',data_df["Lifetime Post Impressions by people who have liked your Page"].mode())
print('Lifetime Post reach by people who like your Page: ',data_df["Lifetime Post reach by people who like your Page"].mode())
print('Lifetime People who have liked your Page and engaged with your post: ',data_df["Lifetime People who have liked your Page and engaged with your post"].mode())
print('comment: ',data_df["comment"].mode())
print('like: ',data_df["like"].dropna().mode())
print('share: ',data_df["share"].dropna().mode())
print('Total Interactions: ',data_df["Total Interactions"].mode())


# ## 5. Поиск самого популярного объекта в выборке

# In[55]:


data_df[(data_df["Total Interactions"]==data_df["Total Interactions"].max())]


# Данный объект является наиболее популярным, так как с ним было совершено наибольшее кольчество взаимодействий (лайков и репостов)
