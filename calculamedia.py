# Programa para cadastrar aluno e calcular média das notas

# Entrada de dados
print("=== Cadastro de Aluno ===")
nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
idade = int(input("Digite a idade: "))
ra = int(input("Digite o RA: "))

# Entrada das 4 notas
print("\n=== Lançamento das Notas ===")
n1 = float(input("Digite a primeira nota:  "))
n2 = float(input("Digite a segunda nota:  "))
n3 = float(input("Digite a terceira nota:  "))
n4 = float(input("Digite a quarta nota:  "))


# Processamento: cálculo da média
media = n1+n2+n3+n4 / 4

# Saída formatadabe
print("\n=== Resultado Final ===")
print(f"Aluno: {nome} {sobrenome}")
print(f"Idade: {idade} anos")
print(f"RA: {ra}")

print(f"Média Final: {media:.2f}")
