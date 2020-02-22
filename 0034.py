from math import factorial as f
ans=0
for i in range(3,7*f(9)+1):
    if sum(map(lambda x: f(x),list(map(int,str(i)))))==i:
        ans+=i
print(ans)