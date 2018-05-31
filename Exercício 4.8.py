#   Exercício 4.8
#   Ler dois números e escolher uma operação a ser realizada

n1 = float(input('Digite seu primeiro número:'))
n2 = float(input('Digite seu segundo número:'))
op = input('Digite a operação você deseja realizar: (+), (-), (*) ou (/):')
if op == ('+'):
    Resultado = (n1+n2)
elif op == ('-'):
    Resultado = (n1-n2)
elif op == ('*'):
    Resultado = (n1*n2)
elif op == ('/'):
    Resultado = (n1/n2)    
else:
    print('Digite uma operação válida entre (+), (-), (*) ou (/):')
    Resultado == ('Não válida')
print('O resultado desta operação é %4.2f' % Resultado)
