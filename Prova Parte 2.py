#-*- coding: utf-8 -*-
# Questao escolhida: 2

#Printando o objetivo do programa
print("Questão 2\nPrograma que calcula a tabulada de um número.\n")

numero = int(input("Digite um número para encontrar sua tabuada: ")) #Usuário precisa entrar com um valor

print(f"\nTabuada de {numero}:") #Print que mostra de qual número será a tabuada

for i in range(1,11): #Criação de um loop que se repetirá 10 vezes
    print(f"{numero} x {i} = {numero*i}") #Printa a multiplicação para criação da tabuada de 1 até 10

