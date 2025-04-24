from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to use enter 
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.edge.options import Options

def credit():
    load_dotenv()
    username = f"{os.getenv('USER_NAME')}"
    password = f"{os.getenv('PASSWORD')}"
    edge_options = Options()
    edge_options.add_experimental_option("detach",True)
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=edge_options)
    return driver, username, password

def login():
    driver, username, password = credit()
    driver.get(f'{os.getenv('LINK')}')

    driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/div/div/div[2]/div[2]/a[1]").click()
    driver.find_element(By.NAME,"username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/form/button").click()
    time.sleep(1)
    return driver



