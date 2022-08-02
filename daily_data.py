from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
from datetime import timedelta

dt = 0
Begin = "2020/05/01"
End = "2020/05/01"
Begin = datetime.strptime(Begin, "%Y/%m/%d")
End = datetime.strptime(End, "%Y/%m/%d")
for dt in range(250):
    FromDate = Begin + timedelta(days=dt)
    ToDate = End + timedelta(days=dt)
    SDate = FromDate.strftime('%d/%m/%Y')
    EDate = ToDate.strftime('%d/%m/%Y')

    driver = webdriver.Chrome(executable_path="C://Users//sreej//Downloads//chromedriver_win32 (1)//chromedriver.exe")
    driver.get("https://reports.nikshay.in/Reports/TBNotification")
    driver.maximize_window()

    ##Select from date
    d=driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/div[1]/div/input")
    driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)
    driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/div[1]/div/input').clear()
    d.send_keys(SDate)
    d.send_keys(Keys.RETURN)
    time.sleep(2)
    
    ##Select to date
    d=driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/div[2]/div/input")
    driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)
    driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/div[2]/div/input').clear()
    d.send_keys(EDate)
    d.send_keys(Keys.RETURN)
    time.sleep(2)
    
    ##Select get data button
    element = driver.find_element_by_css_selector('#StateData > div.row > div:nth-child(1) > div > form > div > div.button_top > a')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)
    index=3
    index_district=3
    while(1):
        element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(index) + "]/td[1]/a")
        print(element.text)
        print(SDate)    
        if element.text=='West Bengal':
            driver.execute_script("arguments[0].click();", element)
            #state
            time.sleep(2)
            try:
                element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/table/tbody/tr[" + str(index_district) + "]/td[1]/a")
                print(element.text) 
                if element.text=='Uttar Dinajpur':
                    print(index_district)
                    driver.execute_script("arguments[0].click();", element)
                    #District
                    time.sleep(2)
                    ##################################

                    row = 3
                    templist = []
                    while (1):
                        try:
                            State = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(index) + "]/td[1]/a").text
                            District = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/table/tbody/tr[" + str(index_district) + "]/td[1]/a").text
                            SDate=SDate
                            EDate = EDate
                            TBUnit = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/table/tbody/tr[" + str(row) + "]/td[1]").text
                            Public_Notif = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/table/tbody/tr[" + str(row) + "]/td[2]").text
                            Private_Notif = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/table/tbody/tr[" + str(row) + "]/td[3]").text

                            Table_dict = {'State': State,
                                    'District' : District,
                                    'SDate': SDate,
                                    'EDate': EDate,
                                    'TBUnit': TBUnit,
                                    'Public_Notif': Public_Notif,
                                    'Private_Notif': Private_Notif
                                    }
                            templist.append(Table_dict)
                            df = pd.DataFrame(templist)
                            row = row + 1

                        # if there are no more table data to scrape
                        except NoSuchElementException:
                            break

                    df.to_csv("C://Users//sreej//Downloads//Uttar Dinajpur.csv", mode='a', index=False, header=False)
                    driver.close()
                    #dt = dt + 1
                    break 
                else :
                    index_district=index_district+1
            except NoSuchElementException:
                            break 
        else :
            index=index+1
                