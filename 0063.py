from math import log
ans=0
for i in range(2,100000):
    for exp in range(2,11):
        if (i**exp)**(1/float(len(str(i**exp)))) in range(1000):
            print(i,i**exp,(i**exp)**(1/float(len(str(i**exp)))))
            ans+=1
print(ans)