t = 0
d = 50
d += 1

for x1 in range(0,d):
    for y1 in range(0,d):
        for x2 in range(0,d):
            for y2 in range(0,d):
                a = x1**2 + y1**2
                b = x2**2 + y2**2
                c = (x1-x2)**2 + (y1-y2)**2
                if a+b==c or a+c==b or b+c==a:
                    if (x1,y1)!=(x2,y2) and (x1,y1)!=(0,0) and (x2,y2)!=(0,0):                        
                        t += 1
t //= 2 # Removes symmetrical triangles.
print(t)
