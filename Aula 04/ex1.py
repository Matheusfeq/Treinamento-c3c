x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

while(y == 0):
    y = int(input("Valor inválido. Digite novamente o segundo valor: "))

print("O valor da divisão é: ",x/y)