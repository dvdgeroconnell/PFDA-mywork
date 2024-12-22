# ********************************************************************************************************
# assignment_6_Weather.py
#
# Purpose of Program:
#   A program to...
#
# Assumptions:
#   List any assumptions here...
#
# Author: David O'Connell
#
# References:
#   PFDA Topic 56 lecture videos (Andrew Beatty) - https://vlegalwaymayo.atu.ie/course/view.php?id=10462
#    
#   The following sites were the primary references for research on Python, matplotlib, NumPy and pandas 
#     https://www.geeksforgeeks.org/
#     https://stackoverflow.com/
#     https://matplotlib.org/
#     https://www.w3schools.com/
#     https://pandas.pydata.org/
#     https://www.datacamp.com/
#
# ********************************************************************************************************
#
# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns

# Read the file, drop the first 23 rows as they are header data, then also drop the first row
# of data as there are nearly 4 months of data missing after it
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv", skiprows=23,low_memory=False)
df = df.drop(0)

df['datetime'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['datetime2'] = df['datetime']
df = df.set_index('datetime2')
#df['yr'] = pd.DatetimeIndex(df['datetime']).year

mean_daily_temp = df["temp"].resample("d").mean()
#print(mean_daily_temp.head(1))
mean_monthly_temp = df["temp"].resample("m").mean()
#print(mean_monthly_temp.head(1))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,8), sharex='col')
ax1 = axes[0]
ax2 = axes[1]
ax1.plot(df["datetime"], df["temp"])
ax1.plot(mean_daily_temp)
ax1.plot(mean_monthly_temp)
ax1.set_title('Full Dataset', fontsize=14)

dateFrom = "2024-01-01 01:00:00"
dateTo = "2024-12-31 23:00:00"
df_latest = df.loc[dateFrom:dateTo]
mean_daily_temp_latest = df_latest["temp"].resample("d").mean()
print(mean_daily_temp_latest.head(1))
print(mean_daily_temp_latest.tail(1))
mean_monthly_temp_latest = df_latest["temp"].resample("m").mean()

ax2.plot(df_latest["datetime"], df_latest["temp"])
ax2.plot(mean_daily_temp_latest)
ax2.plot(mean_monthly_temp_latest)
ax2.set_title('Latest Year', fontsize=14)

xlabels = ["Hourly Temp","Daily Avg","Monthly Avg"]
plt.xticks(rotation=90)
plt.tight_layout(rect=(0, 0.1, 1, 1))
ax1.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)
ax2.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)

plt.show()