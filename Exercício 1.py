#        EXERC�CIO 1

from time import sleep

print("\nPrograma que printa Hello World, caso o primeiro n�mero seja maior que o segundo.\n")

x = "\nHello World!"

sleep(1)

a = int(input("N�mero A: "))
b = int(input("N�mero B: "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

if a > b:
    print(f"\nO n�mero {a} � maior que o n�mero{b}.")
    print(x)

else:
    print(f"\nO n�mero {a} n�o � maior que o n�mero {b}.")
