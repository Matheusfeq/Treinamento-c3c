codigo = 123456
codigoInput = int(input("Digite o código de 6 números: "))
senha = 'C3c@9999#'

if (codigoInput == codigo):
    senhaInput = input("Código correto! Digite a senha de acesso: ")
    if(senhaInput == senha):
        print("Acesso permitido!")
    else:
        print("Senha incorreta")

else:
    print("Usuário inválido!")