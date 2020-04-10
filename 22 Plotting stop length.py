# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()

"""
<script.py> output:
    violation_raw
    APB                                 17.967033
    Call for Service                    22.124371
    Equipment/Inspection Violation      11.445655
    Motorist Assist/Courtesy            17.741463
    Other Traffic Violation             13.844490
    Registration Violation              13.736970
    Seatbelt Violation                   9.662815
    Special Detail/Directed Patrol      15.123632
    Speeding                            10.581562
    Suspicious Person                   14.910714
    Violation of City/Town Ordinance    13.254144
    Warrant                             24.055556
    Name: stop_minutes, dtype: float64

"""
