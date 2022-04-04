par = []
impar = []

for i in range(5):
    n = int(input("Digite um número: "))
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)

pares = {"Pares":par}
print(pares)
print(impar)
