n,k=input().split(" ")
lis=[int(x) for x in input().split()]
sum = 0
for num in range(0,int(k)+1,1):
    sum = sum+num
print(sum)
