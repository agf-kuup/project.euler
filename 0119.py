pows=[]
for exp in range(2,10):
    for base in range(2,10000):
        pows.append(base**exp)
pows=list(set(pows))
pows.sort()
print(pows)
cont=0
sol=[]
for i in pows:
    s=sum(list(map(int,str(i))))
    for root in range(2,10):
        if s**root==i:
            sol.append(i)
            cont+=1
            break
    if cont==30:
        print(sol[29])
        break