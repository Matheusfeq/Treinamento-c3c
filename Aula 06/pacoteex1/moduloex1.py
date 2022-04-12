def login(cont):
    
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    banco = {"Ronaldo" : '123',
             "Alberto" : '456',
             "Rogério" : '789'}

    for key in banco:
        if (key == usuario) and (banco[key] == senha):
            print('Usuário autorizado no sistema!')
            break
    
    if cont == 2:
        print("Usuário bloqueado!")

    if usuario in banco and (banco[usuario] != senha):
        cont += 1
        print("Tente novamente! você tem mais %i chance(s)!"%(3 - cont))
        login(cont)

    
