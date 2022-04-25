# i=0
# while i<=20:
#     # i=i=1
#     if i==6 or i==8 or i==19 or i==20:
#         continue
#     # if i==8:
#     #     continue
#     # if i==19:
#     #     continue
#     # if i==20:
#     #     continue
#     i=i+1
#     print(i)


c_p=int(input("enter the c_p"))
s_p=int(input("enter the s_p"))
if c_p>s_p:
    print("profit",c_p-s_p)
elif c_p<s_p:
    print("loss",c_p-s_p)
else:
    print("nothing")