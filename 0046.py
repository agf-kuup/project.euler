n=10000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
odd=list(set([x+2*y*y for x in primes[1:] for y in range(1,10000)]).difference(primes))
odd.sort()
for i in range(33, 1000000,2):
    if i not in odd:
        if i not in primes:
            break
print(i)