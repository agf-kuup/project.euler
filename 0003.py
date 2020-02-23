n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
q=600851475143
M=0
for i in primes:
    if q%i==0:
        q=int(q/i)
        M=i
print(max(q,M))