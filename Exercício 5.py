#        EXERC�CIO 5

from time import sleep

print("\nPrograma que calcula a m�dia entre 3 notas, caso a m�dia seja superior a 7, retornar a mensagem de aprova��o\n")

sleep(1)

nota1 = float(input("Qual o a primeira nota? "))
nota2 = float(input("Qual o a segunda nota? "))
nota3 = float(input("Qual o a terceira nota? "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

media = (nota1+nota2+nota3)/3

if media >= 7:
    print("\nAprovado")

else:
    print("\n\nReprovado")

print(f"\nSua m�dia � de {media}")
