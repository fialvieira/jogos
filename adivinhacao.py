print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("**************************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou ", chute)

if numero_secreto == int(chute):
    print("Você acertou!")
elif int(chute) > numero_secreto:
    print("Você errou! O seu chute foi maior do que o número secreto.")
elif int(chute) < numero_secreto:
    print("Você errou! O seu chute foi menor do que o número secreto.")

print("**************************************")
print("Fim de jogo!")
print("**************************************")