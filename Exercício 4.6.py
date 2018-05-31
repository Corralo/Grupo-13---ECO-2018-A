#   Exercício 4.6
#   Preço da passagem segundo a distência percorrida

dist=float(input('Qual a distância em quilômetros até seu destino final?'))
if dist<=200:
    p=(0.50*dist)
    print('O preço da sua passagem é de R$%4.2f' % p)
else:
    p=(0.45*dist)
    print('O preço da sua passagem é de R$%4.2f' % p)
