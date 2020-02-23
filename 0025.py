A=[1,1]
i,ans=2,0
while(True):
    t=A[i-1]+A[i-2]
    A.append(t)
    if len(str(t))>999:
        break
    i+=1
print(i+1) #Is needed this +1 because I'm starting the fibonacci sequence from 0.