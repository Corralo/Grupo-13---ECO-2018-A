# Exercício 4.2
# Aplicação de multa por velocidade

velocidade = int(input('Qual a sua velocidade na estrada?'))
multa=((velocidade-80)*5)
if velocidade>80:
    print('Sua multa é de R$ %3.2f!' % multa)
if velocidade<=80:
    print('Parabéns, você é um ótimo motorista!')
    
