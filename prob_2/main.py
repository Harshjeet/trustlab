import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_actual_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    actual_url = response.url
    return actual_url


driver = webdriver.Chrome()
actions = webdriver.ActionChains(driver)

short_url = input('Enter your tiny url(include http:// or https://): ')
if short_url:
    actual_url = get_actual_url(short_url)

    file_name = input('Enter the url file name to save (in .txt) : ')
    with open(file_name, 'w') as f:
        f.write(actual_url)

    driver.get(actual_url)
else:
    gsheet_url = input('enter your gsheet url :')
    driver.get(gsheet_url)

driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/div[1]').click()
actions.send_keys('d')
actions.perform()

user_input = input("press the key (x for excel_file or c for csv_file : ").strip()
if user_input == 'x':
    actions.send_keys(user_input)
    actions.perform()

elif user_input == 'c':
    actions.send_keys(user_input)
    actions.perform()
time.sleep(5)
    
