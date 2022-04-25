# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

 

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

# def missingK(arr, k):
#   n = len(arr)
#   l = 0
#   u = n - 1
#   mid = 0
#   while(l <= u):
#     mid = (l + u)//2;
#     numbers_less_than_mid = arr[mid] - (mid + 1);
#     if(numbers_less_than_mid == k):
#         if(mid > 0 and (arr[mid - 1] - (mid)) == k):   
#         u = mid - 1;
#         continue;
       
#       # Else we return arr[mid] - 1.
#       return arr[mid]-1;
       
#     # Here we appropriately
#     # narrow down the search window.
#     if(numbers_less_than_mid < k):   
#       l = mid + 1;
#     elif(k < numbers_less_than_mid):
#       u = mid - 1;
 
#   # In case the upper limit is -ve
#   # it means the missing number set
#   # is 1,2,..,k and hence we directly return k.
#   if(u < 0):
#     return k;
   
#   # Else we find the residual count
#   # of numbers which we'd then add to
#   # arr[u] and get the missing kth number.
#   less = arr[u] - (u + 1);
#   k -= less;
   
#   # Return arr[u] + k
#   return arr[u] + k;
 
# # Driver Code
# if __name__=='__main__':
 
#     arr = [2,3,4,7,11];
#     k = 5;
   
#     # Function Call
#     # print("Missing kth number = "+ str(missingK(arr, k)))



# class Solution:
#     def twoSum(self, nums, target):
#         dic = []

        #A number can appear twice inside the same index, so I use a list
        # for i in xrange(0, len(nums)):
        #     try:
        #         dic[nums[i]].append(i)
        #     except:
        #         dic[nums[i]] = []
        #         dic[nums[i]].append(i)



'''
# num=int(input("enter the number"))
# if num>0:
#     print(num*1,"\n",num*2,"\n",num*3,"\n",num*4,"\n",num*5)
#     print(num*6,"\n",num*7,"\n",num*8,"\n",num*9,"\n",num*10)
# else:
#     print("not")



# i=39
# a=40
# while i>=30:
#     print(a-i)
#     i-=1


# import requests
# import json
# get_url=requests.get("https://api.merakilearn.org/courses")
# meraki_data=get_url.json()
# with open("course.json","w") as file_data:
#     json.dump(meraki_data,file_data,indent=4)
# read_data=open("course.json","r")
# read=read_data.read()
# data=json.loads(read)
# print()
# i=0
# while i<len(data):
#     print(str(i+1)+".",data[i]["name"],data[i]["id"])
#     i+=1
# coures_no=int(input("enter which course number you want::"))
# print(data[coures_no-1]["name"],data[coures_no-1]["id"])
# print()
# a=data[coures_no-1]["name"]+"_"+data[coures_no-1]["id"]+".json"
# get_url_2=requests.get("http://api.merakilearn.org/courses/"+data[coures_no-1]["id"]+"/exercises")
# meraki_data_2=get_url_2.json()
# with open(a,"w") as file_data_2:
#     json.dump(meraki_data_2,file_data_2,indent=4)
# r=open(a,"r")
# read=r.read()
# data=json.loads(read)
# i=0
# while i<len(data["course"]["exercises"]):
#     print(str(i+1)+".",data["course"]["exercises"][i]["name"])
#     i+=1
# topic=int(input("enter which topic you want::"))
# topic-=1
# i=0
# while i<len(data["course"]["exercises"][topic]["content"]):
#     print(data["course"]["exercises"][topic]["content"][i]["value"])
#     print()
#     i+=1
# while topic<=len(data["course"]["exercises"]):
#     p_n=input("enter which you want previous or next>>p/n::")
#     if p_n=="p": 
#         topic-=1
#         # continue
#         if p_n=="p" and topic>1:
#             print(data["course"]["exercises"][topic]["name"],"/n")
#             i=0
#             while i<len(data["course"]["exercises"][topic]["content"][i]["value"]):
#                 print(data["course"]["exercises"][topic]["content"]["value"])
#                 i+=1
#         else:
#             i=0
#             while i<len(data):
#                 print(str(i+1),data["course"]["exercises"][i]["name"])
#                 i+=1
#     elif p_n=="n":
#         topic+=1
#         # continue
#         if p_n=="n" and topic<len(data["course"]["exercises"]):
#             print(data["course"]["exercises"][topic]["name"],"/n")
#             i+=1
#             i=0
#             while i<len(data["course"]["exercises"][topic]["content"]):
#                 print(data["course"]["exercises"][topic]["content"][i]["value"])
#                 i+=1   
#             break
'''













# name=(input("enter any ing and ly word::"))
# if "ly " in  name:
#     print(name+"ing")
# elif "ing" in name:
#     print(name+"ly")
# else:
#     print("lying")


# x=5
# y=10
# a=(x is y) and (y is not x)
# print(a+a)




# a=True
# print(a**3)


# name=input("enter")
# if name=="ram":
#     print("fghjk")
# elif name=="pinky":
#     print("dxfcgvhbk")
# else:
#     print("werjk")
# if name=="ishu":
#     print("qwerthulk;")
# else:
#     print("dil")


