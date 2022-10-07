import random

print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("**************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000
pontos_perdidos = 0
verificador = False

while True:
    try:
        print("Qual o nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")
        nivel = input("Defina um nível: ")

        if not nivel.isnumeric():
            raise ValueError("Apenas números são permitidos!")

        if int(nivel) < 1 or int(nivel) > 3:
            raise ValueError("Nível fora do range permitido: 1 - 3!")
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

match int(nivel):
    case 1:
        total_de_tentativas = 20
    case 2:
        total_de_tentativas = 10
    case 3:
        total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa: {str(rodada)} de {str(total_de_tentativas)}")
    print(f"Pontos: {pontos} pontos")

    while True:
        try:
            chute = input("Digite um número entre 1 e 100: ")

            if not chute.isnumeric():
                raise ValueError("Você deve digitar apenas NÚMEROS entre 1 e 100!")

            if int(chute) < 1 or int(chute) > 100:
                raise ValueError("Você deve digitar um número entre 1 e 100!")

        except ValueError as e:
            print("Valor inválido: ", e)
        else:
            break

    acertou = int(chute) == numero_secreto
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto

    print("Você digitou ", chute)

    if acertou:
        print(f"Você acertou e fez {pontos} pontos!")
        break
    elif maior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - int(chute))
        if rodada == total_de_tentativas:
            print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
    elif menor:
        print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - int(chute))
        if rodada == total_de_tentativas:
            print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    pontos = pontos - pontos_perdidos

print("**************************************")
print("Fim de jogo!")
print("**************************************")
