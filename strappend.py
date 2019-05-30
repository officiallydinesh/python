mylist=[]
str1=input()
mylist.extend(str1)
mylist.append(".")
for i in range(0,len(mylist)):
    print(mylist[i],end="")
