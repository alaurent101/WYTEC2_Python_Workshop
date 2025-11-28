# Import Pandas module
import pandas as pd

# Read data from file
glider_data = pd.read_csv('glider_data.csv',sep=',')

# Quality Control: Filter out data above 40oC and below -8oC
glider_data = glider_data[(glider_data.sci_water_temp < 40) & (glider_data.sci_water_temp > -8)]

# Quality Control: Filter out data too close to the surface
glider_data = glider_data[glider_data.depth > 3]

# Make a scatter plot
glider_data.plot.scatter('unixtime',
                         'depth',
                         c='sci_water_temp',
                         marker='o',
                         edgecolor='none',
                         cmap='viridis',
                         ylim=[glider_data['depth'].max(),0],
                         figsize=[19,9])