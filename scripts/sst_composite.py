import urllib.request
import netCDF4
import numpy as np 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 
import cmocean 


# Create the URL
url='https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST41.htmlTable?analysed_sst[(2002-06-01T09:00:00Z)][(-89.99):1000:(89.99)][(-179.99):1000:(180.0)]'

# Download data and store it in a NetCDF file
filename='satellite_data_tempfile1.nc'
urllib.request.urlretrieve (url, filename)

# open NetCDF data
nc = netCDF4.Dataset('satellite_data_tempfile1.nc')
ncv = nc.variables

# Extract variables of interest from inside the NetCDF file
lon = ncv['longitude'][:]
lat = ncv['latitude'][:]
sst = ncv['sstMasked'][0,0,:,:]

# Make grids of lats and lons for later use to make maps
lons, lats = np.meshgrid(lon,lat)


#%% Create map (PlateCarree Projection) 
fig = plt.figure(figsize=(13,13)) # Create figure
ax = plt.axes(projection=ccrs.PlateCarree()) # Create axis within figure (with projection)
ax.pcolormesh(lons, lats, sst, transform=ccrs.PlateCarree()) # Add colormap to axis (specifying projection of data) 
ax.coastlines(resolution='10m') # Add coastline to axis



#%% Create map (LambertConformal Projection)
# Create figure
fig = plt.figure(figsize=(13,13))
# Create axis within figure (with projection)
ax = plt.axes(projection=ccrs.LambertConformal(central_longitude=(lon.max()+lon.min())/2, central_latitude=(lat.max()+lat.min())/2)) 
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
plt.title('Satellite SST (3-day composite)') 
