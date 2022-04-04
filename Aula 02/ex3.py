nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = int(input("Digite o seu peso: "))
academia = input("Digite o nome da academia que frequenta: ")

aluno = {
    "nome":nome,
    "idade":idade,
    "altura":altura,
    "peso":peso,
    "academia":academia
}

print(aluno)