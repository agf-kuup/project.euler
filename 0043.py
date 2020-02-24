p17=["017","034","051","068","085"]
dig=[str(i) for i in range(10)]
for i in range(1,1000//17+1):
    m=str(17*i)
    if len(set(m))==3:
        p17.append(m)
p13=[]
for i in p17:
    for j in dig:
        d8d10=j+i[:2]
        if len(set(i+j))==4 and int(d8d10)%13==0:
            p13.append(j+i)
p11=[]
for i in p13:
    for j in dig:
        d7d9=j+i[:2]
        if len(set(i+j))==5 and int(d7d9)%11==0:
            p11.append(j+i)
p7=[]
for i in p11:
    for j in dig:
        d6d8=j+i[:2]
        if len(set(i+j))==6 and int(d6d8)%7==0:
            p7.append(j+i)
p5=[]
for i in p7:
    for j in dig:
        d5d7=j+i[:2]
        if len(set(i+j))==7 and int(d5d7)%5==0:
            p5.append(j+i)
p3=[]
for i in p5:
    for j in dig:
        d4d6=j+i[:2]
        if len(set(i+j))==8 and int(d4d6)%3==0:
            p3.append(j+i)
p2=[]
for i in p3:
    for j in dig:
        d3d5=j+i[:2]
        if len(set(i+j))==9 and int(d3d5)%2==0:
            p2.append(j+i)
sol=[]
for i in p2:
    for j in dig[1:]:
        d=j+i
        if len(set(d))==10:
            sol.append(int(d))
print(sum(sol))