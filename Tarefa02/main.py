from ast import While
from pacoteex2.inputs import*
from pacoteex2.operacoes import*

mercadoriaTotal = []

while(True):
    mercadoria = []

    mercadoria.append(input("Digite o nome da mercadoria: "))
    mercadoria.append(receberQntdMinima())
    mercadoria.append(receberQntdMaxima())
    mercadoria.append(receberQntdAtual(mercadoria[2]))
    mercadoria.append(receberValor())

    total = mercadoria[3]*mercadoria[4]
    mercadoria.append(total)
    
    if(mercadoria[3] < mercadoria[1]):
        reposicao = 'Sim'
    else:
        reposicao = 'Não'

    mercadoria.append(reposicao)
    mercadoriaTotal.append(mercadoria)

    resp = input("Quer inserir outra mercadoria?(S/N): ")
    if resp.upper() == 'N':
        break

tabela(mercadoriaTotal)


