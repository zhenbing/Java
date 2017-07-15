from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

original_file = "/mnt/win/meterology/test.csv"
fields = ["STATION", "YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "ODATE", "LDATE", "LTIME", "CCCC", "LATITUDE",
              "LONGITUDE", "ELEVATION", "TYPE", "STN_TYPE", "IW", "IR", "IX", "H", "VIS", "N", "WD", "WS", "AT", "TD",
              "RH", "LP", "SPL", "A3", "SLP", "DP03", "DP_IDX", "WW", "W1", "W2", "NH", "CL", "CM", "CH", "N1", "C1",
              "H1", "N2", "C2", "H2", "N3", "C3", "H3", "N4", "C4", "H4", "CBN", "CBT", "CBH", "RAIN01", "RAIN02",
              "RAIN03", "RAIN06", "RAIN09", "RAIN12", "RAIN15", "RAIN18", "RAIN24", "DP24", "DT24", "MAX_AT24",
              "MIN_AT24", "MAX_AT12", "MIN_AT12", "SNOWH", "MIN_AT", "EVA", "ALR", "SUNP", "GS", "SW1", "SW2", "SW3",
              "SW4", "SW5", "SW6", "Q_H", "Q_VIS", "Q_N", "Q_WD", "Q_WS", "Q_AT", "Q_TD", "Q_RH", "Q_LP", "Q_SPL",
              "Q_A3", "Q_SLP", "Q_DP03", "Q_DP_IDX", "Q_WW", "Q_W1", "Q_W2", "Q_NH", "Q_CL", "Q_CM", "Q_CH", "Q_N1",
              "Q_C1", "Q_H1", "Q_N2", "Q_C2", "Q_H2", "Q_N3", "Q_C3", "Q_H3", "Q_N4", "Q_C4", "Q_H4", "Q_CBN", "Q_CBT",
              "Q_CBH", "Q_RAIN01", "Q_RAIN02", "Q_RAIN03", "Q_RAIN06", "Q_RAIN09", "Q_RAIN12", "Q_RAIN15", "Q_RAIN18",
              "Q_RAIN24", "Q_DP24", "Q_DT24", "Q_MAX_AT24", "Q_MIN_AT24", "Q_MAX_AT12", "Q_MIN_AT12", "Q_SNOWH",
              "Q_MIN_AT", "Q_EVA", "Q_ALR", "Q_SUNP", "Q_GS", "Q_SW1", "Q_SW2", "Q_SW3", "Q_SW4", "Q_SW5", "Q_SW6",
              "RAIN032", "RAIN062", "RAIN122", "RAIN242", "STAMP", "TELEID"]
freq = ['D', 'M', 'Q-DEC', 'A-DEC']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# calculate daily mean value
def temp_prepare(csvfile):
    df = pd.read_csv(csvfile, sep=',', skiprows=1, header=None, names=fields)
    df['datetime'] = pd.to_datetime(df.ODATE)
    temp_df = df.pivot_table(values='AT', index='datetime', columns='STATION', aggfunc=np.mean)
    daily_temp = temp_df.resample('D', how='mean')
    return daily_temp

# calculate monthly, quarterly, yearly mean value
def temp_freq(temp_df, freq):
    try:
        # if freq=='D':
        #     print 'calculating daily temperature...'
        if freq=='M':
            print 'calculating monthly temperature...'
        elif freq=='Q-DEC':
            print 'calculating quarterly temperature...'
        elif freq=='A-DEC':
            print 'calculating yearly temperature...'

        temp_stats = temp_df.resample(freq, how='mean')
        return temp_stats
    except:
        print "the frequence parameter is not valid, valid ones are 'D', 'M', 'Q-DEC', 'A-DEC'."

# calculating ten days mean value
def temp_ten(daily_temp):
    first_ten = daily_temp[daily_temp.index.day <= 10].resample('M', how='mean', label='left', loffset='10D')
    second_ten = daily_temp[(daily_temp.index.day>=11) & (daily_temp.index.day<=20)].resample('M', how='mean',
                                                                                              label='left',
                                                                                              loffset='20D')
    third_ten = daily_temp[daily_temp.index.day >=21].resample('M', how='mean', label='right')
    tenly_temp = pd.concat([first_ten,second_ten,third_ten])
    return tenly_temp

