# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

"""
output:
      state   stop_date stop_time  county_name driver_gender driver_race  \
    0    RI  2005-01-04     12:55          NaN             M       White   
    1    RI  2005-01-23     23:15          NaN             M       White   
    2    RI  2005-02-17     04:15          NaN             M       White   
    3    RI  2005-02-20     17:15          NaN             M       White   
    4    RI  2005-02-24     01:20          NaN             F       White   
    
                        violation_raw  violation  search_conducted search_type  \
    0  Equipment/Inspection Violation  Equipment             False         NaN   
    1                        Speeding   Speeding             False         NaN   
    2                        Speeding   Speeding             False         NaN   
    3                Call for Service      Other             False         NaN   
    4                        Speeding   Speeding             False         NaN   
    
        stop_outcome is_arrested stop_duration  drugs_related_stop district  
    0       Citation       False      0-15 Min               False  Zone X4  
    1       Citation       False      0-15 Min               False  Zone K3  
    2       Citation       False      0-15 Min               False  Zone X4  
    3  Arrest Driver        True     16-30 Min               False  Zone X1  
    4       Citation       False      0-15 Min               False  Zone X3  
    state                     0
    stop_date                 0
    stop_time                 0
    county_name           91741
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
    """
