from math import factorial as f
A=[0]*1000001
A[1]=1
A[2]=2
A[145]=1
A[69]=5
A[169]=3
A[871]=2
A[872]=2
A[78]=4
A[540]=2
def col(n):
    v=[n]
    sol=0
    while True:
        n=sum(list(map(lambda x: f(int(x)),str(n))))
        if n in v:
            break
        v.append(n)
        if n<1000001:
            if A[n]!=0:
                sol=A[n]
                break
    v=v[::-1]
    for i in range(len(v)):
        if v[i]<1000001:
            A[v[i]]=sol
        sol+=1
for i in range(3,1000001):
    col(i)
print(A.count(60))