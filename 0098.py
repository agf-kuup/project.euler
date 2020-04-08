from itertools import permutations as c

sq=[str(i**2) for i in range(1,100000)]
sq=([i for i in sq if i[-1]!=0])

A=open("0098_words.txt","r")
T=list(A)[0].split(',')
T=[i.replace('"',"") for i in T]
L=dict()
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    L[i]=[]
for i in T:
    L[len(i)].append(i)
for i in range(2,14):
    X=L[i]
    X.sort()
    Y=[sorted(i) for i in X]
    for j in range(len(Y)):
        for k in range(j+1,len(Y)):
            if Y[j]==Y[k]:
                a=X[j]
                b=X[k]
                chars=set(a)
                size=len(chars)
                ps=list(c([1,2,3,4,5,6,7,8,9,0],size))
                chars=list(chars)
                for t in ps:
                    x,y=a,b
                    for sw in range(size):
                        x=x.replace(chars[sw],str(t[sw]))
                        y=y.replace(chars[sw],str(t[sw]))
                    if x in sq and y in sq:
                        print(x,y)