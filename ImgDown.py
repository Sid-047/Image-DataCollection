import io
import time
import requests
import datetime
import threading
from PIL import Image
from colorama import Fore,Style


t1=time.time()
a=0
f=open("New_LinkLinkSet.txt","r")
s=f.read()
imgSet=eval(s)

t1=time.time()
def saving(img_):
    try:
        global a
        t1_=time.time()
        r=requests.get(img_).content
        f=io.BytesIO(r)
        imgf=Image.open(f)
        imgf.save("ImgSet/"+str(a)+'.png')
        t2_=time.time()
        if a%2==0:
            print(Fore.MAGENTA+Style.BRIGHT+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        else:
            print(Fore.CYAN+Style.BRIGHT+'\t\t'+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        a+=1
    except:
        print(Fore.RED+Style.BRIGHT+"~~~|",i)
        pass

for i in imgSet:
    ThreadObj=threading.Thread(target=saving,args=(i,))
    ThreadObj.start()
    ThreadObj.join(timeout=60)
              
t2=time.time()
print("\n\n\nExecTime:", t2-t1)

