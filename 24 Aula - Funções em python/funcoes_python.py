# Local das funções em Python

# Declarando uma função em Python
# Obs: Na declaração da função é obrigatório colocar o def

# =====================================================================
# 1ª Função em Python (Sem Parâmetro e sem Retorno)

def soma(): 
    a = 80
    b = 100
    resSoma = a + b
    print(f"{a} + {b} = {resSoma}")

# Teste de Chamada com a função soma ()
# soma()

# =====================================================================    
# 2ª Função em Python (Com Parâmetro e sem Retorno)

def multi(c1):
    c2 = 5
    resMulti = c1 * c2
    print(f"{c2} X {c1} = {resMulti}")   
    
# =====================================================================
# 3ª Função em Python (Com vários Parâmetros e sem Retorno)

def corinthians(palmeiras, saoPaulo, santos):
    flamengo = palmeiras + saoPaulo
    print(santos, flamengo)
    
# Teste de chamada da função corinthians
a = 10
b = 30.50
c = "O resultado da conta é:"
corinthians(a, b, c)