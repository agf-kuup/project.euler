import numpy as np

n=100 # I tried to verify if it was correct for the small numbers, but the solution was shorter than expected
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False

t=np.poly1d([1])
for i in primes:
    coefs=[0 for z in range(n+1)]
    for j in range(n+1):
        if (j)%i==0:
            coefs[j]=1
    t*=np.poly1d(coefs[::-1])
v=0
while t.coef[v]<5000:
    v+=1
print(t.coef[v],v)