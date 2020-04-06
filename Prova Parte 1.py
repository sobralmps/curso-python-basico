#-*- coding: utf-8 -*-
# Questao escolhida: 1

#Printando o objetivo do programa
print("Questão 1\nAlgoritmo que verifica se a senha inserida está correta. Terminal será bloqueado após 3 tentativas")

tentativas_restantes = 3 #Contador de tentativas restantes
senha_correta = 'pythonbasico' #Define uma variável para a senha do sistema

for i in range(0,3): #Criação de loop
    senha_usuario = input("\nDigite a senha para poder entrar: ") #Usuário precisa entrar com uma senha

    if senha_usuario == senha_correta: #Verifica se a senha é correta
        print("\nSeja bem-vindo!")
        break

    else:
        tentativas_restantes = tentativas_restantes - 1 #Diminui as tentativas restantes em caso de erro.
        print(f"\nSenha incorreta. Tente novamente. Tentativas restantes: {tentativas_restantes}.") #Avisa o erro

if tentativas_restantes == 0: #Verifica se há tentativas restantes, caso não haja ele bloqueia o terminal
    print("\nTerminal bloqueado.")
