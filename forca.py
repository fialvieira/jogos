def jogar():
    print("**************************************")
    print("***Olá, bem vindo ao jogo de forca!***")
    print("**************************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        letras_faltando = str(letras_acertadas.count('_'))
        print(f"Faltam {letras_faltando} letras para acertar!!!")
        print(''.join(letras_acertadas))
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index += 1

        if ''.join(letras_acertadas) == palavra_secreta:
            print(''.join(letras_acertadas))
            print("Parabêns, você acertou!")
            break;

    print("**************************************")
    print("************Fim de jogo!**************")
    print("**************************************")

if __name__ == "__main__":
    jogar()
