import numpy as np
n=101
t=np.poly1d([1])
for i in range(1,n):
    s=[0 for z in range(n)]
    for j in range(n):
        if (j)%i==0:
            s[j]=1
    print(" ")
    print(np.poly1d(s[::-1]))
    print(" ")
    t*=np.poly1d(s[::-1])
print(t.coef[100])