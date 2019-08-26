sum=0
n=int(input())
while(n!=0):
    rem=n%10
    sum=sum+rem*rem
    n=n//10
print(sum)
