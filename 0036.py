ans=0
for i in range(1000000):
    if str(i)[::-1]==str(i):
        if (bin(i)[2:])[::-1]==str(bin(i)[2:]):
            ans+=i
print(ans)