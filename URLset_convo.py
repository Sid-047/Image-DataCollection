f = open("N:\OpenSourceContribution\Image-DataCollection\LinkSet.txt", "r")

dataList = ('\n'+f.read()).split("\n\n\n\n\n\n\n\n\n\n\n")[1:]

print("---->", len(dataList))
dataStampList = [x.split('\n') for x in dataList]
for i in dataTimeList:
    print(i[0])

selectStamp = input("Jus' Get the TimeStamp yo:")
for j in dataStampList:
    if selectStamp==j[0]:
        print(j)