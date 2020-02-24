maxnum=0
for i in range(1,9999): #Si es un # de 5 digitos, su T será menor a la cadena del 9
    T=''
    for p in range(1,10):
        T+=str(i*p)
        if '0' in T or len(T)>9:
            break
        if len(set(T))==9:
            if maxnum<int(T):
                maxnum=int(T)
            break
print(maxnum)