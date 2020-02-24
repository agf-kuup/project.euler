n=5000000
era =[1] * n
primes=[0]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
def basic_filter(n):
    s=str(n)
    if s[0] in "14689" or s[-1] in "14689":
        return False
    if len(set(s[1:-1]).intersection(set(["2","4","5","6","8","0"])))!=0:
        return False
    else: return n
A=set(list(map(basic_filter,primes)))
ans=[]
for i in A:
    n=i
    m=i
    test=True
    while n!=0:
        if n//10 not in primes:
            test=False
            break
        n//=10
    p=10
    while m!=0:
        if m%(10**p) not in primes:
            test=False
            break
        m%=10**p
        p-=1
    if test==True:
        ans.append(i)
print(sum(ans)-17)
print(len(ans)-5)