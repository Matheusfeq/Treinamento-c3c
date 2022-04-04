idade = int(input("Digite a sua idade: "))

if (idade <= 15):
    print("Você não pode votar!")
elif(idade >= 18 and idade < 70):
    print("Você é obrigado a votar!")
else:
    print("Você pode votar, mas não é obrigado")