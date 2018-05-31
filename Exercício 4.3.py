# Exercício 4.3
# Imprimir o maior e o menor número dentre três dados

n1=int(input("Escreva seu primeiro número:"))
n2=int(input("Escreva seu segundo número:"))
n3=int(input("Escreva seu terceiro número:"))
if n1>n2>n3:
    print('Seu menor número é %d e seu maior número é %d' %(n3, n1))
if n2>n1>n3:
    print('Seu menor número é %d e seu maior número é %d' %(n3, n2))
if n1>n3>n2:
    print('Seu menor número é %d e seu maior número é %d' %(n2, n1))
if n2>n3>n1:
    print('Seu menor número é %d e seu maior número é %d' %(n1, n2))
if n3>n2>n1:
    print('Seu menor número é %d e seu maior número é %d' %(n1, n3))
if n3>n1>n2:
    print('Seu menor número é %d e seu maior número é %d' %(n2, n3))
