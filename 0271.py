
# 13082761331670030 is 2,3,5,7,11,13,17,19,23,29,31,37,41,43

# Using a for loop from 0 to p-1 and a conditional if i**3%p==1, I got this: 
# For values in 2,  1
# For values in 3,  1
# For values in 5,  1
# For values in 7,  1 2 4
# For values in 11, 1
# For values in 13, 1 3 9 
# For values in 17, 1
# For values in 19, 1 7 11
# For values in 23, 1
# For values in 29, 1
# For values in 31, 1 5 25
# For values in 37, 1 10 26
# For values in 41, 1
# For values in 43, 1 6 36
#
# So the solution must accomplish those modular equations.
# Anyway they're only 3**6-1 solutions (-1 avoiding the 1).

from functools import reduce

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=int(prod/n_i)
        sum += int(a_i* mul_inv(p, n_i)*p)
    return int(sum % prod)

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=int(a// b)
        a, b= b, a%b
        x0, x1=int(x1 -q *x0), int(x0)
    if x1<0 : x1+= b0
    return int(x1)

primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]

r7 =[1,2,4]
r13=[1,3,9]
r19=[1,7,11]
r31=[1,5,25]
r37=[1,10,26]
r43=[1,6,36]
ans=0
for i7 in range(3):
    m7=r7[i7]
    for i13 in range(3):
        m13=r13[i13]
        for i19 in range(3):
            m19=r19[i19]
            for i31 in range(3):
                m31=r31[i31]
                for i37 in range(3):
                    m37=r37[i37]
                    for i43 in range(3):
                        m43=r43[i43]
                        ans+=chinese_remainder(primes,[1,1,1,m7,1,m13,1,m19,1,1,m31,m37,1,m43])
print(int(ans)-1)