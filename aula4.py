#listas
'''
preco_1 = 20
preco_2 = 50
preco_3 = 100

precos = [20,50,100]
#indice    0  1  2

print(precos[2])
print(precos.index(100))

#listas

diversidades = [15, 'lucas', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

for preco in precos:
    print(preco)
'''
#dado uma colecao de dados idades [15,46,75,34,23],
#imprima na tela a soma destes valores

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total) 