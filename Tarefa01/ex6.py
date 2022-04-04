x = int(input("Digite um número: "))
y = int(input("digite um outro número: "))          #Recebe 2 valores inteiros
z = (x*y)+5             #Adiciona 5 ao resultado do produto dos 2 inteiros e guarda numa variável 'z'
if z <= 0:              #Se 'z' for menor ou igual a 0, a resposta é A
    resposta = "A"
elif z <= 100:          #Se 'z' for menor ou igual a 100, mas maior que 0, a resposta é B
    resposta = "B"
else:                   #Se 'z' for maior que 100, a resposta é C
    resposta = "C"
print("Resultado final: %i. Resposta: %s" %(z,resposta))        #Imprime o valor de 'z' e a resposta

#item A) z = 55 / resposta = B
#item B) z = 20005 / resposta = C
#item C) z = -913 / resposta = A
#item D) z = -315 / resposta = A
#item E) z = 155 / resposta = C