# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri['stop_time'], sep = ' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

"""
<script.py> output:
    stop_date                     object
    stop_time                     object
    driver_gender                 object
    driver_race                   object
    violation_raw                 object
    violation                     object
    search_conducted                bool
    search_type                   object
    stop_outcome                  object
    is_arrested                     bool
    stop_duration                 object
    drugs_related_stop              bool
    district                      object
    stop_datetime         datetime64[ns]
    dtype: object

<script.py> output:
    stop_date                     object
    stop_time                     object
    driver_gender                 object
    driver_race                   object
    violation_raw                 object
    violation                     object
    search_conducted                bool
    search_type                   object
    stop_outcome                  object
    is_arrested                     bool
    stop_duration                 object
    drugs_related_stop              bool
    district                      object
    stop_datetime         datetime64[ns]
    dtype: object
"""
