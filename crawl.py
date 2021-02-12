import sys
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

path=sys.argv[1]
pwdVal=sys.argv[2]
mode=sys.argv[3]


def __main__():
    if(mode.__ne__("no_signin")):
        src=get_phd_html()
        parseHtml(src)
    else:
        pathSrc=sys.argv[4]
        with open(pathSrc,'r') as f:
            raw=f.read()
            doc=bs(raw)
            tr_list=doc.find_all("tr")
            
            for tr in tr_list:
                td_list=tr.find_all("td")
                a_list=tr.find_all("a")
                active_list=doc.find_all("span","-")
                if active_list.__len__ !=0:
                    print(active_list)
            #for line in f.readlines():
            #    print(line)
                
        f.close()
    return

def get_phd_html():
    #set vdi
#    dp=Display(visible=0, size=(1920,1280)).start()
    

    #set headless option
    options=webdriver.ChromeOptions()
    #options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    #set driver
    driver=webdriver.Chrome(path, options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    #Access into webpage
    driver.get('https://console.aws.amazon.com')
    driver.implicitly_wait(3)
    #find & write in email input dom
    emailIpt=driver.find_element_by_id("resolving_input")
    emailIpt.send_keys("oscar.yoon13@gmail.com")
    #click next button
    nextBtn=driver.find_element_by_id("next_button")
    nextBtn.click()
#    driver.implicitly_wait(3)
    #find & write in password input dom

    WebDriverWait(driver, 10).until(EC.presense_of_element_located((By.ID, "password"))).send_keys(pwdVal)


#    pwd=driver.find_element_by_id("password")
#    pwd.send_keys(pwdVal)

    #click signin button
    sginBtn=driver.find_element_by_id("signin_button")
    sginBtn.click()

    time.sleep(10)

    #move into event log page
    driver.get("https://phd.aws.amazon.com/phd/home?region=ap-northeast-2#/event-log")
    source=driver.page_source

    driver.quit()
    
    dp.stop()
    return source;


def parseHtml(source):
    soup=bs(source, "html.parser")
    fs=open('phd.html','a')
    
    for tag in soup.find_all("tr", class_="awsui-table-row"):
        print(tag)
        fs.write(tag.__str__())
    fs.close()
    return




__main__()
