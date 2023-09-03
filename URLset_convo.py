f = open("N:\OpenSourceContribution\Image-DataCollection\LinkSet.txt", "r")

dataList = f.read().split("\n\n\n\n\n\n\n\n\n\n\n")[1:]

print("---->", len(dataList))
for i in dataList:
    x = i.split('\n')
    print(x[0])