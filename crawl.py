import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

path="/Users/primstryn/EnvFiles/"
pwdVal="InputYours"

driver=webdriver.Chrome(path+"chromedriver")

#Access into webpage
driver.get('https://console.aws.amazon.com')

#find & write in email input dom
emailIpt=driver.find_element_by_id("resolving_input")
emailIpt.send_keys("oscar.yoon13@gmail.com")

#click next button
nextBtn=driver.find_element_by_id("next_button")
nextBtn.click()

#find & write in password input dom
pwd=driver.find_element_by_id("password")
pwd.send_keys(pwdVal)

#click signin button
sginBtn=driver.find_element_by_id("signin_button")
sginBtn.click()
