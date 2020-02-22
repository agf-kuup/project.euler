A=[1,1]
i,ans=2,0
while(True):
    t=A[i-1]+A[i-2]
    A.append(t)
    if t%2==0:
        ans+=t
    if t>4000000:
        break
    i+=1
print(ans)