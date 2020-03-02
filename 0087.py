#From the problem 0007
n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False

p2=list(filter(lambda x: x<50000000, list(map(lambda x: x**2,primes))))
p3=list(filter(lambda x: x<50000000, list(map(lambda x: x**3,primes))))
p4=list(filter(lambda x: x<50000000, list(map(lambda x: x**4,primes))))

print(len(set(list(filter(lambda x: x<50000000, [a+b+c for a in p2 for b in p3 for c in p4])))))