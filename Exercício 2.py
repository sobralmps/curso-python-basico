#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que pede um número e retorna se ele é positivo \n")

sleep(1)

x = int(input("Insira o número: "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

if x > 0:
    print(f"\nO número {x} é um número positivo.")

if x == 0:
    print(f"\nO número {x} é neutro.")

else:
    print(f"\nO número {x} é negativo.")
