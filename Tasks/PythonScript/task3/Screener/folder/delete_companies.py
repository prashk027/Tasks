import pandas as pd
from selenium.webdriver.common.by import By
import time
from login_screener import credit

driver = credit()[0]

def delete_comp():
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/a").click()
    delete_each_comp()

def delete_each_comp():
    ul = driver.find_elements(By.XPATH,"/html/body/main/div[2]/div[2]/ul/li")

    total_comp = len(ul)
    isNotZero = True

    while isNotZero:
        if total_comp == 0:
            isNotZero = False
        else:
            for i in range(total_comp):
                time.sleep(2)
                driver.find_element(By.XPATH,"//*[@id='watchlist-content']/ul/li[1]/button").click()
                time.sleep(1)
            break
        total_comp = len(driver.find_elements(By.XPATH,"/html/body/main/div[2]/div[2]/ul/li"))


def loggedIn():
    try:
        driver.find_element(By.XPATH,"/html/body/div/div[2]/main/div[1]/div[2]/a[2]").click()
        delete_each_comp()

    except Exception as e:
        print(e)

    finally:
        print("DELETED ALL ROWS")
        driver.close()