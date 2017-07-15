from collections import defaultdict

WIND_D = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'C']
#value_range = (0,360)
def add_windd_col(df):
    # add a column to store the wind direction strings, such as N, NNE, NE, etc.
    x = df.WD
    y = df.WS

    df.loc[((x >= 348.76) & (x <= 360)) , 'WDS'] = 'N'
    df.loc[((x >= 0) & (x <= 11.25)), 'WDS'] = 'N'
    df.loc[(x >= 11.26) & (x <= 33.75), 'WDS'] = 'NNE'
    df.loc[(x >= 33.76) & (x <= 56.25), 'WDS'] = 'NE'
    df.loc[(x >= 56.26 ) & (x <= 78.75), 'WDS'] = 'ENE'
    df.loc[(x >= 78.76) & (x <= 101.25), 'WDS'] = 'E'
    df.loc[(x >= 101.26) & (x <= 123.75), 'WDS'] = 'ESE'
    df.loc[(x >= 123.76 ) & (x <= 146.25), 'WDS'] = 'SE'
    df.loc[(x >= 146.26) & (x <= 168.75), 'WDS'] = 'SSE'
    df.loc[(x >= 168.76) & (x <= 191.25), 'WDS'] = 'S'
    df.loc[(x >= 191.26) & (x <= 213.75), 'WDS'] = 'SSW'
    df.loc[(x >= 213.76) & (x <= 236.25), 'WDS'] = 'SW'
    df.loc[(x >= 236.26) & (x <= 258.75), 'WDS'] = 'WSW'
    df.loc[(x >= 258.76) & (x <= 281.25), 'WDS'] = 'W'
    df.loc[(x >= 281.26 ) & (x <= 303.75), 'WDS'] = 'WNW'
    df.loc[(x >= 303.76) & (x <= 326.25), 'WDS'] = 'NW'
    df.loc[(x >= 326.26) & (x <= 348.75), 'WDS'] = 'NNW'
    df.loc[((y <= 0.2) & (x>=0) & (x<=360)), 'WDS'] = 'C'

    return df

def count(df):
    # counting the number of each wind direction and store in dictionary
    counts = defaultdict(int)
    for wd in WIND_D:
        counts[wd] = (df.WDS == wd).sum()
    return counts

def windd_freq(counts_dict):
    valid_num = sum(counts_dict.values())
    max_value = max(counts_dict.values())
    new_dict = {v: k for k, v in counts_dict.items()}
    most_freq = new_dict[max_value]
    frequence = max_value*100.0/valid_num
    print 'the most frequency wind direction is %s, and its frequency is %.2f %s.'%(most_freq, frequence,'%')
    return most_freq, frequence

# # sequence = [(x1,y1),(x2,y2),...]
# def directions_counts(sequence):
#     counts = defaultdict(int)
# #     x-wind direction;y-wind velocity
#     for x,y in sequence:
#         if (x>=348.76 and x<=360) or (x>=0 and x<=11.25):
#             counts['N']+=1
#         elif x>=11.26 and x<=33.75:
#             counts['NNE']+=1
#         elif x>=33.76 and x<=56.25:
#             counts['NE']+=1
#         elif x>=56.26 and x<=78.75:
#             counts['ENE']+=1
#         elif x>=78.76 and x<=101.25:
#             counts['E']+=1
#         elif x>=101.26 and x<=123.75:
#             counts['ESE']+=1
#         elif x>=123.76 and x<=146.25:
#             counts['SE']+=1
#         elif x>=146.26 and x<=168.75:
#             counts['SSE']+=1
#         elif x>=168.76 and x<=191.25:
#             counts['S']+=1
#         elif x>=191.26 and x<=213.75:
#             counts['SSW']+=1
#         elif x>=213.76 and x<=236.25:
#             counts['SW']+=1
#         elif x>=236.26 and x<=258.75:
#             counts['WSW']+=1
#         elif x>=258.76 and x<=281.25:
#             counts['W']+=1
#         elif x>=281.26 and x<=303.75:
#             counts['WNW']+=1
#         elif x>=303.76 and x<=326.25:
#             counts['NW']+=1
#         elif x>=326.26 and x<=348.75:
#             counts['NNW']+=1
#         elif y<=0.2:
#             counts['C']+=1
#         else:
#             counts['None']+1
#
# # find the most frequent wind direction and its counts [(count, wind_dirction)]
# def top_counts(count_dict, n=1):
#     value_key_pairs = [(count, wind_direction) for wind_direction, count in count_dict.items()]
#     value_key_pairs.sort()
#     return value_key_pairs[-n:]
