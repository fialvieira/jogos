print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("**************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while total_de_tentativas >= rodada:
    print("Tentativa: " + str(rodada) + " de 3")

    chute = input("Digite o seu número: ")

    acertou = int(chute) == numero_secreto
    maior   = int(chute) > numero_secreto
    menor   = int(chute) < numero_secreto

    print("Você digitou ", chute)

    if acertou:
        print("Você acertou!")
        total_de_tentativas = 0
    elif maior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif menor:
        print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada += 1

print("**************************************")
print("Fim de jogo!")
print("**************************************")