########Algorithm from 0007
n=1000000
era =[1] * n
primes=[]
for p in range(2, n):
    if era[p]:
        primes.append(str(p))
        for i in range(p*p, n, p):
            era[i] = False
#######Filter by 0037
def basic_filter(n):
    if len(set(n).intersection(set(["2","4","5","6","8","0"])))!=0:
        return False
    else: return True
primes=list(filter(basic_filter,primes))
ans=2
for p in primes:
    flag=True
    for j in range(9):
        p=p[1:]+p[0]
        if p not in primes:
            flag=False
            break
    if flag:
        ans+=1
print(ans)