# Programa: Treinando Tabuada

# Solicita o número que o usuário quer treinar
numero = int(input("Digite o número que você quer treinar a tabuada: "))

acertos = 0
erros = 0

# Loop de 1 a 10
for i in range(1, 11):
    resposta = int(input(f"Quanto é {numero} x {i}? "))
    resultado_correto = numero * i
    
    if resposta == resultado_correto:
        print(" Correto!")
        acertos += 1
    else:
        print(f" Que pena, você errou! O valor correto é {resultado_correto}.")
        erros += 1

# Resultado final
print("\n--- Resultado Final ---")
print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")
