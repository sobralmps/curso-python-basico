#-*- coding: utf-8 -*-
# Questao escolhida: 4

#Printando objetivo do programa
print("Questão 4\nPrograma que recebe 10 números inteiros e mostra a quantidade de números pares e ímpares.\n")

num_par = 0 #Criação da contador de números pares
num_impar = 0 #Criação de contador de números ímpares

for i in range(0,10): #Gera loop que se repetirá por 10 vezes
    num = int(input(f"Digite o {i+1} número: ")) #Pede para que o usuário entre com um número

    if (num % 2) == 0: #Verifica se o número digitado é par
        num_par = num_par + 1 #Adiciona o número par ao contador de números pares
    else: #Verifica se o número digitado NÃO é par
        num_impar = num_impar + 1 #Adicionar o número não par ao contador de números ímpares

#Printa os contadores com as quantidades de números ímpares e pares
print(f"\nEntre esses 10 números inteiros, há {num_par} números pares, e {num_impar} números ímpares.")