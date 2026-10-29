import os
import time

# Contador

def contador():
    while True:
        Input = input("Pronto para o contador? (Y/n): ")
            
        contador = 300
        if Input == "Y" or Input == "y":
            while contador > 0:
                print(f"Valor do contador {contador}")
                time.sleep(0.01)
                contador -= 1
                
            print("\n\nPronto!!!")
            
            Input = input("Quer ver de novo? (Y/n): ")
            if Input == "N" or Input == "n":
                print("Voltando!!!")
                time.sleep(1)
                return
            elif Input == "Y" or Input == "y":
                print("\nReiniciando o contador...\n")
                time.sleep(1)
                os.system("cls")
            else:
                print("\nOpção inválida!!")
                os.system('cls')
                
        elif Input == "N" or Input == "n":
            print("\nVoltando")
            time.sleep(1)
            return
        else:
            print("\nOpção inválida!!")
            os.system('cls')
            
# Multiplicaçao

def Multi():
    while True:
        print("=== Tabuada do 2 ===\n\n")
            
        numero = 0
        while numero <= 10:
            print(f"2 X {numero} = {numero * 2}")
            time.sleep(0.01)
            numero += 1
                
        inputCaba = input("\nPronto!!! Quer ver denovo? (Y/n): ")
            
        if inputCaba == "N" or inputCaba == "n":
            os.system('cls')
            print("Voltando...")
            time.sleep(1)
            
            return
        elif inputCaba == "Y" or inputCaba == "y":
            os.system('cls')
            print("Reiniciando a tabuada...")
            time.sleep(1.5)
        
        else: 
            os.system('cls')
            print("Opção inválida!!!")
            print("reiniciando a tabuada...")
            time.sleep(1.5)
        