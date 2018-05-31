# Preço do aluguel de um carro

distância = float(input('Qual a distância que você percorreu com seu carro alugado?'))
dias = float(input('Quantos dias você permaneceu com o carro?'))
valor = ((0.15*distância)+(60*dias))
print('Você deverá pagar R$ %5.2f' % valor)
