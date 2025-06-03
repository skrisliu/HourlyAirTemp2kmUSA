# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 19:45:21 2025

@author: skrisliu

visualizing the generated near-surface air temperature data
on specific day, all hours
"""

import os
import numpy as np
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import netCDF4 as nc

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


YEAR = '2018'   #  YEAR
MODE = 'avg'    #  which data to load: avg, low, upp   
DOY = '042'     #  Day Of Year (DOY)

dfile = 'goes16_abi_conus_lat_lon.nc' # the latlon file

#%% load latlon, predicted air temp
latlon = nc.Dataset(dfile)

date = datetime(int(YEAR), 1, 1) + timedelta(days=int(DOY) - 1)
yyyymmdd = date.strftime('%Y%m%d')

def convert_timezones_fixed(yyyymmdd: str, hh: str):
    """
    Convert UTC date and hour to:
    - UTC
    - Fixed Eastern Time (UTC-5)
    - Fixed Pacific Time (UTC-8)

    Parameters:
        yyyymmdd (str): Date in 'YYYYMMDD' format
        hh (str): Hour in 'HH' format (00–23) in UTC

    Returns:
        dict: Dictionary with times in UTC, ET (UTC-5), and PT (UTC-8)
    """
    # Parse input UTC datetime
    dt_utc = datetime.strptime(yyyymmdd + hh.zfill(2), "%Y%m%d%H")
    dt_utc = dt_utc.replace(tzinfo=timezone.utc)

    # Define fixed timezones
    utc_minus_5 = timezone(timedelta(hours=-5))  # Eastern
    utc_minus_8 = timezone(timedelta(hours=-8))  # Pacific

    # Convert
    dt_et_fixed = dt_utc.astimezone(utc_minus_5)
    dt_pt_fixed = dt_utc.astimezone(utc_minus_8)

    # Format
    fmt = "%Y-%m-%d %H:%M"
    return {
        "UTC": dt_utc.strftime(fmt),
        "Fixed_ET": dt_et_fixed.strftime(fmt),
        "Fixed_PT": dt_pt_fixed.strftime(fmt),
    }


#%% load predicted air temp, 24 hours of that day, transform to K then to °C
im0file = 'y' + YEAR + MODE + '/doy' + DOY + '/' + YEAR + DOY 

ims = {}
for h in range(24):
    hh = format(h,'02d')
    imfile = im0file + hh + '.nc'
    
    fp = nc.Dataset(imfile)
    im = fp['at'][:,:].data
    mask = fp['at'][:,:].mask
    
    im = im.astype(np.float32)
    im = im*0.00341802+149 -273.15
    im[mask] = np.nan
    ims[hh] = im
   

#%% set up before plot images

# make a fig folder to place the hourly image
os.makedirs('fig', exist_ok=True)

# define projection
proj = ccrs.AlbersEqualArea(central_longitude=-96, central_latitude=37.5, standard_parallels=(29.5, 45.5))

# set vmin,vmax to be 1% and 99% of all data within the same day 
data_valids = []
for hh in ims.keys():
    im = ims[hh]
    data_valid = im[~np.isnan(im)]
    data_valids.append(data_valid)

data_valids = np.concatenate(data_valids)
vminn = np.percentile(data_valids,1)
vmaxx = np.percentile(data_valids,99)
vminmax = [vminn,vmaxx]

   
#%% plot data, and output to subdir
for hh in ims.keys():
    timestamp = convert_timezones_fixed(yyyymmdd,hh)
    
    
    fig, ax = plt.subplots(figsize=(7.9, 5), subplot_kw={'projection': proj}, dpi=300)
    
    # Add coastlines and states
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.3)
    ax.add_feature(cfeature.STATES, linewidth=0.2, linestyle=":", edgecolor="gray")
    
    img = ax.pcolormesh(latlon['longitude'], latlon['latitude'], ims[hh], 
                        cmap="coolwarm", shading='auto', transform=ccrs.PlateCarree(),
                        vmin=vminmax[0], vmax=vminmax[1])
    
    ax.set_extent([-119.6, -72.8, 25, 50], crs=ccrs.PlateCarree())
    
    
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    
    # plt.gca().xaxis.set_ticks([])
    # plt.gca().yaxis.set_ticks([])
    
    cax = ax.inset_axes([0.515, 0.0545, 0.25, 0.02])  # [left, bottom, width, height] in axes fraction
    cb = fig.colorbar(img, cax=cax, orientation='horizontal', extend='both')
    cb.ax.tick_params(labelsize=5)  # Adjust colorbar tick size
    ax = plt.gca()
    ax.text(0.519, 0.083, 'Near-Surface Air Temperature (°C)', fontsize=8, 
            transform=ax.transAxes, ha='left', va='bottom')
    sss = 'UTC\n' + timestamp['UTC'] + '\n\n' + 'UTC-5 New York\n' + timestamp['Fixed_ET']
    ax.text(0.01, 0.01, sss, fontsize=7, 
            transform=ax.transAxes, ha='left', va='bottom')
    
    plt.tight_layout(pad=0.1)
    plt.savefig('fig/at'+YEAR+DOY+hh+'.jpg')
    plt.show()

























    
