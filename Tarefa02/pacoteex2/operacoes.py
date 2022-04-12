from prettytable import PrettyTable

def tabela(mercadoriaTotal):
    x = PrettyTable()
    x.field_names = ['Nome da mercadoria', 'Quantidade mínima', 'Quantidade máxima', 'Quantidade atual', 'Valor unitário', 'Valor total', 'Reposição?']
    x.add_rows(mercadoriaTotal)

    print(x)