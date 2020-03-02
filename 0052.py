import time
start=time.time()
t=True
n=11
while t==True:
    n+=1
    n6=6*n
    N=set(list(str(n)))
    N6=set(list(str(n6)))
    if N==N6:
        for x in range(2,6):
            nx=set(list(str(n*x)))
            if nx != N:
                break
        if x==5 and nx==N:
            print(n)
            break