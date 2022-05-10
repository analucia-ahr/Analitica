#!/usr/bin/env python
# coding: utf-8

# 1. Importa pandas. 
# 2. Lee el archivo .csv usando la función read_csv. 
# 3. Observa las primeras líneas usando la función head.

# In[23]:


import pandas as pd 
data = pd.read_csv("avocado.csv")
data.head()
#join = pd.concat([])
#join.shape


# 4. Obtén diferentes combinaciones de columnas y datos.

# In[28]:


import pandas as pd
df = pd.read_csv('avocado.csv')
df.head()
df.iloc[1:, 0:5]


# 5. Revisa los datos obtenidos por la función  describe.

# In[29]:


df.describe()


# 6. ¿Cuántos objetos hay? 18249
# 6. ¿Cuál es el valor de la variable 2 del objeto 15? 1.28
# 6. ¿Cuál es el mínimo y máximo de la variable 3? max = 6.250565e+07, min = 8.456000e+01

# In[30]:


df.count()


# In[33]:


df.loc[15, 'AveragePrice']

