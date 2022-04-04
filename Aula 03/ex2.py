horasTrabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salarioHora = float(input("Digite o valor da hora trabalhada: "))

if (horasTrabalhadas <= 160):
    salarioTotal = horasTrabalhadas*salarioHora
else:
    salarioTotal = horasTrabalhadas*salarioHora + (horasTrabalhadas - 160)*salarioHora*0.5

print("O salário total é: ",salarioTotal)