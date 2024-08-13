import pandas as pd
import math
from statistics import mean


def calc_alpha(num):
    x_radians = math.atan(num)
    x_degree = math.degrees(x_radians)
    return x_degree


# create new_df
main_df = pd.read_csv('gold_price_dayli_oanda.csv')

n = 14  # you can input it
num_round = main_df.count()[1] // n
row_x1 = 0
row_x2 = n

lst_close = []
lst_open = []
lst_index = []
lst_rise_fall = []
lst_degree = []
lst_volume = []
lst_subs_open_close = []
lst_trend_slope = []
for i in range(num_round):
    # akharesh age ezaf oomad ignore kon
    if row_x2 - main_df.count()[1] > 0:
        break
    # create lst close and open
    lst_close.append(list(main_df['Close'][row_x1:row_x2]))
    lst_open.append(list(main_df['Open'][row_x1:row_x2]))
    # calc index
    lst_index.append(f'({row_x1}to{row_x2})')
    # calc volume mean /1000
    lst_volume.append(mean(list(main_df['Volume'][row_x1:row_x2])) / 1000)
    # calc sub open and close
    lst_subs_open_close.append(
        sum(list(main_df['Open']-main_df['Close'])[row_x1:row_x2]))

    # baze dataframe selecting
    row_x1 += n
    row_x2 += n

# create new
lst_line_slope_mm = []

# calculate line slope  between max and min open and close
# calc rise or fall
# calc degree

for i in range(len(lst_close)):
    # line slope min max
    # for calc slope
    if lst_close[i][0] - lst_close[i][-1] > 0:
        line_slope = (max(lst_close[i]) - min(lst_close[i]))
    else:
        line_slope = (max(lst_close[i]) - min(lst_close[i])) * -1

    line_slope = line_slope / n
    line_slope = round(line_slope, 3)
    lst_line_slope_mm.append(line_slope)
    # calc trend slope   firs close and last close delta  / n  --- > trend slope
    trend_slope = lst_close[i][0] - lst_close[i][1]
    trend_slope = trend_slope / n
    lst_trend_slope.append(trend_slope)

    # rise or fall
    if lst_close[i][0] - lst_close[i][-1] > 0:
        lst_rise_fall.append(1)
    else:
        lst_rise_fall.append(0)
    # degree
    lst_degree.append(calc_alpha(line_slope))

new_df = pd.DataFrame(lst_line_slope_mm, index=lst_index,
                      columns=['Line Slope MM'])

new_df['Degree'] = lst_degree
new_df['Mean'] = lst_volume
new_df['Sub oc'] = lst_subs_open_close
new_df['Trend slope'] = lst_trend_slope
new_df.index.name = 'num of df'
new_df.to_csv('chart_details.csv')
