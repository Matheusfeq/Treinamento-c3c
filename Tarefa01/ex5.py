estoqueAtual = int(input("Digite a quantidade atual de estoque: "))
estoqueMinimo = int(input("Digite a quantidade mínima de estoque: "))
estoqueMaximo = int(input("Digite a quantidade máxima de estoque: "))

estoqueMedio = (estoqueMaximo + estoqueMinimo)/2

if (estoqueAtual >= estoqueMedio):
    print("Não efetuar compra")
else:
    print("Efetuar compra")