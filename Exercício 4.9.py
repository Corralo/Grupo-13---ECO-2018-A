#   Exercício 4.9
#   Cálculo para financiamento da casa própria

casa = float(input('Digite o valor do imóvel desejado:'))
salário = float(input('Digite o valor de seu salário atual:'))
qtde = float(input('Digite o número de anos em que deseja pagar o imóvel:'))
prestmax = (salário*(30/100))
prestreq = (casa/(qtde*12))
if prestreq>prestmax:
    print('Seu salário não é compatível com o imóvel desejado!')
elif prestreq <= prestmax:
    print('Parabéns! Você poderá adquirir este imóvel pelo valor mensal de R$ %4.2f.' % prestreq)
                   
