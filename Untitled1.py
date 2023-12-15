#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt # Sample Sales Data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'Product': ['A', 'B', 'A', 'C'],
    'Sales': [100, 150, 120, 200]
}

sales_df = pd.DataFrame(data)
sales_df['Date'] = pd.to_datetime(sales_df['Date'])  # Convert 'Date' column to datetime
# Display basic information about the dataset
print(sales_df.info())

# Display basic statistics
print(sales_df.describe())# Calculate total sales per product
total_sales_per_product = sales_df.groupby('Product')['Sales'].sum().reset_index()

# Display the result
print(total_sales_per_product)
# Plotting
plt.bar(total_sales_per_product['Product'], total_sales_per_product['Sales'])
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()


# In[5]:


get_ipython().system('pip install matplotlib')


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt# Sample Sales Data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'Product': ['A', 'B', 'A', 'C'],
    'Sales': [100, 150, 120, 200]
}

sales_df = pd.DataFrame(data)
sales_df['Date'] = pd.to_datetime(sales_df['Date'])  # Convert 'Date' column to datetime
# Display basic information about the dataset
print(sales_df.info())

# Display basic statistics
print(sales_df.describe())# Calculate total sales per product
total_sales_per_product = sales_df.groupby('Product')['Sales'].sum().reset_index()

# Display the result
print(total_sales_per_product)
# Plotting
plt.bar(total_sales_per_product['Product'], total_sales_per_product['Sales'])
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()


# In[ ]:




