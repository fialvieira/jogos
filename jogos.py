import forca
import adivinhacao


def escolher_jogo():
    print("**************************************")
    print("*********Escolha o seu jogo!**********")
    print("**************************************")

    print("(1) Forca (2) Adivinhação")

    while True:
        try:
            jogo = input("Qual o jogo? ")

            if not jogo.isnumeric():
                raise ValueError("Apenas números são permitidos!")

            if int(jogo) < 1 or int(jogo) > 2:
                raise ValueError("Nível fora do range permitido: 1 - 2!")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break

    if int(jogo) == 1:
        print("Jogando forca...")
        forca.jogar()
    else:
        print("Jogando adivinhação...")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolher_jogo()
