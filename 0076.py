import numpy as np
n=101
t=np.poly1d([1])
for i in range(1,n):
    s=[0 for z in range(n)]   # Coefs of the polynomial.
    for j in range(n):
        if (j)%i==0:          # Those coefs will only be non-zero if the exp isn't divisible by the number
            s[j]=1            # It will be 1 IOC
    print(" ")
    print(np.poly1d(s[::-1]))
    print(" ")
    t*=np.poly1d(s[::-1])     # Since poly1D makes the polynomial ([1,2,3]) into x^2+2x+3, I need to reverse the array.
print(t.coef[100])