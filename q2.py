# list=[1,2,3,4,5,6,7]
# # [12,34,56]
# i=0
# empty_list=[]
# while i<len(list):
#     j=1
#     while j<i+2:
#         b=str(list[i])+str(list[j])
#         empty_list.append(str(b)
#         j=+2
#     i=+2
# print(empty_list)




# class Acc:
#     def __init__(self,id):
#         self.id=id
#         id=555
# acc=Acc(111)
# print(acc.id)

    
# count=1
# def doThis():
#     global count
# for i in (1,2,3):
#     count+=1
# doThis()
# print(count)


# counter={}
# def addToCounter(country):
#     if country in counter:
#         counter[country]+=1
#     else:
#         counter[country]=1
# addToCounter('China')
# addToCounter('japan')
# addToCounter('china')
# print(len(counter))




# def addToList(listcontainer):
#     listcontainer+=[10]
# mylistContainer=[10,20,30,40]
# addToList(mylistContainer)
# print(len(mylistContainer))


# check1=['Learn','Quiz','Practice','Contribute']
# check2=check1
# check3=check1[:]
# check2[0]='Code'
# check3[1]='Mcq'
# count=0
# for c in (check1,check2,check3):
#     if c[0]=='Code':
#         count+=1
#     if c[1]=='Mcq':
#         count+=10
        # print(count)

# nameList=['Harsh','Pratik','Bob','Dhruv']
# print(nameList[1][-1])


# dictionary={}
# dictionary[1]=1
# dictionary['1']=2
# dictionary[1]+=1
# sum=0
# for k in dictionary:
#     sum+=dictionary[k]
# print(sum)



# r=lambda q:q*2
# s=lambda q:q*3
# x=2
# x=r(x)
# x=s(x)
# s=r(x)
# print(x)