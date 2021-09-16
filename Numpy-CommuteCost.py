# -*- coding: utf-8 -*-
"""
Numpy Assignment
The purpose of this program is to utilize numpy and pandas to figure out
the date in which the most money was spent on the commute.

@author: aylat
"""

import numpy as np
import pandas as pd

# Using pandas to import excel data, specifying sheet name & column index
commute = pd.read_excel("commute.xlsx", sheet_name = "Sales",
                        index_col= "Date")

# Replacing all the "Yes" and "No" to 1's and 0's using pandas
# Pass the values into a list if more than one needs to be replaced
# This will only create a copy of the replaced data, but will not replace 
# the data in the original dataframe
commute.replace(["Yes", "No"],[1,0])

# Adding the inplace argument will replace the data in the original dataframe
commute.replace(["Yes", "No"],[1,0], inplace = True)

# Passing the data into a 2-dimensional array (matrix)
np_commute_array = np.array(commute)

# Passing commute prices into a separate array (vector)
np_prices_array = np.array([8,3,0.5,12])

# Using the dot product function to multiply the vector by the matrix 
# to figure out how much was spent each day on the commute
# When multiplying a vector and a matrix, the number of columns in the
# matrix should be equal to the number of rows in the vector
# In this case there are four columns in the matrix, and four rows
# in the vector

daily_commute_cost = np_commute_array.dot(np_prices_array)

# Using the sum function to calculate the total price incurred on 
# commuting; total cost = $4,683.0
daily_commute_cost.sum()

# Using the argmax function to determine when the most money was spent
# This function will return the index of the value, in this case, 145
# Referencing that index in our original dataframe, the corresponding value
# (money spent) is $50.5
daily_commute_cost.argmax()

# Finding the date in which the most money was spent on commute, and 
# formatting the date (2020-10-24)
commute.index[daily_commute_cost.argmax()].strftime("%Y-%m-%d")



