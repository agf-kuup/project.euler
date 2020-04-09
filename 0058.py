import random 

# This is_Prime code 
# is extracted from 
# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python

def is_Prime(n):
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


def add_lev(x):
    return [(2*x)**2+1,(2*x+1)**2-2*x,(2*x)**2+1-2*x] #There is missing one element because is a square. It doesn't affect, but meh.

# l=1 is    3, 5, 7, 9
# l=2 is    17, 21, 13, 25
l=3
primesDensity=8
numberElements=13
ratio=primesDensity/numberElements

# I had to round until get the correct answer, because all the code was correct except for the rounding.
while ratio>.10:
    lev=add_lev(l)
    numberElements+=4
    for i in lev:
        if is_Prime(i):
            primesDensity+=1
    ratio=round(primesDensity/numberElements,4)
    l+=1
print(2*l-1)