# seed=int(input("enter the number"))
# if seed>1000:
#     print(seed%5)
# else:
#     print("discount nahi milega")    



# b=int(input("Enter salary......."))
# year_of_service=int(input("enter year of service....."))
# bonus=b*(10/100)
# if year_of_service>5:
#   print ("Bonus is",bonus+b)
# else:
#   print ("No bonus:", b)












# QUESTION



# what is request ?
# the request module allows you to send http request using python , the http request returns a response object with all the response data(content,encoding status etc.)


# 2) what is http & https?
# http= Hyper Text Transfer Protocol is a comunication protocol using sending and reciving webpage and files on the internet
# https=Hyper Text Transfer Protocol secure is communication over a computer and is widely used on the internet.

# 3) what is URL?
# URL= (uniform resorse locator ) is location of webpage or files on the internet.

# 4) what is API?
# API=(Application Progrramming interface)
# is a software intermedairy thats allows to talk two application to each other...

# 5) What is REST API?
# a restful application program interface that uses  http request to get ,put,post and delet data.

# 6) what is library ?
# library is a collection of module.

# 7) what is module?
# in python ,modules are simply files with "py" extension containing python code that can be imported inside another py0thon program.

# 8) what is Get and Post?






##if else logical question

# # cheacking num is positive or negative 
# num=int(input("enter any number:"))
# if num=="-":
#     print(num)
# else:
#     print(-num)


# check three digit number
# num=int(input("enter a num;"))
# if num>=100 and num<=999:
#     print("3 digit number")
# else:
#     print("not three digit")

# day=int(input("enter day number:"))
# if day>=1 and day<=5:
#     charge=2
#     print(day*charge)
# elif day>=6 and day<=10:
#     charge=3
#     print(day*charge)
# elif day>=11 and day<=15:
#     charge=4
#     print(day*charge)
# elif day>15 :
#     charge=5
#     print(day*charge)
# else:
#     print("invalid input")

# cheak strin present or not
# cheack=input("enter something:") 
# if "1" in cheack or "2" in cheack or"3" in cheack or "4" in cheack or "5" in cheack or "6" in cheack or"7" in cheack or "8" in cheack or "9" in cheack or "0" in cheack :
#     print("yes")
# else:
#     print("no")



# # second max
# n1=int(input("enter 1st num:"))
# n2=int(input("enter 2nd num:"))
# n3=int(input("enter 3rd num:"))
# if n1>=n2 and n1>n3:
#     print(n1,"and",n2,"are equal")
# if n1>=n3 and n1>n2:
#     print(n1,"and",n2 ,"are equal")
# if n2>n1 and n2>=n3:
#     print(n2,"and",n3,"are equal")
# if n3>n1 :
#     print(n3,"is greater")
# if n3>n2:
#     print(n3,"is greater")
# else:
    # print(n3,"is greatest")

# # ing and ly addition
# some=input("enter something:")
# if "ing" not in some:
#     print(some+"ing")
# elif "ing" in some:
#     print(some+"ly")
# name=input("enter your name:")
# lastname=input("enter last name:")
# print(lastname,"",name)
# 

# some =int(input("enter  something:"))
# a=some//10
# b=a%10
# if b==3:
#     print('yes')
# else:
#     print("no")









##loop logical question

# # first 10 evem numbers
# i=1
# while i <=20:
#     if i%2==0:
#         print(i)
#     else:
#         pass
#     i+=1

# # first 10 odd numbers
# i=1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     else:
#         pass
#     i+=1

# # print 10, 20, 30 … … 300
# i=1
# while i <=300:
#     if i%10==0:
#         print(i)
#     i+=1


# # print
# # 1 1
# # 2 4
# # 3 9...and so on
# i=1
# while i <=10:
#     print(i,i*i)
#     i+=1


# # table
# num=int(input("enter any num:"))
# i=1
# while i<=10:
#     print(num*i)
#     i+=1


# # armstrong number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3

#    temp //= 10
#    print(temp)

# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")



# sum=0
# i=0
# c=0
# while i<=10:
#     num=int(input("enter any number:"))
#     sum+=num
#     i+=1
#     c+=1
# print(sum/c)



# help(print);



# a=[1,2,3,4,6,2,1,4]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)


# user=input("enter any name:")
# i=1
# while i <=1:
#     print("'",user,"'")
#     i+=1


# # 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
# user=int(input("enter limit of series:"))
# a=str(2)
# i=1
# while i <=user:
#     print(a*i,end=",")
#     i+=1


# # 1 + 8 + 27 …………n terms
# user=int(input("enter limit:"))
# i=1
# while i<=user:
#     print(i**3,end="+")
#     i+=1


# # S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
# user=int(input("enter limit:"))
# i=1
# while i <=user:
#     a=i*i
#     if i%2==0:
#         print(a,end="-")
#     else:
#         print(a,end="+")
#     i+=1


# # 1 + 2 + 6 + 24 + 120 . . . . . n terms
# user=int(input("enter limit:"))
# i=1
# while i<=user:
#     j=1
#     print(i*i*j,end="+")
#     i+=1
#     j+=1


