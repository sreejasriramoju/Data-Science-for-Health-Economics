from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.support.select import Select

ind=38
t=1
state = 'West Bengal'
#Open browser
row=4
templist = []
Table_dict = {'State': 'State',
                'District' : 'District',
                'TBUnit': 'TBUnit',
                'PHI Code': 'Code',
                'PHI Name': 'Name',
                'Microscopy': 'Microscopy',
                'Cbnaat': 'Cbnaat'
                }
templist.append(Table_dict)
df = pd.DataFrame(templist)
while(1):
    driver = webdriver.Chrome(executable_path="C://Users//sreej//OneDrive//Documents//drivers//chromedriver.exe")
    driver.get("https://reports.nikshay.in/Reports/PhiDirectory")
    #####select state
    driver.find_element(By.ID, "State").send_keys(state)
    time.sleep(2)
    #####select district
    dropdown_dis =Select(driver.find_element(By.ID,"District"))
    dropdown_dis.select_by_index(ind)
    time.sleep(1.5)
    dropdown_tu =Select(driver.find_element(By.ID,"Tu"))
    try:
        
        #####select unit
        dropdown_tu.select_by_index(t)
        time.sleep(1.5)
        #click get data button
        element = driver.find_element_by_css_selector('#aOverviewData')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        ########data extraction
        row=4
        templist = []
        while(1):
            try:
                State = 'West Bengal'
                District = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[2]/td/b").text
                print(District)
                TBUnit = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[3]/td/b").text
                print(TBUnit)
                Code = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[" + str(row) + "]/td[1]").text
                Name = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[" + str(row) + "]/td[2]").text
                print(s)
                try:
                    driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[" + str(row) + "]/td[3]/i")
                    Microscopy=1
                except NoSuchElementException:
                    Microscopy=0
                try:
                    driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div/div[6]/table/tbody/tr[" + str(row) + "]/td[4]/i")
                    Cbnaat=1
                except NoSuchElementException:
                    Cbnaat=0
                
                Table_dict = {'State': State,
                        'District' : District,
                        'TBUnit': TBUnit,
                        'PHI Code': Code,
                        'PHI Name':Name,
                        'Microscopy': Microscopy,
                        'Cbnaat': Cbnaat
                        }
                templist.append(Table_dict)
                df = pd.DataFrame(templist)
                row = row + 1

            # if there are no more table data to scrape
            except NoSuchElementException:
                print('broke')
                break
        
        if row>4:
            df.to_csv("C://Users//sreej//Downloads//Rampurhat_tbu.csv", mode='a', index=False, header=False)
        driver.close()
        t=t+1
    except NoSuchElementException:
        print('nnnnn')
        break 