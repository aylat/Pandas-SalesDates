# -*- coding: utf-8 -*-
"""
Pandas Assignment
The purpose of this program is to break one large data set into smaller data sets
based on order date

@author: aylat
"""

import pandas as pd

# Using pandas to import excel data, specifying the column index
# Note: Since there is only one worksheet in this data set, there is no need
# to specify the sheet name in the arguments
sales_data = pd.read_excel("sales_data.xlsx", index_col = "Row ID")

# Adding a new column to the dataframe to reformat the Order Date from 
# Date-Time format to Month-Year format
sales_data["Order Date: Month-Year"] = sales_data["Order Date"].dt.strftime("%m-%Y")

# Using a .grouby function to group the data by the new column (Order Date: Month-Year)
# and storing it in a new dataframe
groupby = sales_data.groupby("Order Date: Month-Year")

# Extracting a certain date (month-year) from the new groupby dataframe using the .get_group function
# This will also return a value for how many rows are included in this 
# category of data (316)
groupby.get_group("12-2015")

# Using a for loop to store all of the partial dataframes in a list
# gb.groups is a dictionary, with groups as the key (month-year), and the 
# corresponding values are the indices that pertain to the particular group name
# Separating the entire dataframe into individual dataframes that contain
# all of the information that corresponds to a specific month-year date
ls =[]
for df in groupby.groups:
    ls.append(groupby.get_group(df))
    
# Using a for loop to export the new dataframe back into excel, using
# Order Date: Month-Year as the file name
# The .iloc function allows for only the first element of the specified column
for df in ls:
    file_name = df["Order Date: Month-Year"].iloc[0]
    df.to_excel("{}.xlsx".format(file_name), index=False) 







