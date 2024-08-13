from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from CheckPlost import Checklines as cl 
from datetime import datetime

count = 0 
driver2 = None 
def OpenWeb(Detail:bool,driver2):
    global count 
    # Just one time Open Web site 
    if count == 0 and driver2 == None : 
        # Open The website for all of work 
        try:
            # Open Website 
            driver2 = webdriver.Firefox()
            driver2.get('https://www.tradingview.com/')
            sleep(2)
            driver2.maximize_window()
            ready  = input('are you ready ?(y/n)  --> change your url to your chart you want then  enter y') 
            if ready == 'y' : 
                pass 
            else : 
                return 
            # Check for specific errors (404 and 403)
            if "404" in driver2.title:
                print("Error 404: Page not found")
            elif "403" in driver2.title:
                print("Error 403: Forbidden\nTurn Off your Vpn \nOr\nTurn ON your Vpn \nOr\nChange Your Vpn\nCheck All of this method")
            else:
                print("Page loaded successfully")
            
            count += 1 
            # Check Website Still Open or Closed ? 
            try:
                element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
                WebDriverWait(driver2, 10).until(element_present)
                print("Web page is still open.")
            except Exception as e:
                print("Web page is closed or not responsive:", str(e))
                count = 0 
            
            return driver2 

        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            
    def price_per_time() : 
        try : 
            
            price_pertime = driver2.find_element(
            by=By.XPATH, value='/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]')
            return float(price_pertime.text),cl.line1,cl.line2,cl.line3,cl.line4,cl.line5,cl.line6,cl.line7,datetime.now()
             
        except : 
            print('Update Your Path!\nClick on Update Button')
        # return price_pertime.text 

    if Detail : 
        return price_per_time()
