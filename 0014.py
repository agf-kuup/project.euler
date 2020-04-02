A=[0]*1000001
A[13]=10
A[40]=9
A[20]=8
A[10]=7
A[5]=6
A[16]=5
A[8]=4
A[4]=3
A[2]=2
A[1]=1

def col(n):
    v=[n]
    sol=0
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        v.append(n)
        if n<1000001:
            if A[n]!=0:
                sol=A[n]
    v=v[::-1]
    for i in range(len(v)):
        if v[i]<1000001:
            A[v[i]]=sol
        sol+=1

for i in range(3,1000000):
    col(i)
print(A.index(max(A)))