# # Write a program to print only odd numbers from the given list using a while loop . L = [23, 45, 32, 25, 46,
# # 33, 71, 90]
# L = [23, 45, 32, 25, 46,33, 71, 90]
# i=0
# while i<len(L):
#     if L[i]%2!=0:
#         print(L[i])
#     i+=1
    


# # Write a program to print all the factors of a number using a while loop .
# user=int(input("enter any number to cheack factors:"))
# i=1
# while i <user:
#     if user%i==0:
#         print("factors of ",user,"is",i)
#     i+=1
    

# # Accept two numbers from the user and display sum of even numbers between them(including both)
# user1=int(input("enter start number:"))
# user2=int(input("enter end number:"))
# i=user1
# sum=0
# while i <=user2:
#     if user1%2==0:
#         sum+=i
#     user1+=1
#     i+=1
# print(sum)


# # Write a program to print the factorial of a number.
# user=int(input("enter any number:"))
# i=1
# factorial=1
# while i<=user:
#     factorial*=user
#     i+=1
#     user-=1
# print(factorial)   



# for i in (1,2,3):
#     print(i)

# for i in (2,3,4):
#     print(i)

# for i in (4,3,2,1,0):
#     print(i, end=" ")

# for i in range(10):
#     if(i%2!=0):
#         print("Hello",i)


# for i in range(10,2,-2):
#     print(i, "Hello")


# str = "Python Output based Questions"
# word=str.split()
# for i in word:
#     print(i)


# for i in range(7,10):
#     print("Python Output based Questions*")
# print("Python Output based Questions")

# for i in range(7,-2,-9):
#     print(i)
#     for j in range(i):
#         print(j)


# i="9"
# for k in i:
#     print(k)


# for i in range(1,8):
#     print(i)
# i+=2


# for i in range(4,7):
#     i=i+1
# print("Hello")

# i=4
# while(i<10):
#     i=i+3
#     print(i)


# for i in range(20):
#     if i//4==0:
#         print(i,"0")
#     print(i)


# print(5//4)


# x=1234
# while x%10:
    # x=x//10
# print(x)



# for i in 1,2,3:
#     print(i*i)

# for i in 2,4,6:
#     print("H"*i)


# p=10
# q=20     
# p=p*q//4
# q=p+q**3
# print(p,q)


# x=2
# y=6
# x=x+y/2 + y//4
# print(x)

# L = [13 , 12 , 21 , 16 , 35 , 7, 4]
# s = 5
# s1 = 3
# for i in L:
#     if (i % 4 == 0):
#         s = s + i
#         continue
#     if (i % 7 == 0):
#         s1 = s1 + i
# print(s , end=" ")
# print(s1)


# print('cs' + 'ip' if '234'.isdigit() else 'IT' + '-402')

## nested loop


  
# 0
# 11
# 222
# 3333
# 44444

# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(i,end="")
#     print()

# 0
# 01
# 012
# 0123
# 01234

# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(j,end="")
#     print()



# 0
# 01
# 012
# 0123
# 01234
# 0123
# 123
# 23
# 3
# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(j,end="")
#     print()
# for i in range(5):
#     for j in range(4):
#         if i<=j:
#             print(j,end="")
    # print()

# *
# **
# ***
# ****
# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,5):
#         print(j,end=" ")
#     for j in range(i+1):
#         print(j,end=" ")
#     print()


# 0
# 12
# 234
# 3456
# 45678
# for i in range(5):
#     for j in range(i+1):
#         print(j+i,end="")
#     print()

# 00000
# 1111
# 222
# 33
# 4
# for i in range(5):
#     for j in range(5-i):
#         print(i,end="")
#     print()   


# 1
# 44
# 999
# # 16161616
# for i in range(5):
#     for j in range(i):
#         print(i*i,end="")
#     print() 




##operators

# converting 12hours to 24 hours
# a="12hours"
# b=a[0:2]
# b=int(b)
# c=a[2:8]
# print(str((b*2))+c)

# a="12hours"
# print(str(12+12)+"hourse")


##loop
##using decreament
# a = 1
# while a !=11:
#     print (a)
#     a-=-1

#dry run
# a=1   while a!=11   print(a)   a=a-(-1)=1
# a=1    1!=11         1         a=1-(-1)=2
# a=2    2!=11         2         a=2-(-1)=3
# a=3    3!=11         3         a=3-(-1)=4
# a=4
# .
# .
# a=11   11!=11       F



##decrement ques

# a = 1 
# while a <= 10:
#     print (a)
#     a = a-(-1)

#dry run
# a=1   while a<=10  print(a)   a=a-(-1)
# a=1     1<=10       1         a=1-(-1)=2
# a=2     2<=10       2         a=2-(-1)=3
# a=3     3<=10       3         a=3-(-1)=4
# a=4     4<=10       4         a=4-(-1)=5
# a=5     5<=10       5         a=5-(-1)=6
# a=6     6<=10       6         a=6-(-1)=7
# .
# .
# a=11   11<=10       F


