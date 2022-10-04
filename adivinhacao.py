print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("**************************************")

numero_secreto = 42

chute = input("Digite o seu número: ")
acertou = int(chute) == numero_secreto
maior   = int(chute) > numero_secreto
menor   = int(chute) < numero_secreto

print("Você digitou ", chute)

if acertou:
    print("Você acertou!")
elif maior:
    print("Você errou! O seu chute foi maior do que o número secreto.")
elif menor:
    print("Você errou! O seu chute foi menor do que o número secreto.")

print("**************************************")
print("Fim de jogo!")
print("**************************************")