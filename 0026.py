from decimal import getcontext,Decimal
getcontext().prec=10002
limit=1000000
A=[0 for i in range(limit)]
A[0]=1
A[1]=1
primes=[]
for i in range(3,limit+1,2):
    if A[i]==0:
        primes.append(i)
        for j in range(i,int(limit/i),2):
            if j%i==0:
                A[j]=1
nmax=0
trivial=4
maxd=trivial
for i in range(999,12,-1):
    trivial=4
    F=Decimal(1.)/Decimal(i)
    if i in primes:
        L=list(str(F))
        T=False
        while T==False:
            #print L[2:maxd]
            #print L[maxd:2*maxd-2]
            if L[2:trivial]!=L[trivial:2*trivial-2]:
                trivial+=1
                if trivial>maxd: 
                    maxd=trivial
                    nmax=i
            else: T=True
print(maxd,nmax)