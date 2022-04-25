# which number is divisivle by 2 and its own number its called prime number)


num=int(input("enter any number::"))
counter=0
i=1
while i<=num:
    if num%i==0:
        counter=counter+1
    i=i+1
if counter==2:
    print(num,"its prime number::")
else:
    print(num,"its not prime number")  




    




