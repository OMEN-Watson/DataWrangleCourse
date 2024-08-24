'''
This module implements the missing values table in Rattle, using Python

@Author: Charini Nanayakkara
'''

import sys
import pandas as pd

file_name = sys.argv[1]
pattern_count_dict = {} # Dictionary to store patterns of row values (as in 
                        # rattle missing file table). The key is a pattern. The
                        # value is a tuple where the first value indicates the
                        # number of times a pattern occurs and the second value
                        # tells the number of variables with missing values per
                        # each pattern. 
table_value_list = [] # Table to contain missing value data as list of lists.
                      # The first value in the sub list is the missing value count 
                      # per row. Second value is a tuple containing the pattern
                      # and the missing variables per pattern.

df = pd.read_csv(file_name)

null_table = df.isnull()
tot_missing_vals_per_var = null_table.sum(axis=0) # Total missing values per variable
total_missing_vals = tot_missing_vals_per_var.sum() # Total missing values

for index, row in null_table.iterrows():
  count,var_no = pattern_count_dict.get(tuple(row),(0,0))
  count += 1
  var_no = sum(row) # True = 1 and False = 0. Therefore, null values are counted
  pattern_count_dict[tuple(row)] = (count,var_no)
  

for key,value in pattern_count_dict.items():
  table_value_list.append([value[0], [int(not item) for item in key] + [value[1]]])
  
table_value_list.sort(reverse=True)

table_value_list.append(['',tot_missing_vals_per_var.tolist() + \
                         [total_missing_vals]])


data = [item[1] for item in table_value_list] # Data to write to table
columns_list = tot_missing_vals_per_var.index.tolist() + ['']
index_list = [item[0] for item in table_value_list]
# Create new pandas DataFrame 
new_df = pd.DataFrame(data, columns = columns_list, index = index_list) 
print('---------------')
print (new_df)
