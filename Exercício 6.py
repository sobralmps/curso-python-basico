#        EXERCÍCIO 6

from time import sleep

print("\nPrograma que verificar se um número inteiro é par ou ímpar\n")

sleep(1)

num = int(input("Qual o número? "))

sleep(0.5)

print("\nCalculando...")

sleep(0.5)

result = num % 2

if result == 0:
    print("\nNúmero par")

else:
    print("\nNúmero ímpar")
