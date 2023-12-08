import io
import os
import time
import glob
import requests
import datetime
import threading
from PIL import Image
from selenium import webdriver
from colorama import Fore,Style
from selenium.webdriver.common.by import By

imgLabel = 0
queryPos = -1
imgSet = set()
imgTempVal = 0
t1 = time.time()
driver = webdriver.Firefox()
q = ['<Search Keyword Query>', '<Search Keyword Query>', '<Search Keyword Query>', '<Get some More Queries On!>']
f = open("Scraped_LinkSet.txt", "a")
f.write("\n\n\n\n\n\n\n\n\n\n")
f.write(str(datetime.datetime.now())+'\n')
f.close()
for q_ in q:
    skip = 0
    max_ = 150
    queryPos+=1
    imgTempVal = 1
    imgTemp = set()
    driver.get("https://www.google.com/search?q={}&tbm=isch&source=hp&biw=1873&bih=969&ei=jX1tY83SF87az7sPwKO68AY&iflsig=AJiK0e8AAAAAY22LnaUQStNMEm2fk8dCGptfVOdHqY1D&ved=0ahUKEwiNzZqI16T7AhVO7XMBHcCRDm4Q4dUDCAc&uact=5&oq=cat&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQ6CAgAELEDEIMBUABYrQFgvgdoAHAAeACAAU-IAewBkgEBM5gBAKABAaoBC2d3cy13aXotaW1n&sclient=img".format(q_))
    while len(imgTemp)<max_:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        if skip>100:
            break
        picSelect = 0
        try:
            comPics = driver.find_elements(By.CLASS_NAME,"Q4LuWd")
            for img in comPics[len(imgTemp)+skip:max_]:
                picSelect+=1
                if picSelect%10==0:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(3)
                if skip>100:
                    break
                img.click()
                time.sleep(1)
                orgPics = driver.find_elements(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]")
                try:
                    morePics_btn = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input")
                    morePics_btn.click()
                    time.sleep(1)
                    print(Fore.RED+Style.BRIGHT+"~~~Yoooooo !"+Fore.RESET)
                except:
                    pass
                for pic in orgPics:
                    if pic.get_attribute('src') in imgTemp or 'encrypted' in pic.get_attribute('src'):
                        print(Fore.YELLOW+Style.BRIGHT+pic.get_attribute('src')+Fore.RESET)
                        skip+=1
                        max_+=1
                        break
                    if 'http' in pic.get_attribute('src') and 'encrypted' not in pic.get_attribute('src') and pic.get_attribute('src') not in imgTemp:
                        x = len(imgSet)+queryPos*imgTempVal
                        y = len(imgTemp)+queryPos*imgTempVal
                        imgTemp.add(pic.get_attribute('src'))
                        print(Fore.BLUE+Style.BRIGHT+"\tScrapped Img{}~Img{} Url...".format(str(x+y),str(y))+Fore.RESET)
                        print(Fore.GREEN+Style.BRIGHT+pic.get_attribute('src')+Fore.RESET)
                        q_ = q_.replace(" ", "_")
                        f = open("Scraped_LinkSet.txt", "a")
                        f.write(str(list([q_, pic.get_attribute('src')]))+"\n")
                        f.close()
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            pass
        imgTempVal = len(imgTemp)
        imgSet = imgSet.union(imgTemp)
        break

t2 = time.time()
print("\n\n\nFetchingExecTime:", t2-t1)

if not os.path.isdir("imgSet"):
   os.makedirs("imgSet")
else:
    fileList = []
    os.chdir("imgSet")
    imgFiles = glob.glob("*.png")
    if len(imgFiles)==0:
        for i in imgFiles:
            try:
                fileList.append(int(i.split(".")[0] ))
            except:
                pass
        imgLabel = max(fileList)+1

t1 = time.time()
def saving(imgDown):
    try:
        global imgLabel
        t1_ = time.time()
        r = requests.get(imgDown).content
        f = io.BytesIO(r)
        imgf = Image.open(f)
        imgf.save("imgSet/"+str(imgLabel)+'.png')
        t2_ = time.time()
        if imgLabel%2==0:
            print(Fore.MAGENTA+Style.BRIGHT+str(imgLabel)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs'+Fore.RESET)
        else:
            print(Fore.CYAN+Style.BRIGHT+'\t\t'+str(imgLabel)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs'+Fore.RESET)
        imgLabel+=1
    except:
        print(Fore.RED+Style.BRIGHT+"~~~| "+str(i)+Fore.RESET)
        pass

for i in imgSet:
    ThreadObj = threading.Thread(target=saving, args =(i,))
    ThreadObj.start()
    ThreadObj.join(timeout=60)
              
t2 = time.time()
print("\n\n\nWritingExecTime:", t2-t1)