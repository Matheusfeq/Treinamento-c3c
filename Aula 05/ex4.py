def calcularMedia(x,y):
    acumulador = 0
    if (y > x):
        for i in range(x+1,y):
            acumulador += i
            n = y - x - 1
    else:
        for i in range(y+1,x):
            acumulador += i
            n = x - y - 1

    media = acumulador/n
    return media

print(calcularMedia(10,6))