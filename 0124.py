from time import time
import operator

n=100000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False

Z=primes
zzz=time()
def factor(n):
    a=[]
    t=n
    if t%2==0:
        a.append(2)
        while t%2==0:
            t/=2
    if t in Z:
        a.append(t)
        return a
    else:
        for i in range(3,1+int(t**.5),2):
            if t%i==0:
                while t%i==0:
                    t/=i
                a.append(i)
            if t<2:
                break
        if t==1:
            return a
        else:
            a.append(t)
            return a
def prod(n):
    p=1
    for i in n:
        p*=i
    return p

x={}
for i in range(1,100001):
    x[i]=prod(factor(i))

sortx=sorted(x.items(), key=operator.itemgetter(1))
print(sortx[9999])
