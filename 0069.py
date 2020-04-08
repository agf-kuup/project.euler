# We know that the euler phi function is calculated basing on that if
# 
# n= p1^a1 * p2^a2 * ... * pk^ak
# 
# Then phi(n)= X[pi^(ai-1)]* X[pi-1]  (The X is the product from 1 to k)
# 
# Then if we want to get the max value for n/phi(n), then we must only use
# free square n's.
# 
# This means that n=p1*p2*...pk
# 
# So the equation will become
# 
#    p1     p2            pk
#   ---- * ---- * .... * ----
#   p1-1   p2-1          pk-1 
# 
# Generating this way the max number, since we're multiplicating numbers greater than 1.
# 
# So the way to get the max quotient is getting the max number of primes such that multiplied
# generates the biggest number smaller than 1000000. So we must get the smallest primes and multiply
# until get a number that limits with 1000000

n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
#Index of python starts in 0

t=1
while t<1000000:
    v=primes.pop(0)
    t*=v
print(t//v)