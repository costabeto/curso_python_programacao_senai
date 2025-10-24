# Programa: Altura dos Alunos

# Inicializa as variáveis
mais_alto_numero = 0
mais_alto_altura = 0
mais_baixo_numero = 0
mais_baixo_altura = 999  # valor alto só pra começar a comparação

# Loop para ler 10 conjuntos de dados
for i in range(1, 11):
    print(f"\n--- Aluno {i} ---")
    numero = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno (em cm): "))
    
    # Verifica se é o mais alto
    if altura > mais_alto_altura:
        mais_alto_altura = altura
        mais_alto_numero = numero

    # Verifica se é o mais baixo
    if altura < mais_baixo_altura:
        mais_baixo_altura = altura
        mais_baixo_numero = numero

# Exibe os resultados
print("\n===== RESULTADO FINAL =====")
print(f" Aluno mais alto: Nº {mais_alto_numero} com {mais_alto_altura:.1f} cm")
print(f" Aluno mais baixo: Nº {mais_baixo_numero} com {mais_baixo_altura:.1f} cm")
