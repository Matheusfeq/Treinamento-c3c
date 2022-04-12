quantidadeNegativos = 0
for i in range(10):
    x = float(input("Digite um valor: "))
    if (x < 0):
        quantidadeNegativos += 1

print("Quantidade de números negativos: ",quantidadeNegativos)