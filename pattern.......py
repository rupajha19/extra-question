
#                1
        #       121
        #      12321
        #     1234321
        #    123454321 

i=0
while i<=5:
    print(" "*(4-i),end="")
    j=0
    while j-1<i*2:
        if j+1>i+1:
            print((i*2)-j+1,end="")
        else:
            print(j+1,end="")
        j+=1
    print()
    i+=1



# no_rows=int(input("enter:"))

# for row in range(1,no_rows+1):
#     for column in range(1,row+1):
#         print("*",end="")
#     print()


# for row in range(no_rows-1,0,-1):
#     for column in range(1,row+1):
#         print("*",end="")
#     print()





