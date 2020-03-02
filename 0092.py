#Presetting all
lmt=10000000
A=[0 for i in range(lmt)]
for i in [44,32,13,1,10]: A[i]=-1
for i in [85, 89, 145, 42, 20, 4, 16, 37, 58]: A[i]=1

def squaring(n):
    m=0
    while n!=0:
       m+=(n%10)**2
       n//=10
    return(m)
    
def sumsq(n):
    NotRegistered=[]
    while True:
        x=squaring(n)
        NotRegistered.append(x)
        if A[x]==1 or A[x]==-1:
            for h in NotRegistered:
                A[h]=A[x]
            break
        else:
            n=x

for r in range(2,10000000):
    sumsq(r)

print(A.count(1))