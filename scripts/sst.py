import urllib.request
import netCDF4
import numpy as np 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 
import cmocean 

# Define the spatial and temporal box of interest
year = 2022
month = 6
minlat = -24.68751
maxlat = 29.52083
minlon = -40.27082
maxlon = 13.9375
isub = 0.5

# Make "minday" and "maxday" strings by concatenating several pieces
minday = str(year)+'-'+str(month).zfill(2)+'-11T12:00:00Z'
maxday = str(year)+'-'+str(month+1).zfill(2)+'-11T12:00:00Z'

# Create the URL
base_url='https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1sstd8dayR20190SQ.nc?sstMasked%5B(2022-06-05T12:00:00Z)%5D%5B(18.02083):(-9.020833)%5D%5B(-30.02082):(1.979177)%5D&.draw=surface&.vars=longitude%7Clatitude%7CsstMasked&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff'
query='sst[('+minday+'):'+str(isub)+':('+maxday+')][(0.0):'+str(isub)+':(0.0)][('+str(minlat)+'):'+str(isub)+':('+str(maxlat)+')][('+str(minlon)+'):'+str(isub)+':('+str(maxlon)+')]'
# url = base_url+query
url = base_url

# Download data and store it in a NetCDF file
filename='satellite_data2.nc'
urllib.request.urlretrieve (url, filename)

# open NetCDF data
nc = netCDF4.Dataset(filename)
ncv = nc.variables

# Extract variables of interest from inside the NetCDF file
lon = ncv['longitude'][:]
lat = ncv['latitude'][:]
sst = ncv['sstMasked'][0,:,:]

# Make grids of lats and lons for later use to make maps
lons, lats = np.meshgrid(lon,lat)


import matplotlib.pyplot as plt

#%% Create map (LambertConformal Projection)
# Create figure
fig = plt.figure(figsize=(13,13))
# Create axis within figure (with projection)
ax = plt.axes(projection=ccrs.LambertConformal(central_longitude=(maxlon+minlon)/2, central_latitude=(maxlat+minlat)/2)) 
# Add colormap to axis (specifying projection of data) 
cs = ax.pcolormesh(lons, lats, sst, cmap=cmocean.cm.thermal, transform=ccrs.PlateCarree()) 
# Add colorbar
cbar = fig.colorbar(cs, shrink=0.6, orientation='vertical', extend='both') 
# Add legend to colorbar
cbar.set_label('Sea Surface Temperature ($^\circ$C)') 
 # Add land to axis
ax.add_feature(cfeature.NaturalEarthFeature(category='physical', scale='10m',facecolor='none', name='coastline'),
               edgecolor='#666666', facecolor='#bfbfbf')
# Add gridlines to axis
ax.gridlines()
# Add title to figure
plt.title('Satellite SST (Monthly composite for '+str(year)+'/'+str(month)+')') 


