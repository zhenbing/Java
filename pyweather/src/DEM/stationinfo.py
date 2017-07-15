import pandas as pd
from pandas import DataFrame, Series
import numpy as np

file = "/mnt/win/weatherdata/ZR_SURF2010-2015.csv"
data_dir = "/mnt/win/weatherdata/"
fields = ["STATION","YEAR","MONTH","DAY","HOUR","MINUTE","ODATE","LDATE","LTIME","CCCC","LATITUDE","LONGITUDE","ELEVATION","TYPE","STN_TYPE","IW","IR","IX","H","VIS","N","WD","WS","AT","TD","RH","LP","SPL","A3","SLP","DP03","DP_IDX","WW","W1","W2","NH","CL","CM","CH","N1","C1","H1","N2","C2","H2","N3","C3","H3","N4","C4","H4","CBN","CBT","CBH","RAIN01","RAIN02","RAIN03","RAIN06","RAIN09","RAIN12","RAIN15","RAIN18","RAIN24","DP24","DT24","MAX_AT24","MIN_AT24","MAX_AT12","MIN_AT12","SNOWH","MIN_AT","EVA","ALR","SUNP","GS","SW1","SW2","SW3","SW4","SW5","SW6","Q_H","Q_VIS","Q_N","Q_WD","Q_WS","Q_AT","Q_TD","Q_RH","Q_LP","Q_SPL","Q_A3","Q_SLP","Q_DP03","Q_DP_IDX","Q_WW","Q_W1","Q_W2","Q_NH","Q_CL","Q_CM","Q_CH","Q_N1","Q_C1","Q_H1","Q_N2","Q_C2","Q_H2","Q_N3","Q_C3","Q_H3","Q_N4","Q_C4","Q_H4","Q_CBN","Q_CBT","Q_CBH","Q_RAIN01","Q_RAIN02","Q_RAIN03","Q_RAIN06","Q_RAIN09","Q_RAIN12","Q_RAIN15","Q_RAIN18","Q_RAIN24","Q_DP24","Q_DT24","Q_MAX_AT24","Q_MIN_AT24","Q_MAX_AT12","Q_MIN_AT12","Q_SNOWH","Q_MIN_AT","Q_EVA","Q_ALR","Q_SUNP","Q_GS","Q_SW1","Q_SW2","Q_SW3","Q_SW4","Q_SW5","Q_SW6","RAIN032","RAIN062","RAIN122","RAIN242","STAMP","TELEID"]

df = pd.read_csv(file, sep=',',skiprows=1, header=None, names = fields)
station_ids = np.unique(df.STATION)

station_df = df.pivot_table(values='STATION', index='', columns='STATION', aggfunc=np.mean)

data_of_the_year = df[df.STATION == year]
data_of_the_year.to_csv(file_name,sep=',',header=fields)