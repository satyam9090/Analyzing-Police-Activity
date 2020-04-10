# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
annual_drug_rate.plot()

# Display the plot
plt.show()

"""
<script.py> output:
    stop_datetime
    2005-12-31    0.006501
    2006-12-31    0.007258
    2007-12-31    0.007970
    2008-12-31    0.007505
    2009-12-31    0.009889
    2010-12-31    0.010081
    2011-12-31    0.009731
    2012-12-31    0.009921
    2013-12-31    0.013094
    2014-12-31    0.013826
    2015-12-31    0.012266
    Freq: A-DEC, Name: drugs_related_stop, dtype: float64
"""
