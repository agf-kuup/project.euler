n=500000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        for i in range(p*p, n, p):
            era[i] = False
#Index of python starts in 0

lmt=n
Z=[0 for i in range(lmt+1)]
for i in primes:
    for t in range(i,lmt,i):
        Z[t]+=1

for v in range(4,lmt+1):
    if Z[v]==4:
        if Z[v-1]==4:
            if Z[v-2]==4:
                if Z[v-3]==4:
                    print(v-3,v-2,v-1,v)
                    break