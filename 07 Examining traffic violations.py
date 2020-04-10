# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))

"""
<script.py> output:
    Speeding               48423
    Moving violation       16224
    Equipment              10921
    Other                   4409
    Registration/plates     3703
    Seat belt               2856
    Name: violation, dtype: int64
    Speeding               0.559571
    Moving violation       0.187483
    Equipment              0.126202
    Other                  0.050950
    Registration/plates    0.042791
    Seat belt              0.033004
    Name: violation, dtype: float64
"""
