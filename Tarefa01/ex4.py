salarioFixo = float(input("Digite o salário fixo: "))
valorVendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: "))

if (valorVendas <= 1500):
    comissao = valorVendas*0.03
else:
    comissao = 1500*0.03 + (valorVendas - 1500)*0.05

salarioTotal = salarioFixo + comissao

print("Salário total é: %f reais" %(salarioTotal))