# I had to re-read because p1<10**7, but p2 not, so I have to get
# the next prime after 10**7 (that is 10**7+3)

n=1000004
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
primes.remove(2)
primes.remove(3)


def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=int(a// b)
        a, b= b, a%b
        x0, x1=int(x1 -q *x0), int(x0)
    if x1<0 : x1+= b0
    return int(x1)

s=0
for i in range(1,len(primes)):
    p1=primes[i-1]
    p2=primes[i]
    v=10**(len(str(p1)))
    vv=mul_inv(v,p2)
    # print(((vv*(p2-p1))%p2)*v+p1)
    s+=((vv*(p2-p1))%p2)*v+p1
    # print(s,p1,p2)
print(s)
print(primes[-1])