import numpy as np

change=[1,2,5,10,20,50,100,200]
t=np.poly1d([1])
for i in change:
    coefs=[0 for z in range(201)]
    for j in range(200+1):
        if (j)%i==0:
            coefs[j]=1
    t*=np.poly1d(coefs[::-1])
v=0
print(t.coef[200])