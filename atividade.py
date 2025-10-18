# Programa para calcular a hipotenusa de um triângulo retângulo

# Entrada dos catetos
cateto_oposto = float(input("Entre com o valor do cateto oposto: "))
cateto_adjacente = float(input("Entre com o valor do cateto adjacente: "))

# Cálculo da hipotenusa usando o Teorema de Pitágoras
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

# Exibição do resultado
print(f"O valor da hipotenusa é {hipotenusa:.1f}")
