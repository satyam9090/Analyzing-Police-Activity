# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

"""
<script.py> output:
    stop_date             91741
    stop_time             91741
    driver_gender         91741
    driver_race           91741
    violation_raw         91741
    violation             91741
    search_conducted      91741
    search_type           91741
    stop_outcome          91741
    is_arrested           91741
    stop_duration         91741
    drugs_related_stop    91741
    district              91741
    dtype: int64
    stop_date                 0
    stop_time                 0
    driver_gender             0
    driver_race               0
    violation_raw             0
    violation                 0
    search_conducted          0
    search_type           83229
    stop_outcome              0
    is_arrested               0
    stop_duration             0
    drugs_related_stop        0
    district                  0
    dtype: int64
    (86536, 13)

<script.py> output:
    stop_date                 0
    stop_time                 0
    driver_gender          5205
    driver_race            5202
    violation_raw          5202
    violation              5202
    search_conducted          0
    search_type           88434
    stop_outcome           5202
    is_arrested            5202
    stop_duration          5202
    drugs_related_stop        0
    district                  0
    dtype: int64
    stop_date                 0
    stop_time                 0
    driver_gender             0
    driver_race               0
    violation_raw             0
    violation                 0
    search_conducted          0
    search_type           83229
    stop_outcome              0
    is_arrested               0
    stop_duration             0
    drugs_related_stop        0
    district                  0
    dtype: int64
    (86536, 13)
"""
