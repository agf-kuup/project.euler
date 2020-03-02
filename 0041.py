#No puede ser más grande o sería divisible entre 3, (1+2+...+9=45 y 45%9=0)
n=100000000 
ans=0
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        ans += p
        for i in range(p*p, n, p):
            era[i] = False

for i in primes[::-1]:
    p=[]
    j=i
    while i!=0: 
        p.append(i%10)
        i//=10
    if set(p)==set(range(1,len(p)+1)):
        print(j)
        break