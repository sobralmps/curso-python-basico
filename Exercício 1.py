#-*- coding: utf-8 -*-

#        EXERCÍCIO 1

from time import sleep

print("\nPrograma que printa Hello World, caso o primeiro número seja maior que o segundo.\n")

x = "\nHello World!"

sleep(1)

a = int(input("Número A: "))
b = int(input("Número B: "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

if a > b:
    print(f"\nO número {a} é maior que o número{b}.")
    print(x)

else:
    print(f"\nO número {a} não é maior que o número {b}.")
