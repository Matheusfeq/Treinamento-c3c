quantidadeDentro = 0
quantidadeFora = 0
for i in range(10):
    x = float(input("Digite um valor: "))
    if (x >= 10 and x <= 20):
        quantidadeDentro += 1
    else:
        quantidadeFora += 1

print("Quantidade de números dentro do intervalo: ",quantidadeDentro)
print("Quantidade de números fora do intervalo: ",quantidadeFora)