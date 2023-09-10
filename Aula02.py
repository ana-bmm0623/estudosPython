#%%
# Desvio Condicional

'''
    Em programação, o controle de fluxo determina a ordem em que o código é executado;

    Essencial para tornar nossos programas dinâmicos e capazes de tomar decisões com base em diferentes condições;

    Permite que o programa tome decisões e execute um bloco de código específico com base em determinadas condições pré-definidas.
'''
# Desvio Simples

# O mais simples de todos os desvios condicionais

x = 10
if x > 0:
    print(" x é positivo")
print("fim do programa")

#Desvio Condicional com Else (composto)

#Outra forma de desvio condicional que permite que o código reaja quando a condição escificada não é atendida.

x = 0
if x > 0:
    print(" x é positivo") #True
else:
    print("x é negativo ou zero") #False
print("fim do programa")

#Desvio Aninhado

#Uma extensão do desvio condicional que permite verificar várias condições.

idade = 15

if idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 60:
    print('Você é adulto.')
else:
    print ("Você é um idoso.")

#Desvio Condicional Aninhado

#Existem outras formas de implementar desvios condicionais, como elif, nested if, etc.

x = 10
if x > 0:
    print(" x é positivo")
    if x % 2 == 0:
        print(" x é par")
    else:
        print("x é ímpar")
else:
    print("x é negativo ou zero")