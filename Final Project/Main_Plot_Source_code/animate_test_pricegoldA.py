from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import datetime as dt
from price_per_time_webA import price_per_time_func
import numpy as np 
# dataframe
df_information = pd.read_csv('gold_price_dayli_oanda.csv')

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# define list for time and price
lst_price = []
lst_time = []

# start plot
starter = 1939

# define list for lines
lst_line1 = []
lst_line2 = []
lst_line3 = []
lst_line4 = []
lst_line5 = []
lst_line6 = []
lst_line7 = []
lst_line8 = []
# defint scatter list
lst_time_scatter_t = []
lst_price_scatter_t = []
lst_price_scatter_f = []
lst_time_scatter_f = []

# define lines
high = (df_information["High"].iloc[2] + df_information["High"].iloc[3])/2
low = (df_information["Low"].iloc[2] + df_information["Low"].iloc[3])/2

nim = high - low

line1 = low + (nim * 1.618)
line2 = low + (nim * 1.27)
line3 = low + (nim * 0.114)
line4 = low + (nim * 0.382)
line5 = low + (nim * 0.618)
line6 = low + (nim * 0.886)
# line7 = low + (nim * (-0.27)) * -1


# sell and buy
sell1 = 0
sell2 = 0
sell3 = 0
sell4 = 0
buy1 = 0
buy2 = 0
buy3 = 0
buy4 = 0
count = -1
first = 0
first2 = 0
# time_col list
time_col = []  # for sell
time_col_2 = []

time_col2 = []  # for buy
time_col2_2 = []


