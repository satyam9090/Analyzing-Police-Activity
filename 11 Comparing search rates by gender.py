# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())

# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())

# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())

"""
<script.py> output:
    0.019180617481282074

<script.py> output:
    0.04542557598546892

<script.py> output:
    driver_gender
    F    0.019181
    M    0.045426
    Name: search_conducted, dtype: float64
"""
