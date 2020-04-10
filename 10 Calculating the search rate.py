# Check the data type of 'search_conducted'
print(ri.search_conducted.dtypes)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

"""
output:
    bool
    False    0.961785
    True     0.038215
    Name: search_conducted, dtype: float64
    0.0382153092354627
"""
