idadeHomem1 = int(input("Digite a idade do primeiro homem: "))
idadeHomem2 = int(input("Digite a idade do segundo homem: "))
idadeMulher1 = int(input("Digite a idade da primeira mulher: "))
idadeMulher2 = int(input("Digite a idade da segunda mulher: "))

if(idadeHomem1 > idadeHomem2 and idadeMulher1 > idadeMulher2):
    soma = idadeHomem1 + idadeMulher2
    produto = idadeHomem2 * idadeMulher1
elif(idadeHomem1 > idadeHomem2 and idadeMulher2 > idadeMulher1):
    soma = idadeHomem1 + idadeMulher1
    produto = idadeHomem2 * idadeMulher2
elif(idadeHomem2 > idadeHomem1 and idadeMulher1 > idadeMulher2):
    soma = idadeHomem2 + idadeMulher2
    produto = idadeHomem1 * idadeMulher1
else:
    soma = idadeHomem2 + idadeMulher1
    produto = idadeHomem1 * idadeMulher2

print("Soma das idades do homem mais velho com a mulher mais nova: ",soma)
print("Produto das idades do homem mais novo com a mulher mais velha: ",produto)
