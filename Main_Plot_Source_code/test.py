from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

count = 0
driver = ''
for i in range(10):
    if count == 0:
        driver = webdriver.Firefox()
        driver.get(
            'https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD')
        sleep(3)
        driver.maximize_window()
        count += 1

        price_pertime = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]')

    print(float((price_pertime.text).strip()))

    print('Round')
