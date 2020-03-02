n=1000000
ans=0
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(p)
        ans += p
        for i in range(p*p, n, p):
            era[i] = False

def factor(t):
    a=[]
    while t%2==0:
        t//=2
        a.append(2)
    for i in list(filter(lambda x: x<t**.5,primes[:t])):
        if t<2:
            break
        else:
            while t%i==0:
                a.append(i)
                t/=i
    if t!=1:
        a.append(t)
    g=list(set(a))
    h=[]
    for n in range(len(g)):
        r=a.count(g[n])
        h.append(r+1)
    e=1
    for c in range(len(h)):
        e*=h[c]
    return e        

D=1
i=2
while True:
    if i%2==0:
        if factor(int(i/2))*factor(i+1)>500:
            print(i*(i+1)/2)
            break
    else:
        if factor(i)*factor(int((i+1)/2))>500:
            print(i*(i+1)/2)
            break
    i+=1