import os
import funcs

os.system('cls')

while True:
    print("1 - Contador")
    print("2 - Tabela de multiplicação")
    print("3 - Sair")
    inputCaba = int(input("Escolha (Apenas números): "))
    
    if inputCaba == 1:
        os.system('cls')
        funcs.contador()
        os.system('cls')
        
    elif inputCaba == 2:
        os.system('cls')
        funcs.Multi()
        os.system('cls')
        
    elif inputCaba == 3:
        os.system('cls')
        break
    
    else:
        print("\n\nOpção incorreta") 