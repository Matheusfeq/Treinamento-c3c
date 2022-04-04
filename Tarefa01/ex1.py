nota1 = float(input("Digite a nota da 1a avaliação: "))
nota2 = float(input("Digite a nota da 2a avaliação: "))

avaliacoes = {"media":(nota1 + nota2)/2,
              "nota1":nota1,
              "nota2":nota1
}

print("Média: ",avaliacoes["media"])

if (avaliacoes["media"] >= 7):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
