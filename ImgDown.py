import io
import os
import time
import glob
import requests
import threading
from PIL import Image
from colorama import Fore,Style


t1=time.time()
imgDown=0
f=open("txtStuff/DownURLs_set.txt","r")
s=f.read()
imgSet=eval(s)

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
        if len(fileList)==0:
            imgLabel = 0
        else:
            imgLabel = max(fileList)+1

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

t2=time.time()
print("\n\n\nWritingExecTime:", t2-t1)