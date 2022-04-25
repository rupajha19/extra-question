# armstrong number is that which sum of cube equal to its own digit.

num=int(input("enter any number::"))
i=num
sum=0
while i >0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if num==sum:
    print(num,"its armstrong number")
else:
    print(num,("its not armstrong number"))



