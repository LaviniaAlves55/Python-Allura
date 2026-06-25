import Adivinhação
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    forca.jogar()
    print("Jogando forca")
elif (jogo == 2):
    Adivinhação.jogar()
    print("Jogando Adivinhação")