def add_lev(x):
    return set([(2*x+1)**2,(2*x)**2+1,(2*x+1)**2-2*x,(2*x)**2+1-2*x])
n=10000
era =[1] * n
primes=set([])
for p in range(2, n):
    if era[p]:
        primes.add(p)
        for i in range(p*p, n, p):
            era[i] = False
ratio=1
diags=set([1])
x=1
while ratio>.2:
    diags=diags.union(add_lev(x))
    x+=1
    print(diags)
    print(diags.intersection(primes))
    ratio=len(diags.intersection(primes))/len(diags)

print(ratio)
print((len(diags)+1)//2)