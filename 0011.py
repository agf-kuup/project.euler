
n=1000000
ans=0
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        ans += p
        for i in range(p*p, n, p):
            era[i] = False

def factor(n):
    num=1
    while n!=1:
        if 
        
for i in range(10000):
    