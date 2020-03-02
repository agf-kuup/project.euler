n=1000000
era =[1] * n
primes=set([])
for p in range(2, n):
    if era[p]:
        primes.add(p)
        for i in range(p*p, n, p):
            era[i] = False
i=1
t=0
ans=0
while t<25:
    i+=2
    if not i in primes and i%5!=0:
        repunit=1
        for j in range(1,i-1):
            jj=0
            repunit+=10**j
            if repunit%i==0:
                jj+=1
                lenunit=len(str(repunit))
                if (i-1)%lenunit==0:
                    t+=1
                    ans+=i
                    print(i,repunit)
                    break
            if jj!=0:
                break
print(ans)