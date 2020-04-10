# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' 
print(ri.is_arrested.dtypes)

"""
<script.py> output:
    0    False
    1    False
    2    False
    3     True
    4    False
    Name: is_arrested, dtype: object
    bool
"""
