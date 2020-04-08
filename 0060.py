import random

# Extracted from https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python

def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

n=20000
era =[1] * n
ps=[]
for p in range(2, n):
    if era[p]:
        ps.append(p)
        for i in range(p*p, n, p):
            era[i] = False

def combs(a,b):
    x=int(str(a)+str(b))
    y=int(str(b)+str(a))
    if is_Prime(x) and is_Prime(y):
        return True

S=set(list(map(str,ps)))
flag=0
n=len(ps)
for p1 in range(n):
    for p2 in range(p1+1,n):
        if combs(ps[p1],ps[p2]):
            for p3 in range(p2+1,n):
                if combs(ps[p1],ps[p3]) and combs(ps[p2],ps[p3]):
                    for p4 in range(p3+1,n):
                        if combs(ps[p3],ps[p4]) and combs(ps[p4],ps[p2]) and combs(ps[p1],ps[p4]):
                            for p5 in range(p4+1,n):
                                if combs(ps[p1],ps[p5]) and combs(ps[p2],ps[p5]) and combs(ps[p3],ps[p5]) and combs(ps[p4],ps[p5]):  
                                    print(ps[p1],ps[p2],ps[p3],ps[p4],ps[p5], ps[p1]+ps[p2]+ps[p3]+ps[p4]+ps[p5])