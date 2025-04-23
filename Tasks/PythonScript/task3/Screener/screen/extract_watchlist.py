from selenium.webdriver.common.by import By
import time
import login_screener

data={}
driver = login_screener.login()

def extract():
    try:
        tr_rows = driver.find_elements(By.XPATH,"/html/body/main/div[3]/div[3]/table/tbody/tr")
        req_rows = len(tr_rows)

        for cols in range(2,19):
            head = driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{cols}]').text
            data[head]=[]
            
        for i in range(2, req_rows + 1):
            if (i - 1) % 16 == 0:
                continue
            for col in range(2, 19):
                header = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{col}]').text
                value = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[{i}]/td[{col + 1}]').text
                data[header].append(value)
        time.sleep(1)
        print("Your data is Scrap from Screener.in")

    except Exception as e:
        print(e)
        time.sleep(1)
        print("NO COMPANIES")

    finally:
        time.sleep(1)
        driver.close()

def extract_watch():
    tr_rows = driver.find_elements(By.XPATH,"/html/body/main/div[3]/div[3]/table/tbody/tr")
    req_rows = len(tr_rows)

    for cols in range(2,19):
        head = driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{cols}]').text
        data[head]=[]
            
        for i in range(2, req_rows + 1):
            if (i - 1) % 16 == 0:
                continue
            for col in range(2, 19):
                header = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{col}]').text
                value = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[{i}]/td[{col + 1}]').text
                data[header].append(value)
    time.sleep(1)
    print("Your data is Scrap from Screener.in")


driver.find_element(By.XPATH,"/html/body/div/div[2]/main/div[1]/div[2]/a[1]").click()
try:
    tr_rows = driver.find_elements(By.XPATH,"/html/body/main/div[3]/div[3]/table/tbody/tr")
    req_rows = len(tr_rows)

    for cols in range(2,19):
        head = driver.find_element(By.XPATH,f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{cols}]').text
        data[head]=[]
            
    for i in range(2, req_rows + 1):
        if (i - 1) % 16 == 0:
            continue
        for col in range(2, 19):
            header = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[1]/th[{col}]').text
            value = driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[3]/table/tbody/tr[{i}]/td[{col + 1}]').text
            data[header].append(value)
    time.sleep(1)
    print("Your data is Scrap from Screener.in")

except Exception as e:
    print(e)
    time.sleep(1)
    print("NO COMPANIES")

finally:
    time.sleep(1)
    driver.close()
