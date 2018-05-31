#   Exercício 4.3
#   Calculando o aumento do saláro do empregado

sal=float(input('Senhor empregado, qual é o seu salário atual?'))
if sal>1250:
    ns=(sal+(sal*10/100))
    print('Seu salário será de R$%5.2f' % ns)
if sal<=1250:
    ns=(sal+(sal*15/100))
    print('Seu salário será de R$%5.2f' % ns)
