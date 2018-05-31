mercadoria=float(input('Diga o preço da mercadoria:'))
desconto=float(input('Qual é o percentual de desconto?'))
preço=(mercadoria-(mercadoria*desconto/100))
print('O preço atual é de R$ %5.2f' %preço)