# calculating five days mean value
def temp_five(daily_temp):
    first_five = daily_temp[daily_temp.index.day <= 5].resample('M', how='mean', label='left', loffset='5D')
    second_five = daily_temp[(daily_temp.index.day>=6) & (daily_temp.index.day<=10)].resample('M', how='mean',
                                                                                              label='left',
                                                                                              loffset='10D')
    third_five = daily_temp[(daily_temp.index.day >= 11) & (daily_temp.index.day <= 15)].resample('M', how='mean',
                                                                                                  label='left',
                                                                                                  loffset='15D')
    fourth_five = daily_temp[(daily_temp.index.day >= 16) & (daily_temp.index.day <= 20)].resample('M', how='mean',
                                                                                                 label='left',
                                                                                                 loffset='20D')
    fifth_five = daily_temp[(daily_temp.index.day >= 21) & (daily_temp.index.day <= 25)].resample('M', how='mean',
                                                                                                 label='left',
                                                                                                 loffset='25D')
    sixth_five = daily_temp[daily_temp.index.day >=26].resample('M', how='mean', label='right')
    five_temp = pd.concat([first_five,second_five,third_five,fourth_five,fifth_five,sixth_five])
    return five_temp


def annual_stats(df):
    years = np.unique(df.YEAR)
    for year in years:
        data = df[df.YEAR == year]
        month_mean = data.pivot_table(values='AT', index='STATION', columns='MONTH', aggfunc=np.mean)
        month_mean_columns = []
        for month in months:
            month_mean_columns.append('%s_mean'%month)
        month_mean.columns = month_mean_columns

        month_mean['year_mean'] = (month_mean.Jan_mean + month_mean.Feb_mean + month_mean.Mar_mean + month_mean.Apr_mean + month_mean.May_mean + month_mean.Jun_mean + month_mean.Jul_mean + month_mean.Aug_mean + month_mean.Sep_mean + month_mean.Oct_mean + month_mean.Nov_mean + month_mean.Dec_mean)/12.0

        # extrame value should record its time either
        month_max = data.pivot_table(values = 'AT', index = 'STATION', columns = 'MONTH', aggfunc = np.max)
        month_max.columns = ['Jan_max', 'Feb_max', 'Mar_max', 'Apr_max', 'May_max', 'Jun_max', 'Jul_max',
                          'Aug_max', 'Sep_max', 'Oct_max', 'Nov_max', 'Dec_max']

# pandas.resample method
def temp_stats(df):
    df['datetime']=pd.to_datetime(df.ODATE)
    temperature = df.pivot_table(values = 'AT', index='datetime', columns='STATION', aggfunc = np.mean)

    # calculate daily and monthly mean value
    daily_temp = temperature.resample('D',how='mean')
    monthly_temp = temperature.resample('M', how='mean')
    # calculate quarterly and yearly mean value, assigning december as the last month of a year
    quarterly_temp = temperature.resample('Q-DEC',how = 'mean')
    yearly_temp = temperature.resample('A-DEC', how='mean')

    return daily_temp, monthly_temp, quarterly_temp, yearly_temp

def five_days(df,delta):
    if delta ==5:
        name = 'hou'
    elif delta ==10:
        name = 'xun'
    years = np.unique(df.YEAR)
    months = np.unique(df.MONTH)
    for year in years:
        for month in months:
            timeseries = []
            start = datetime(year, month, 1)
            timeseries.append(start)
            for i in range(1,30/delta):
                timeseries.append(start + timedelta(delta)*i)


# seperate the big file by year into several csv files
def sep_by_year(original_file):
        dataframe = pd.read_csv(file, sep=',', skiprows=1, header=None, names=fields)
        years = np.unique(dataframe.YEAR)
        for year in years:
            file_name = os.path.join(os.path.dirname(original_file), "%d_surface_data.csv" % year)
            data_of_the_year = dataframe[dataframe.YEAR == year]
            # data_of_the_year = dataframe[dataframe['YEAR'] == year]

            # save data_year in to csv file
            data_of_the_year.to_csv(file_name, sep=',', header=fields)

# slice the dataframe according to datetime
def month_mean_t(df):
    month_mean = df.pivot_table(values='AT', index='STATION', columns='MONTH', aggfunc=np.mean)
    return month_mean

def month_max_t(df):
    month_max = df.pivot_table(values = 'AT', index = 'STATION', columns = 'MONTH', aggfunc = np.max)
    return month_max

def month_min_t(df):
    month_min = df.pivot_table(values = 'AT', index = 'STATION', columns = 'MONTH', aggfunc = np.min)
    return month_min

def year_mean_t(df):
    year_mean = df.pivot_table(values = 'AT', index = 'STATION', columns = 'YEAR', aggfunc = np.mean)
    return year_mean

def year_max_t(df):
    year_max = df.pivot_table(values = 'AT', index = 'STATION', columns = 'YEAR', aggfunc = np.max)
    return year_max

def year_min_t(df):
    year_min = df.pivot_table(values = 'AT', index = 'STATION', columns = 'YEAR', aggfunc = np.min)
    return year_min



