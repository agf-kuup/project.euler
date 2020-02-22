m=0
for i in range(101,999):
    for j in range(101,999):
        u=str(i*j)
        if u==u[::-1]:
            if i*j>m:
                m=i*j
print(m)