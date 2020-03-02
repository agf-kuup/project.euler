import scipy.special as sp
ans=0
for i in range(23,101):
    for j in range(1,101):
        if sp.comb(i,j)>1000000:
            ans+=1
print(ans)