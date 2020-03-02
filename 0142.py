for x in range(1,100000):
    for y in range(1,x):
        s1=(x+y)**.5
        s2=(x-y)**.5
        if s1%1==0 and s2%1==0:
            for z in range(1,y):
                        s3=(x+z)**.5
                        s4=(x-z)**.5
                        if s3%1==0 and s4%1==0:
                            s5=(y+z)**.5
                            s6=(y-z)**.5
                            if s6%1==0 and s5%1==0:
                                print(x,y,z)
                                print(x+y+z)