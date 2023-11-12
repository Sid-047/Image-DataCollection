print("Come On Start Entering the Search QueryKeyWords Yo!")
print("Enter 'Exit' to Finish\n")

a = 0
q = []
while True:
    a+=1
    x = input()
    if x=='Exit':
        break
    else:
        if x!='':
            q.extend(x.split('\n'))

print("\n\nThe Search KeyWord Query List Yo!")
print(list(set(q)))