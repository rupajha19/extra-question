a=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)