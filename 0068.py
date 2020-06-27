from itertools import permutations
m=0
for i in permutations(list(range(10,0,-1))):
    c=i[0]+i[1]+i[2]
    if c==i[2]+i[3]+i[4]:
        if c==i[4]+i[5]+i[6]:
            if c==i[6]+i[7]+i[8]:
                if c==i[1]+i[8]+i[9]:
                    n=int(str(i[9])+str(i[8])+str(i[1])\
                          +str(i[0])+str(i[1])+str(i[2])\
                          +str(i[3])+str(i[2])+str(i[4])\
                          +str(i[5])+str(i[4])+str(i[6])\
                          +str(i[7])+str(i[6])+str(i[8]))
                    print(n,c)