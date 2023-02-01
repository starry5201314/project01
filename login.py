import time

from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Chrome()
addrss01 = input("请输入ip地址")
wd.get(f"http://{addrss01}/login.html?v=1675213907073")
time.sleep(5)
wd.find_element(By.XPATH,'//*[@id="userName"]').click()
wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys('admin')
wd.find_element(By.XPATH,'//*[@id="pwd"]').click()
wd.find_element(By.XPATH,'//*[@id="pwd"]').send_keys('12345')
wd.find_element(By.XPATH,'/html/body/div/div[2]/div/div[4]/button').click()
time.sleep(2)
wd.find_element(By.XPATH,'//*[@id="alert"]/div/div[3]/input[1]').click()

print("hello world")