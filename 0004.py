m=0
for i in range(101,999):
    for j in range(101,999):
        if str(i*j)==str(i*j)[::-1]:
            if i*j>m:
                m=i*j
print(m)