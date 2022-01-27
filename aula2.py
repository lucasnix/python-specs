#condicionais
#if, elif e else
'''
E ai lucas vamos dar uma saida hoje?
se eu terminar meu trabalho aqui, eu consigo.

estou_livre = False
if estou_livre == True:
    print('Estou livre bora tirar as caixas')
else:
    print('pede pro meu brother, pq eu to ocupado')

numero_de_atraso = 0
if numero_de_atraso >= 3:
    print('ja era pra vc amigo')
elif numero_de_atraso == 1:
    print('pode entrar meu consagrado, mais 2 tu ta fora')
elif numero_de_atraso == 2:
    print('pode entrar meu chapa mais 1 tu ta fora, a agua ta batendo na bunda')
else:
    print('pode chegar junto')
'''
#encontre o maior entre 2 numeros

primeiro_valor = input ('digite o primeiro valor: ')
segundo_valor = input ('digite o segundo valor: ')
if int(primeiro_valor) > int(segundo_valor):
    print('primeiro valor maior')
else:
    print('segundo valor maior amigo')