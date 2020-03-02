limit=2000000
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
primes=set(primes)
ans=[0,0]
cont=0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        f=lambda x: x*x+a*x+b
        tcont=0
        for i in range(1000):
            if f(i) not in primes:
                break
        if cont<i:
            ans=[a,b]
            cont=i
print(ans[0]*ans[1])
