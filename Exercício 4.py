#        EXERC�CIO 4

from time import sleep
from datetime import date

print("\nPrograma que a partir do seu ano de nascimento retorna se voc� est� apto ou n�o a tirar CNH\n")

sleep(1)

anonasc = int(input("Qual o ano do seu nascimento? "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

anoatual = date.today().year

if (anoatual-anonasc) >= 18:
    print("\nVoc� est� apto para tirar a CNH")

else:
    print("\nVoc� n�o � digno!")

print(f"\nSua idade � de {anoatual-anonasc} anos")