def animate(i):
    # defins as global
    global starter, lst_line1, lst_line2, lst_line3, lst_line4, lst_line5, lst_line6, lst_line7
    global line1, line2, line3, line4, line5, line6, sell1, buy1, count, time_col
    global sell2, sell3, buy2, buy2, buy3, buy4, first, first2, time_col_2, time_col2_2, price_per_time_func


    gold_price = price_per_time_func()
    lst_price.append(gold_price)

    # time list
    time_now = datetime.now()
    lst_time.append(time_now)

    # lines list
    lst_line1.append(line1)
    lst_line2.append(line2)
    lst_line3.append(line3)
    lst_line4.append(line4)
    lst_line5.append(line5)
    lst_line6.append(line6)

    # main plot
    ax.plot(lst_time, lst_price, 'red')

    # line plot
    plt.plot(lst_time, lst_line1, 'blue')
    plt.plot(lst_time, lst_line2, 'blue')
    plt.plot(lst_time, lst_line3, 'blue')
    plt.plot(lst_time, lst_line4, 'blue')
    plt.plot(lst_time, lst_line5, 'blue')
    plt.plot(lst_time, lst_line6, 'blue')
    print(lst_price[-1])
    print(lst_line6[-1])
    # ------------------------------------- sell and buy ---------------------------
    # sells -----------------------------------------------
    # ------------------- sell1 -------------
    if sell1 == 0:
        if abs(lst_price[-1] - lst_line6[-1]) < .22 and lst_price[-1] < lst_line6[-1]:
            lst_time_scatter_t.append(lst_time[-1])
            lst_price_scatter_t.append(lst_line6[-1])
            time_col.append(time_now)
            sell1 = 1
        elif abs(lst_price[-1] - lst_line6[-1]) < .22 and lst_price[-1] > lst_line6[-1]:
            lst_time_scatter_f.append(lst_time[-1])
            lst_price_scatter_f.append(lst_line6[-1])

    elif sell1 == 1:
        if abs(lst_price[-1] - lst_line6[-1]) < .22:
            lst_time_scatter_f.append(lst_time[-1])
            lst_price_scatter_f.append(lst_line6[-1])

    # ------------------ sell2 ------------------
    if sell2 == 0:
        if len(time_col) == 2:
            if dt.timedelta(seconds=10) < time_col[1] - time_col[0]:
                time_col.append(0)
                sell2 = 1
            else:
                time_col.append(0)

        elif len(time_col) == 1 and abs(lst_price[-1] - lst_line2[-1]) < .22:
            time_col.append(time_now)

        elif abs(lst_price[-1] - lst_line2[-1]) < .22 and len(time_col) == 3:
            lst_time_scatter_f.append(lst_time[-1])
            lst_price_scatter_f.append(lst_line2[-1])

    elif sell2 == 1 and abs(lst_price[-1] - lst_line2[-1]) < .22:  # done sell
        lst_time_scatter_t.append(lst_time[-1])
        lst_price_scatter_t.append(lst_line2[-1])
        time_col_2.append(time_now)
        sell2 = 0  # sell shod
    # ---------------------- sell3 ------------------
    if sell3 == 0:
        if sell1 == 1 and sell2 == 1:
            if len(time_col_2) == 2:
                if dt.timedelta(minutes=1) < time_col_2[1] - time_col_2[0]:
                    time_col_2.append(0)
                    sell3 = 1
                else:
                    time_col_2.append(0)

            elif len(time_col_2) == 1 and abs(lst_price[-1] - lst_line1[-1]) < .22:
                time_col_2.append(time_now)

            elif abs(lst_price[-1] - lst_line1[-1]) < .22 and len(time_col_2) == 3:
                lst_time_scatter_f.append(lst_time[-1])
                lst_price_scatter_f.append(lst_line1[-1])

        elif sell1 == 1 and sell2 == 0 and abs(lst_price[-1] - lst_line1[-1]) < .22 and first == 0:
            if lst_price[-1] < lst_line1[-1]:
                sell3 = 1
                first += 1
        elif sell1 == 1 and sell2 == 0 and abs(lst_price[-1] - lst_line1[-1]) < .22 and first == 1:
            lst_price_scatter_f.append(lst_line1[-1])
            lst_time_scatter_f.append(lst_time[-1])

    elif sell3 == 1 and abs(lst_price[-1] - lst_line1[-1]) < .22:
        lst_price_scatter_t.append(lst_line1[-1])
        lst_time_scatter_t.append(lst_time[-1])
        sell3 = 0
    # buys--------------
    # --------------- buy1 ----------------------
    if buy1 == 0:
        if abs(lst_price[-1] - lst_line5[-1]) < .22:
            lst_time_scatter_t.append(lst_time[-1])
            lst_price_scatter_t.append(lst_line5[-1])
            time_col2.append(time_now)
            buy1 = 1

    elif buy1 == 1:
        if abs(lst_price[-1] - lst_line5[-1]) < .22:
            lst_time_scatter_f.append(lst_time[-1])
            lst_price_scatter_f.append(lst_line5[-1])
    # -------------- buy2 ----------------------
    if buy2 == 0:
        if len(time_col2) == 2:
            if dt.timedelta(seconds=100) < time_col2[1] - time_col2[0]:
                time_col2.append(0)
                buy2 = 1
            else:
                time_col2.append(0)

        elif abs(lst_price[-1] - lst_line4[-1]) < .22 and len(time_col2) == 1:
            time_col2.append(time_now)

        elif abs(lst_price[-1] - lst_line4[-1]) < .22 and len(time_col2) == 3:
            lst_time_scatter_f.append(lst_time[-1])
            lst_price_scatter_f.append(lst_line4[-1])

    elif buy2 == 1:
        lst_time_scatter_t.append(lst_time[-1])
        lst_price_scatter_t.append(lst_line4[-1])
        buy2 = 0
    # ------------------ buy3 --------------
    if buy3 == 0:
        if buy1 == 1 and buy2 == 1:
            if len(time_col2_2) == 2:
                if dt.timedelta(minutes=1) < time_col2_2[1] - time_col2_2[0]:
                    time_col2_2.append(0)
                    sell3 = 1
                else:
                    time_col2_2.append(0)

            elif len(time_col2_2) == 1 and abs(lst_price[-1] - lst_line3[-1]) < .22:
                time_col2_2.append(time_now)

            elif abs(lst_price[-1] - lst_line3[-1]) < .22 and len(time_col2_2) == 3:
                lst_time_scatter_f.append(lst_time[-1])
                lst_price_scatter_f.append(lst_line3[-1])
        elif buy1 == 1 and buy2 == 0 and abs(lst_price[-1] - lst_line3[-1]) < .22 and first2 == 0:
            buy3 = 1
            first2 += 1

        elif buy1 == 1 and buy2 == 0 and abs(lst_price[-1] - lst_line3[-1]) < .22 and first2 == 1:
            lst_price_scatter_f.append(lst_line3[-1])
            lst_time_scatter_f.append(lst_time[-1])

    elif buy3 == 1 and abs(lst_price[-1] - lst_line3[-1]) < .22:
        lst_price_scatter_t.append(lst_line3[-1])
        lst_time_scatter_t.append(lst_time[-1])
        buy3 = 0
    # draw scatter plot
    plt.scatter(lst_time_scatter_t, lst_price_scatter_t,
                c='green', s=35)  # T
    plt.scatter(lst_time_scatter_f, lst_price_scatter_f, c='orange', s=35)  # F


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(
    fig, animate, interval=1000, cache_frame_data=False)
plt.show()
