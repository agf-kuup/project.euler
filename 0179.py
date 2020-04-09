lmt=10**7
S=[0 for i in range(lmt+1)]

for i in range(1,lmt//2):
    for j in range(i,len(S),i):
        S[j]+=1

sol=0
for i in range(1,lmt+1):
    if S[i]==S[i-1]:
        sol+=1
print(sol)