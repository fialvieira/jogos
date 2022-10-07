import random

print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação!")
print("**************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nível: "))

if nivel < 1 or nivel > 3:
    print("Defina um nível entre 1 e 3!")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina um nível: "))

match nivel:
    case 1:
        total_de_tentativas = 20
    case 2:
        total_de_tentativas = 10
    case 3:
        total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa: {str(rodada)} de {str(total_de_tentativas)}")
    chute = input("Digite um número entre 1 e 100: ")

    if not chute.isnumeric():
        print("Você deve digitar um número!")
        continue

    if int(chute) < 1 or int(chute) > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = int(chute) == numero_secreto
    maior   = int(chute) > numero_secreto
    menor   = int(chute) < numero_secreto

    print("Você digitou ", chute)

    if acertou:
        print("Você acertou!")
        break
    elif maior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif menor:
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("**************************************")
print("Fim de jogo!")
print("**************************************")