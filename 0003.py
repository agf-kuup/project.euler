limit=1000000
A=[0 for i in range(limit)]
A[0]=1
A[1]=1
primes=[]
for i in range(3,limit+1,2):
    if A[i]==0:
        primes.append(i)
        for j in range(i,int(limit/i),2):
            if j%i==0:
                A[j]=1

q=600851475143
M=0
for i in primes:
    if q%i==0:
        q=int(q/i)
        M=i
print(max(q,M))