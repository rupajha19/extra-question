n=int(input("enter row::"))
i=0
while n >0:
    b=1
    while b<i:
        print(" ",end="")
        b+=1
    j=1
    while j<(n*2)-1:
        print(j,end="")
        j+=1
    print()
    n-=1
    i+=1

