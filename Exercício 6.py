#        EXERC�CIO 6

from time import sleep

print("\nPrograma que verificar se um n�mero inteiro � par ou �mpar\n")

sleep(1)

num = int(input("Qual o n�mero? "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

result = num % 2

if result == 0:
    print("\nN�mero par")

else:
    print("\nN�mero �mpar")
