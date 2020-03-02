#Puede reducirse a hallar 
for i in range(101010000+3,14*(10**7),2):
    if i%10==3 or i%10==7: #El cuadrado termina en 9 y sólo puede ser de decena 3 o 7
        n=(i**2)//100
        if n%10 - 8 ==0: #El resto es fuerza bruta buscando el número
            n//=100
            if n%10 - 7 ==0: 
                n//=100
                if n%10 - 6 ==0: 
                    n//=100
                    if n%10 - 5 ==0: 
                        n//=100
                        if n%10 - 4 ==0: 
                            n//=100
                            if n%10 - 3 ==0: 
                                n//=100
                                if n%10 - 2 ==0: 
                                    n//=100
                                    if n%10 - 1 ==0:
                                        print(str(i)+'0')
                                        break