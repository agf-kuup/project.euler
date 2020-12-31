from math import gcd
t = 0
for i in range(1,12001):
    for j in range( i//3 , i//2 + 1):
        if gcd(i,j)==1 and j/i<1/2 and j/i>1/3:
            t += 1
print(t)
