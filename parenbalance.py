openlst=[]
closelst=[]
string=input()
mylist=list(string) 
for i in mylist:
    if i=='(':
        openlst.append("(")
    else:
        closelst.append(")")
if len(openlst)==len(closelst):
    print("yes")
else:
    print("no")
