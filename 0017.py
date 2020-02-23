U=['','one','two','three','four','five','six','seven','eight','nine']
D=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
D10=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
H='hundred'
AND='and'
t=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if j==0: 
                if k==1: #If the number is of the form 1X
                    t+=len(D10[i]) #len of built word added to total
                else:
                    t+=len(D[k]+U[i]) #len of built word added to total
            else:
                if k==0 and i==0:
                    t+=len(U[j]+H) #len of built word added to total
                else:
                    if k==1:
                        t+=len(U[j]+H+AND+D10[i]) #len of built word added to total
                    else:
                        t+=len(U[j]+H+AND+D[k]+U[i]) #len of built word added to total
print(t+11) #The 11 is for "one thousand"