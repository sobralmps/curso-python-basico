#        EXERC�CIO 3

from time import sleep

print("\nPrograma que retorna [Feminino], caso voc� digite F, e retorna [Masculino], caso voc� digite M\n")

sleep(1)

x = input("Insira F ou M: ")

sleep(0.5)

if x == "F":
    print("\nFeminino")

if x== "M":
    print("\nMasculino")

else:
    print("\nO que foi digitado n�o � F ou M")
