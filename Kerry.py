from selenium import webdriver
import os
from bs4 import BeautifulSoup
import pyautogui as pg

def Get_data_by_tracking(tracking_number,driver):
    driver.get("https://th.kerryexpress.com/th/track/")
    res = {}
    try:
        import time
        time.sleep(4)
        print('ok')

        
        inputElement = driver.find_element_by_xpath('/html/body/kett-root/kett-search-form/div/div/div/form/div/div[1]/input')
        inputElement.click()
        time.sleep(0.5)
        pg.write(tracking_number,interval=0.2)
        button = driver.find_element_by_class_name('ke-btn-search').click()
        time.sleep(2)
        # try:
        #     data = driver.find_element_by_xpath('/html/body/div[3]/div')
        #     คาดว่าจะถึงวันที่ = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]')
        #     ผู้ส่ง = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[4]')
        #     ผู้รับ = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[5]')
            
        #     soup = BeautifulSoup(data.get_attribute('innerHTML'),features="lxml")
        #     date = soup.findAll("div", {"class": "date"})
        #     description = soup.findAll("div", {"class": "d1"})
        #     location = soup.findAll("div", {"class": "d2"})
            
        #     res['คาดว่าจะถึงวันที่'] = คาดว่าจะถึงวันที่.text.replace("คาดว่าจะถึงวันที่: ","")
        #     res['ผู้ส่ง'] = ผู้ส่ง.text.replace("ผู้ส่ง: ","")
        #     res['ผู้รับ'] = ผู้รับ.text.replace("ผู้รับ: ","")
            
        #     date_clean = []
        #     time_clean = []
        #     for i in date:
        #         r = i.text.replace("\n","").split("Time")
        #         date_clean.append(r[0])
        #         time_clean.append(r[1])
                
        #     description_clean = [i.text.split("\n")[1].strip() for i in description]
        #     location_clean = [i.text for i in location]
        #     info = []
        #     for date,time,des,location in zip(date_clean,time_clean,description_clean,location_clean):
        #         r = { "date" : date ,
        #             "time":time ,
        #             "description" : des ,
        #             "location" : location}
                
        #         info.append(r)
            
        #     res["info"] = info
        #     return res
        # except :
        #     return "Shipment Not Found!"

        try:
            # data = driver.find_element_by_xpath('//*[@id="preview_content"]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[4]/div[3]/li[1]/div[2]/div[1]/span[1]/span')
            data = driver.find_element_by_xpath('//*[@id="preview_content"]/kett-tracking/kett-tracking-search/div[2]/kett-tracking-item/div/div/div[4]/div[3]')
            soup = BeautifulSoup(data.get_attribute('innerHTML'),'html.parser')
            
            return soup

        except:
            return "Shipment Not Found!"

    
    except:
        return "server not ready Please try agian"
        
        

#TEST
path = "C:\webdrivers\chromedriver.exe"

if __name__ == '__main__':

    driver = webdriver.Chrome(path)
    r = Get_data_by_tracking(tracking_number="TNKS000014143NN",driver=driver)
    print(r)