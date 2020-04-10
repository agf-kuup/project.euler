A=dict()
for i in range(1,1000000):
    m=int(3*i/7.0)
    numden=(m,i)
    val=m/float(i)
    A[val]=numden
A.pop(float(3)/7)

print(A[max(A.keys())])
    
