from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from columns_valuesA import columns_values
from create_dataframeA import create_dataframe
from index_date import index_date
# User and Pass and path URL 
# Amirmahdi@Soltan1383
# amirmsh20003@gmail.com
# https://www.tradingview.com/chart/qCGg4jUl/?symbol=OANDA%3AXAUUSD
# except Exception as e:
#     print('ERRRRRRRRRRRRRROOORRRRRRRRRRR\n')
#     lst_error.append(1)
#     continue


time_restart = datetime.now()
lst = []
try:
    driver = webdriver.Firefox()
    driver.get('https://www.tradingview.com/')
    time.sleep(1)
    driver.maximize_window()
except Exception as e :
    print("Error :",e) 
count = 0
# today date
today = datetime.today()

# mointore size
monitore_size_x = pyautogui.size()[0]

# list for save valuewrapper
lst_string_values = []
lst_float_values = []
lst_string_vol = []
lst_index = []
# movment on screen
monitore_size_x = 1858
lst_error = list()

ready = input('are you ready ? ')
if ready == 'y':
    time.sleep(10)
    while count != 100:
        for i in range(monitore_size_x, 150, -5):
            pyautogui.moveTo(i, 600)

            x = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]')
            print(x.text)

            x_vol = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div')
            print(x_vol.text)
            if x.text not in lst_string_values:
                if type(x_vol.text) != str:
                    continue                        
                now_str, today = index_date(today)
                lst_index.append(now_str)
                try  : 
                    lst_float_values.append(columns_values(
                        x.text, float(x_vol.text.strip()[:len(x_vol.text)-1])))
                    lst_string_values.append(x.text)
                    lst_string_vol.append(x_vol.text)
                except : 
                    lst_index.pop()

        last_pos = pyautogui.position()
        pyautogui.moveTo(last_pos[0], last_pos[1])
        pyautogui.mouseDown()
        pyautogui.dragRel(int(pyautogui.size()[0]/2)+200, 0, duration=.2)
        pyautogui.mouseUp()
        monitore_size_x = pyautogui.position()[0]
        # Sleep for Load Website
        time.sleep(1)
        count += 1



df_information = create_dataframe(lst_float_values, lst_index)
print(df_information.head(10))

df_information.to_csv(
    'gold_price_dayli_oanda.csv', index=True, header=True)
df_practice = df_information[:14]
print(df_practice)

print(len(lst_error))
time.sleep(15)
driver.quit()
