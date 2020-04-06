#-*- coding: utf-8 -*-

#        EXERCÍCIO 5

from time import sleep

print("\nPrograma que calcula a média entre 3 notas, caso a média seja superior a 7, retornar a mensagem de aprovação\n")

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

print(f"\nSua média é de {media}")
