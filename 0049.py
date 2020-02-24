from itertools import permutations 

n=10000
era =[1] * n
primes=set([])
for p in range(2, n):
    if era[p]:
        if p<10000 and p>999:
            primes.add(str(p))
        for i in range(p*p, n, p):
            era[i] = False
#Index of python starts in 0
#primes.remove("1487")
#primes.remove("4817")
#primes.remove("8147")
for i in primes:
    cand=set([''.join(p) for p in permutations(i)]).intersection(primes)
    primes=primes.difference(cand)
    if len(cand)>2:
        cand=list(map(int,cand))
        cand.sort()
        dif=0
        for i in range(1,len(cand)):
            d=cand[i]-cand[i-1]
            if d==dif:
                print(''.join([str(x) for x in cand[i-2:i+1]]))
                break
            dif=d