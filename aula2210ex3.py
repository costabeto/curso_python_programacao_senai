# Pede a quantidade de pessoas
n = int(input("Quantas pessoas há na turma? "))

# Inicializa a soma das idades
soma_idades = 0

# Lê as idades de cada pessoa
for i in range(1, n + 1):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    soma_idades += idade

# Calcula a média de idades
media = soma_idades / n

# Mostra a média
print(f"\nA média de idade da turma é: {media:.2f}")

# Verifica a faixa etária da turma
if 0 <= media <= 25:
    print("A turma é jovem.")
elif 26 <= media <= 60:
    print("A turma é adulta.")
elif media > 60:
    print("A turma é idosa.")
else:
    print("Idades inválidas informadas.")
