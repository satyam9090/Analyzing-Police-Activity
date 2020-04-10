# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.stop_outcome.value_counts(normalize=True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.stop_outcome.value_counts(normalize=True))


"""
output:
    Citation            0.952192
    Warning             0.040074
    Arrest Driver       0.005752
    N/D                 0.000959
    Arrest Passenger    0.000639
    No Action           0.000383
    Name: stop_outcome, dtype: float64
    Citation            0.944595
    Warning             0.036184
    Arrest Driver       0.015895
    Arrest Passenger    0.001281
    No Action           0.001068
    N/D                 0.000976
    Name: stop_outcome, dtype: float64
"""
