n=100000000
era =[1] * n
primesPan=[]
for p in range(2, n):
    if era[p]:
        st=str(p)
        if len(list(st))==len(set(st)) or '0' in st:
            primesPan.append(set(str(p)))
        for i in range(p*p, n, p):
            era[i] = False
print(len(primesPan))

