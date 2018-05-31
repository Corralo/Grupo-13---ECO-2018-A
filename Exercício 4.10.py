#   Exercício 4.10
#   Preço da energia consumida

consumo=int(input("Digite o seu consumo em kWh:"))
tipo=input("Tipo da instalação (R,C ou I):")
if tipo == "R":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C":
    if consumo <=1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Este tipo de instalação não é conhecido!")
custo = consumo * preço
print("Valor a pagar: R$ %7.2f" % custo)
