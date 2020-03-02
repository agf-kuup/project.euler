t,exp,c=2,7830457,28433
for i in range(exp-1):
    t*=2
    t%=10000000000
print((c*t+1)%10000000000)