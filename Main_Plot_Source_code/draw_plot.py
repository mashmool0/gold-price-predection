from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from price_per_time_webA import OpenWeb
from CheckPlost import Checklines as cl

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
lst_time = []
lst_price = []
count = 0 

def Create_Plots():
    global lst_price, lst_time, driver ,count 

    driver = OpenWeb(False, None)


    # Call animation Function
    ani = animation.FuncAnimation(
        fig, animate, interval=1000, repeat=True, blit=False, cache_frame_data=False
    )
    plt.title('Gold Price')
    plt.show()
# Define All of list  for Another Plot Check 
lst_line1 = list()
lst_line2 = list()
lst_line3 = list()
lst_line4 = list()
lst_line5 = list()
lst_line6 = list()
lst_line7 = list()

def animate(i):
    global lst_line1,lst_line2,lst_line3,lst_line4,lst_line5,lst_line6,lst_line7
    # Give information
    price,line1,line2,line3,line4,line5,line6,line7,current_time = OpenWeb(True, driver)

    # Create lst for them (need lst to draw)
    lst_time.append(current_time)
    lst_price.append(price)

    # Define list for creating plot
    
    # another lines
    lst_line1.append(line1)
    lst_line2.append(line2)
    lst_line3.append(line3)
    lst_line4.append(line4)
    lst_line5.append(line5)
    lst_line6.append(line6)
    lst_line7.append(line7)

    # Draw Plost
    ax.clear()
    ax.plot(lst_time, lst_price)
    # Draw another Plots
    if len(lst_line1) == len(lst_time) : 
        plt.plot(lst_time, lst_line1)
        plt.plot(lst_time, lst_line2)
        plt.plot(lst_time, lst_line3)
        plt.plot(lst_time, lst_line4)
        plt.plot(lst_time, lst_line5)
        plt.plot(lst_time, lst_line6)
        plt.plot(lst_time, lst_line7)
    else : 
        if len(lst_line1) > len(lst_time) : 
            lst_line1.pop()
            lst_line2.pop()
            lst_line3.pop()
            lst_line4.pop()
            lst_line5.pop()
            lst_line6.pop()
            lst_line7.pop()    
        else  : 
            lst_time.pop()

    # Set name for Labels
    ax.set_xlabel("Time")
    ax.set_ylabel("Gold Price")
