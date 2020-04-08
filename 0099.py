from math import log
A=open("0099_base_exp.txt","r")
ans=0
m=0
t=1
for lines in A.readlines():
    x=list(map(int,lines.split(",")))
    if m<log(x[0])*x[1]:
        ans=t
        m=log(x[0])*x[1]
    t+=1
print(ans)