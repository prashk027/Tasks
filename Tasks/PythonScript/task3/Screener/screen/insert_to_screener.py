import psycopg2
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to use enter 
import login_screener 
import time
from extract_excel import data_50

data = {}

driver = login_screener.login()

def delete_comp():
    driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/a").click()
    delete_each_comp()

def delete_each_comp():
    ul = driver.find_elements(By.XPATH,"/html/body/main/div[2]/div[2]/ul/li")

    total_comp = len(ul)
    is_not_zero = True

    while is_not_zero:
        if total_comp == 0:
            is_not_zero = False
        else:
            for _ in range(total_comp):
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/ul/li[1]/button/i").click()
                time.sleep(1)
            break
        total_comp = len(driver.find_elements(By.XPATH,"/html/body/main/div[2]/div[2]/ul/li"))

def extract_watch():
    tr_rows = driver.find_elements(By.XPATH,"/html/body/main/div[3]/div[3]/table/tbody/tr")
    req_rows = len(tr_rows)
    print(req_rows)
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

def insert_to_psql() -> None:
    try:
        conn = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password="mypass",port=5431)
        cur = conn.cursor()
        cols = [col.replace(" ",'_') for col,_ in data.items()]
        cols = [col.replace('%','PERCENT') for col in cols]
        cols = [col.replace('.','') for col in cols]
        cols = [col.replace('/','BY') for col in cols]
        rows = [v for _,v in data.items()]
        cur.execute("select name from stocks")
        conn.commit()
        company_name = []
        for i in cur.fetchall():
            company_name.append(i[0])

        row_data = []
        li =[]

        for row in range(len(rows)):
            for col in range(len(rows[row])):
                for r in range(len(rows)):
                    if rows[r][col] == '':
                        li.append(0)
                        continue
                    li.append(rows[r][col])
                row_data.append(li)
                li=[]
            break
        
        for row in row_data:
            if row[0] not in company_name:
                print(row[0])
                cur.execute(f"""
                    insert into stocks ({', '.join(cols)})
                    values ({', '.join(['%s'] * len(cols))})
                """,row)
                conn.commit()
                print("Inserted into stocks table.")
            

    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()

# Main code
try:
    driver.find_element(By.XPATH,"/html/body/div/div[2]/main/div[1]/div[2]/a[2]").click()
    delete_comp()
       
    for el in data_50:
        driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div[2]/a[2]").click()
        input = driver.find_element(By.XPATH,"/html/body/main/div[3]/form/div/textarea")

        for co in range(len(el)):
            input.send_keys([f"{el[co]}\n"])
        driver.find_element(By.XPATH,"/html/body/main/div[3]/form/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/main/div[2]/form/button").click()
        extract_watch()
        insert_to_psql()
        delete_comp()

    print("Added from Excel")
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    driver.close()