import os
os.system("cls")
lista1=[]
a=[]
b=[]
c=[]
i=1
while(True):
    os.system("cls")
    print("Ingresando número ",i)
    while(True):
        try:
            num=int(input("Ingrese un número positivo "))
            break
        except ValueError:
            print("Debe ser entero")
    #fuera de la validación agrego el elemento a la lista
    lista1.append(num)
    res=input("Escriba si, si desea seguir ingresando ").lower()
    if(res!="si"):
        break
    i+=1
for i in range(len(lista1)):
    if(lista1[i]%2==0):#dejo en a todos los pares
        a.append(lista1[i])
    if(lista1[i]>0): #dejo en b todos los positivos
        b.append(lista1[i])
    if(i%2==0): #aqui dejo en c todos los elementos que estén en un níndice par
        c.append(lista1[i])
print(lista1)
print(a)
print(b)
print(c)

    
    
