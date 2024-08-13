import pandas as pd

# Give informtaion about Pirce of Gold 
information_price = pd.read_csv('Main_Plot_Source_code/gold_price_dayli_oanda.csv')


class Checklines:
    
    # lines  and list of lines
    # define lines (AI Methods)
    high = (information_price["High"].iloc[1] + information_price["High"].iloc[2])/2
    low = (information_price["Low"].iloc[1] + information_price["Low"].iloc[2])/2
    nim = high - low
    # ----- lines ---- 
    line1 = low + (nim * 1.618)
    line2 = low + (nim * 1.27)
    line3 = low + (nim * 0.114)
    line4 = low + (nim * 0.382)
    line5 = low + (nim * 0.618)
    line6 = low + (nim * 0.886)
    line7 = low + (nim * (-0.27)) * -1
  
   