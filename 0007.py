n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
#Index of python starts in 0
print(primes[10000])