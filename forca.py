import random

def jogar():
    print("**************************************")
    print("***Olá, bem vindo ao jogo de forca!***")
    print("**************************************")

    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        letras_faltando = str(letras_acertadas.count('_'))
        print(f"Faltam {letras_faltando} letras para acertar!!!")
        print(''.join(letras_acertadas))
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1                
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))

        enforcou = erros >= len(palavra_secreta)
        acertou = "_" not in letras_acertadas

    if (acertou):
        print(''.join(letras_acertadas))
        print("Parabêns, você acertou!")

    if (enforcou):
        print(''.join(letras_acertadas))
        print("Que pena, você não acertou, tente novamente!")
        
    print("**************************************")
    print("************Fim de jogo!**************")
    print("**************************************")

if (__name__ == "__main__"):
    jogar()
