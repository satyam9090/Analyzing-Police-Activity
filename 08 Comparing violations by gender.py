# Create a DataFrame of female drivers
female = ri[ri.driver_gender == 'F']

# Create a DataFrame of male drivers
male = ri[ri.driver_gender == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize=True))

"""
output:
    Speeding               0.658114
    Moving violation       0.138218
    Equipment              0.105199
    Registration/plates    0.044418
    Other                  0.029738
    Seat belt              0.024312
    Name: violation, dtype: float64
    Speeding               0.522243
    Moving violation       0.206144
    Equipment              0.134158
    Other                  0.058985
    Registration/plates    0.042175
    Seat belt              0.036296
    Name: violation, dtype: float64
"""
