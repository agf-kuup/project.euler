A=[1,1]
i,pan=2,set(list(map(str,range(1,10))))
while(True):
    t=A[i-1]+A[i-2]
    A.append(t)
    if set(list(str(t)[:9]))==pan and set(list(str(t)[-9:]))==pan:
        break
    i+=1
    if i==100000:
        break
print(i+1)