u=[0,0,0,0]
for i in range(1,1000):
    for j in range(1,1000-i+1):
            if (1000-j-i)**2+j**2==i**2:
                if i*j*(1000-i-j)> u[3]:
                    u=[i,j,1000-i-j,i*j*(1000-i-j)]
print(u[3])