f = open("Image-DataCollection\LinkSet.txt", "r")

dataList = ('\n'+f.read()).split("\n\n\n\n\n\n\n\n\n\n\n")[1:]

print("---->", len(dataList))
dataStampList = [x.split('\n') for x in dataList]
for i in dataStampList:
    print(i[0])

selectStamp = input("Jus' Get the TimeStamp yo:")
LinkSet = set()
for j in dataStampList:
    if selectStamp in j[0]:
        for k in j[1:]:
            if k!='':
                q_list = eval(k)
                if isinstance(q_list, list):
                    LinkSet.add(q_list[1])

print('---------->',len(LinkSet))
print(LinkSet)