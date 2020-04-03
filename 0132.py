# First try was to obtain the factors throught factoring the numbers R(n) such that n|10**9
# But the size of the numbers were very big.
# Then the attempt to do the equation 10**(10**9)=1 mod(9*p) was done, but it wasn't possible
# So I did the function ppow to avoid very huge numbers. The solution was achieved with this method. 
n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False    

X=list(bin(1000000000)[2:])
X.reverse()
print("+++++++++++++",X)
t=[]

def ppow(p):
    allP=[10]
    for i in range(len(X)):
        allP.append((allP[i]**2)%(9*p))
    s=1
    for i in range(len(X)):
        if X[i]=='1':
            s*=allP[i]
            s%=9*p
    if p==11:
        print(s)
    return(s)

for i in primes:
    if ppow(i)==1:
        t.append(i)
        print(t)
    if len(t)==40:
        break
print(sum(t))
print(t)