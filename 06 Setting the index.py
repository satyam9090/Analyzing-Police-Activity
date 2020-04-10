# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)

"""
<script.py> output:
    DatetimeIndex(['2005-01-04 12:55:00', '2005-01-23 23:15:00',
                   '2005-02-17 04:15:00', '2005-02-20 17:15:00',
                   '2005-02-24 01:20:00', '2005-03-14 10:00:00',
                   '2005-03-29 21:55:00', '2005-04-04 21:25:00',
                   '2005-07-14 11:20:00', '2005-07-14 19:55:00',
                   ...
                   '2015-12-31 13:23:00', '2015-12-31 18:59:00',
                   '2015-12-31 19:13:00', '2015-12-31 20:20:00',
                   '2015-12-31 20:50:00', '2015-12-31 21:21:00',
                   '2015-12-31 21:59:00', '2015-12-31 22:04:00',
                   '2015-12-31 22:09:00', '2015-12-31 22:47:00'],
                  dtype='datetime64[ns]', name='stop_datetime', length=86536, freq=None)
    Index(['stop_date', 'stop_time', 'driver_gender', 'driver_race',
           'violation_raw', 'violation', 'search_conducted', 'search_type',
           'stop_outcome', 'is_arrested', 'stop_duration', 'drugs_related_stop',
           'district'],
          dtype='object')
"""
