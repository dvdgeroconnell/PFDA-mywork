# assignment_6_Weather.py
# 17/11 attempt

# Purpose of Program:
#   A program to...

# Assumptions:
#   List any assumptions here...

# Author: David O'Connell

# References:
#   PFDA Topic 56 lecture videos (Andrew Beatty) - https://vlegalwaymayo.atu.ie/course/view.php?id=10462
#   https://www.w3schools.com/python/numpy/default.asp for NumPy
#   https://www.geeksforgeeks.org/rotate-axis-tick-labels-in-seaborn-and-matplotlib/ for rotating labels
#
# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import sys, math

# Read the file, drop the first 23 rows as they are header data, then also drop the first row
# of data as there are nearly 4 months of data missing after it
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv", skiprows=23,low_memory=False)
df = df.drop(0)

df['datetime'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['datetime2'] = df['datetime']
df = df.set_index('datetime2')
#df['yr'] = pd.DatetimeIndex(df['datetime']).year
print(df.head(3))
print(df.tail(3))

mean_daily_temp = df["temp"].resample("d").mean()
mean_monthly_temp = df["temp"].resample("m").mean()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16,8), sharex='col')
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16,8))

ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]
ax1.plot(df["datetime"], df["temp"])
ax1.plot(mean_daily_temp)
ax1.plot(mean_monthly_temp)
ax1.set_title('Full Dataset', fontsize=14)

count_nan = df['wdsp'].isnull().sum()
print("Null count: ",count_nan)

count_blank = 0
inx = 0
print("row 0 wdsp", df.iloc[0,df.columns.get_loc("wdsp")])

#df['wdsp'] = df['wdsp'].replace(' ',pd.isnull)
#df['wdsp'] = df['wdsp'].replace(' ',pd.isna)
df['wdsp'] = df['wdsp'].replace(' ',-999)

#for x in df['wdsp']:
#    if x == ' ':
#        print("position ", inx, "is blank")
#        count_blank += 1
#        #print ("value: ",math.isnan(int(df[inx,df.columns.get_iloc("wdsp")])))
#        df.iloc[inx,df.columns.get_loc("wdsp")] = ''
#    inx += 1
#print("There are ", count_blank, "white spaces")

#print("Blank rows1:\n",df[df['wdsp'].str.contains(' ')])
#print("Blank rows2:\n",df[df['wdsp'].str.contains('')])

# Windspeed is an object, need to change to int for the plot to work
df['wdsp2'] = df['wdsp']
df['wdsp2'] = df['wdsp2'].astype(int)
print("before\n",df.dtypes)

print("position 1795:\n",df.iloc[1795])
#df['wdsp2'] = df['wdsp2'].replace(-999,pd.NA)
df['wdsp2'] = df['wdsp2'].replace(-999,np.nan)

print("after\n",df.dtypes)

inx = 0
for x in df['wdsp2']:
    if x > 45:
        print("temp over 45 ", inx)
        print(df.iloc[inx])
    inx += 1

# Set dummy value for now
#df["wdsp2"] = 1

#df[df['wdsp'].str.contains(' ')] = ''

# Number of samples in the moving window average (1 day / 24 hours)
moving_window_size = 24

# rolling windspeed over a 24 hour moving window
rolling_windspeed = df['wdsp2'].rolling(moving_window_size).mean()
daily_max_windspeed = df["wdsp2"].resample("d").max()
ax3.plot(df['datetime'], df['wdsp2'])
ax3.plot(rolling_windspeed)
ax3.plot(daily_max_windspeed)

# Create a set of plots for 2024 so we can see what 1 year looks like
dateFrom = "2024-01-01 01:00:00"
dateTo = "2024-12-31 23:00:00"
df_latest = df.loc[dateFrom:dateTo]
mean_daily_temp_latest = df_latest["temp"].resample("d").mean()
mean_monthly_temp_latest = df_latest["temp"].resample("m").mean()

#df_latest["wdsp2"] = df_latest["wdsp"].astype(int)
#windspeed = df_latest['wdsp2'].to_numpy()
#np.set_printoptions(threshold=sys.maxsize)
#print(windspeed)

ax2.plot(df_latest["datetime"], df_latest["temp"])
ax2.plot(mean_daily_temp_latest)
ax2.plot(mean_monthly_temp_latest)
ax2.set_title('Latest Year', fontsize=14)

# rolling windspeed over a 24 hour moving window
rolling_windspeed_latest = df_latest['wdsp2'].rolling(moving_window_size).mean()
daily_max_windspeed_latest = df_latest["wdsp2"].resample("d").max()
ax4.plot(df_latest["datetime"],df_latest["wdsp2"])
ax4.plot(rolling_windspeed_latest)
ax4.plot(daily_max_windspeed_latest)

count_nan = df_latest['wdsp2'].isnull().sum()
print("Null count: ",count_nan)

xlabels = ["Hourly Temp","Daily Avg","Monthly Avg"]
wdlabels = ["Windspeed","Rolling Windspeed","Max Windspeed", "Monthly Mean of Daily Max"]

#plt.xticks(rotation=90)
plt.tight_layout(rect=(0, 0.1, 1, 1))
ax1.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)
ax2.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)
ax3.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=wdlabels)
ax4.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=wdlabels)

plt.show()