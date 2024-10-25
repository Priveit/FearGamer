import random 
import os 
import sys 
import time
import webbrowser

def janelas():
    url="https://www.youtube.com/watch?v=NRqkWo9w1Vo"
    for i in range(50):
        webbrowser.open(url)




def sortear():
    print("haihai")
    opcoes = 6

    #sorteia um número de 1 a 6
    sorteado = random.randint(1, opcoes)


    try:   
        escolha = int(input(f"Escolha um número entre 1  e {opcoes}: "))
        if escolha > opcoes or  escolha < 1:
            print("Fora de intervalo!")
            sortear()
            
    
    except  ValueError as mensagem:
        print(f"Entrada inválida! Insira  um número valido! {mensagem} ")
        sortear()
        

    if escolha == sorteado:
        print("se fodeu legal")
        janelas()
        time.sleep(2)
        os.system("shutdown /s /t 1 ")

    else:
        print("você está salvo,por enquanto! ;) ")
        sortear()



sortear()
