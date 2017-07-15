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
def winds_prepare(csvfile):
    df = pd.read_csv(csvfile, sep=',', skiprows=1, header=None, names=fields)
    df['datetime'] = pd.to_datetime(df.ODATE)
    winds_df = df.pivot_table(values='WS', index='datetime', columns='STATION', aggfunc=np.mean)
    daily_winds = winds_df.resample('D', how='mean')
    return daily_winds

# calculate monthly, quarterly, yearly mean value
def windse_freq(winds_df, freq):
    try:
        # if freq=='D':
        #     print 'calculating daily winds...'
        if freq=='M':
            print 'calculating monthly winds...'
        elif freq=='Q-DEC':
            print 'calculating quarterly winds...'
        elif freq=='A-DEC':
            print 'calculating yearly winds...'

            winds_stats = winds_df.resample(freq, how='mean')
        return winds_stats
    except:
        print "the frequence parameter is not valid, valid ones are 'D', 'M', 'Q-DEC', 'A-DEC'."

# calculating ten days mean value
def winds_ten(daily_winds):
    first_ten = daily_winds[daily_winds.index.day <= 10].resample('M', how='mean', label='left', loffset='10D')
    second_ten = daily_winds[(daily_winds.index.day>=11) & (daily_winds.index.day<=20)].resample('M', how='mean',
                                                                                              label='left',
                                                                                              loffset='20D')
    third_ten = daily_winds[daily_winds.index.day >=21].resample('M', how='mean', label='right')
    tenly_winds = pd.concat([first_ten,second_ten,third_ten])
    return tenly_winds

# calculating five days mean value
def winds_five(daily_winds):
    first_five = daily_winds[daily_winds.index.day <= 5].resample('M', how='mean', label='left', loffset='5D')
    second_five = daily_winds[(daily_winds.index.day>=6) & (daily_winds.index.day<=10)].resample('M', how='mean',
                                                                                              label='left',
                                                                                              loffset='10D')
    third_five = daily_winds[(daily_winds.index.day >= 11) & (daily_winds.index.day <= 15)].resample('M', how='mean',
                                                                                                  label='left',
                                                                                                  loffset='15D')
    fourth_five = daily_winds[(daily_winds.index.day >= 16) & (daily_winds.index.day <= 20)].resample('M', how='mean',
                                                                                                 label='left',
                                                                                                 loffset='20D')
    fifth_five = daily_winds[(daily_winds.index.day >= 21) & (daily_winds.index.day <= 25)].resample('M', how='mean',
                                                                                                 label='left',
                                                                                                 loffset='25D')
    sixth_five = daily_winds[daily_winds.index.day >=26].resample('M', how='mean', label='right')
    five_winds = pd.concat([first_five,second_five,third_five,fourth_five,fifth_five,sixth_five])
    return five_winds
