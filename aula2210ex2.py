# Inicializa a soma
soma = 0

# Lê 5 números do usuário
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero  # acumula a soma

# Calcula a média
media = soma / 5

# Exibe os resultados
print(f"\nA soma dos números é: {soma}")
print(f"A média dos números é: {media}")
