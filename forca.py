import random

def imprime_mensagem_abertura():
    print("**************************************")
    print("***Olá, bem vindo ao jogo de forca!***")
    print("**************************************")

def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    return palavras[random.randrange(0, len(palavras))].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra? ")
    return chute.strip().upper()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem(acertou, enforcou, letras_acertadas):
    if (acertou):
        print(''.join(letras_acertadas))
        print("Parabêns, você acertou!")

    if (enforcou):
        print(''.join(letras_acertadas))
        print("Que pena, você não acertou, tente novamente!")

    print("\n")

def imprime_mensagem_final():
    print("**************************************")
    print("************Fim de jogo!**************")
    print("**************************************")
    print("\n")

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        letras_faltando = str(letras_acertadas.count('_'))
        print(f"Faltam {letras_faltando} letras para acertar!!!")
        print(''.join(letras_acertadas))
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)                
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))

        enforcou = erros >= len(palavra_secreta)
        acertou = "_" not in letras_acertadas

    imprime_mensagem(acertou, enforcou, letras_acertadas)
        
    imprime_mensagem_final()

if (__name__ == "__main__"):
    jogar()
    