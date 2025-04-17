from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to use enter 
import time

username = "melibi8600@exclussi.com"
password = "screener@12345"

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# driver.maximize_window()    # to maximize the web page
driver.get('https://www.screener.in/')

driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/div/div/div[2]/div[2]/a[1]").click()
driver.find_element(By.NAME,"username").send_keys(username)
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/form/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div[2]/main/div[1]/div[2]/a[1]").click()

data = {}

tr_rows = driver.find_elements(By.XPATH,"/html/body/main/div[3]/div[3]/table/tbody/tr")
req_rows = len(tr_rows)

for cols in range(2,19):
    head = driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{cols}]').text
    data[head]=[]
    head=''

for rows in range(2,req_rows+1):
    for cols in range(2,19):
        head = driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{cols}]').text
        if rows != 17:
            if cols>=2:
                value=driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[{rows}]/td[{cols+1}]').text
        else:
            continue
        data[head].append(value)
        head,value='',''

time.sleep(1)
print("Your data is Scrap from Screener.in")
driver.close()