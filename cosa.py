m=31
start=time()
print()
t=["()"]*(m)
for i in range(1,m):
    t[i]="("+''.join(t[:i])+")"
print(time()-start)