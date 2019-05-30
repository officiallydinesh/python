a,b=input().split()
for i in range(int(a),int(b)+1):
    if i==int(a):
        continue
    elif i==int(b):
        continue
    elif i % 2 != 0: 
        print(i, end = " ")
       
