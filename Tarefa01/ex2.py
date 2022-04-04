a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

ordenado = []

if(a <= b and a <= c):      #a é o menor
    ordenado.append(a)
    if(b >= c):
        ordenado.append(c)
        ordenado.append(b)
    else:
        ordenado.append(b)
        ordenado.append(c)

elif(b <= a and b <= c):        #b é o menor
    ordenado.append(b)
    if(a >= c):
        ordenado.append(c)
        ordenado.append(a)
    else:
        ordenado.append(a)
        ordenado.append(c)

else:                           #c é o menor
    ordenado.append(c)
    if(a >= b):
        ordenado.append(b)
        ordenado.append(a)
    else:
        ordenado.append(a)
        ordenado.append(b)

print(ordenado)