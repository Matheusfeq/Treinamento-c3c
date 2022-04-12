repetir = 'SIM'

while repetir.upper() == 'SIM':
    nota1 = float(input("Digite uma nota: "))
    while (nota1 < 0 or nota1) > 10:
        nota1 = float(input("Nota inválida. Digite novamente: "))
    nota2 = float(input("Digite a segunda nota: "))
    while (nota2 < 0 or nota2 > 10):
        nota2 = float(input("Nota inválida. Digite novamente: "))
    media = (nota1 + nota2)/2
    print("O aluno obteve média: %.2f" %(media))
    if media < 7:
        print("O aluno foi reprovado")
    else:
        print("O aluno foi aprovado")
    
    repetir = input("Se quiser repetir o programa, digite 'Sim'. Caso contrário, digite qualquer outra coisa: ")