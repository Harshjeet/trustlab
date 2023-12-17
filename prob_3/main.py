from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
actions = webdriver.ActionChains(driver)
driver.get('https://euromomo.eu/graphs-and-maps')

driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/article/section/div[2]').click()
driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/article/section/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]').click()

driver.find_element(By.XPATH, '//*[@id="excess-mortality"]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]').click()
driver.find_element(By.XPATH, '').click()
driver.find_element(By.XPATH, '').click()
driver.find_element(By.XPATH, '').click()
driver.find_element(By.XPATH, '').click()

time.sleep(10)
