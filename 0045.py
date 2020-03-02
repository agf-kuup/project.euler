T=set([int(i*(i+1)/2) for i in range(1000000)])
P=set([int(i*(3*i-1)/2) for i in range(1000000)])
H=set([i*(2*i-1) for i in range(1000000)])
print(max((T.intersection(P)).intersection(H)))