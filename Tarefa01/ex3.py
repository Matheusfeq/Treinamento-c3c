inicio = int(input("Digite a hora de início do jogo: "))
final = int(input("Digite a hora do término do jogo: "))

if (final > inicio):
    duracao = final - inicio
elif(final == inicio):
    duracao = 24
else:
    duracao = (24 - inicio) + final

print("A duração do jogo foi de: %i horas" %(duracao))
