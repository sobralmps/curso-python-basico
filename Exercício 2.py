#        EXERC�CIO 2

from time import sleep

print("\nPrograma que pede um n�mero e retorna se ele � positivo \n")

sleep(1)

x = int(input("Insira o n�mero: "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

if x > 0:
    print(f"\nO n�mero {x} � um n�mero positivo.")

if x == 0:
    print(f"\nO n�mero {x} � neutro.")

else:
    print(f"\nO n�mero {x} � negativo.")
