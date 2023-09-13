from colorama import Fore,Style

f = open("Image-DataCollection\Scraped_LinkSet.txt", "r")
dataList = ('\n'+f.read()).split("\n\n\n\n\n\n\n\n\n\n\n")[1:]
f.close()

print("---->", len(dataList))

if len(dataList)==0:
    print(Fore.RED+Style.BRIGHT+"Scrap some Image URLs Yo !"+Fore.RESET)
    print("There's Nothing in Here")
else:
    dataStampList = [x.split('\n') for x in dataList]
    for i in dataStampList:
        print(Fore.BLUE+Style.BRIGHT+i[0]+'/n'+Fore.RESET)

    selectStamp = input("Jus' Get the TimeStamp yo:")
    LinkSet = set()
    for j in dataStampList:
        if selectStamp in j[0]:
            for k in j[1:]:
                if k!='':
                    q_list = eval(k)
                    if isinstance(q_list, list):
                        LinkSet.add(q_list[1])

    print(Fore.CYAN+Style.BRIGHT+'URL Count ---------->'+Fore.RESET+str(len(LinkSet)))

    f = open("Image-DataCollection\DownURLs_set.txt", "w")
    f.write(str(LinkSet))
    f.close()
    print("LinkSet's fed to DownURLs_set.txt File Yo!")