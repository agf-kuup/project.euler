n=10000
ans=0
########################### Start of prime factors ####################################
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        ans += p
        for i in range(p*p, n, p):
            era[i] = False
########################### Definition of sum of divisors of number####################
def sumdiv(t):
    s=t
    a=[]
    while t%2==0:
        a.append(2)
        t/=2
    for i in primes:
        if t<2 or t**.5<i:
            break
        else:
            while t%i==0:
                a.append(i)
                t//=i
    if t!=1:
        a.append(t)
    g=list(set(a))
    h=[]
    for n in range(len(g)):
        h.append(a.count(g[n])+1)
    e=1
    for c in range(len(h)):
        e*=int((g[c]**(h[c])-1)/(g[c]-1))
    return e-s
######################## Setting known data ############################################
amig=[]
L=[True]*n
L[0],L[1],L[6],L[28]=0,0,6,28
for i in range(len(primes)):
    p=primes[i]
    L[p]=1

###################################### Start of process #################################
for j in range(1,n):
    if L[j]==True:
        q=sumdiv(j)
        L[j]=q
        if q<n:
            if L[q]==j  and q!=j:
                amig.append(q)
                amig.append(j)
print(sum(amig))