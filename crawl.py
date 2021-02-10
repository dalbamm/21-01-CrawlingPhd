import requests
from bs4 import BeautifulSoup
from selenium import webdriver

path="/Users/primstryn/EnvFiles/"
driver=webdriver.Chrome(path+"chromedriver")

driver.get('https://console.aws.amazon.com')
driver.