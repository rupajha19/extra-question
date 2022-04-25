a="my name is rupa"
i=0
count=0
while i<len(a):
    count=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    print(a[i],"=", count)
    i=i+1 


