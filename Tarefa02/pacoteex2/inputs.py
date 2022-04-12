def receberQntdMinima():
    while(True):
        qntdMinima = int(input("Digite a quantidade mínima da mercadoria: "))
        if qntdMinima > 0:
            break
        else:
            print("Quantidade inválida!")
    return qntdMinima

def receberQntdAtual(qntdMaxima):
    while(True):
        qntdAtual = int(input("Digite a quantidade atual da mercadoria: "))
        if qntdAtual > qntdMaxima:
            print("Valor inserido ultrapassa a capacidade máxima!")
        elif qntdAtual > 0:
            break
        else:
            print("Quantidade inválida!")
    return qntdAtual

def receberQntdMaxima():
    while(True):
        qntdMaxima = int(input("Digite a quantidade máxima da mercadoria: "))
        if qntdMaxima > 0:
            break
        else:
            print("Quantidade inválida!")
    return qntdMaxima

def receberValor():
    while(True):
        valor = float(input("Digite o valor unitário da mercadoria: "))
        if valor > 0:
            break
        else:
            print("Valor inválido!")
    return valor
     