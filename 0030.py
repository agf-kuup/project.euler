ans=0
for i in range(2,6*9**5+1):
    if sum(map(lambda x: x**5,list(map(int,str(i)))))==i:
        ans+=i
print(ans)