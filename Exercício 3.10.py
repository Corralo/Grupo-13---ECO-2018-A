# Saiba qual será seu salário após o aumento

salario = float(input('Digite seu salário: '))
aumento = float(input('Digite seu aumento salarial: '))
novo_salario = (salario+(salario*aumento/100))
print('Seu novo salário será de R$ %6.2f' % novo_salario)
