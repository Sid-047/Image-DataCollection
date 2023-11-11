print("Come On Start Entering the Search QueryKeyWords Yo!")
print("Press ctrl+c to Finish")

a = 0
q = []
while True:
    try:
        a+=1
        x = input("~"*a+">")
        for i in x.split('\n'):
            q.append(i)
    except:
        break

print(q)