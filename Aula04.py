# Funções e módulos

'''
    Uma função é um bloco de código que pode ser usado para executar uma tarefa específica;

    As funções são úteis para tornar seu código:
    - mais organizado;
    - reaproveitável;
    - legível.
'''

# Exemplo da construção de uma função:

'''
    def nome_da_função(argumentos):
        corpo da função

    onde:
    nome_da_função é o nome da função para invocá-la;
    argumentos são os argumentos que a função recebe;
    corpo da função é o código que a função executa.
'''

# Função sem parâmetros e sem retorno


def ola_mundo():
    print("Hello, World!")

ola_mundo()

# Função com parâmetros e sem retorno

def ola_mundo(nome):
    print('Hello, ' + nome + "!")

ola_mundo("João")  # Impressão: Hello, João"

# Função com parâmetros e com retorno
def soma(a, b):
    return a + b

soma(2, 2) # Chamada da função: 4

# Função sem parâmetros e com retorno

def get_pi():
    return 3.14159265359

get_pi() # Chamada da função: 3.14159265359

# Função com tipagem de parâmetros e retorno

def soma (a: int, b: int) -> int:
    return a + b

soma(2, 2) # Chamada da função: 4

# Benefícios da utilização de funções

'''
    - Melhor organização;
    - Reutilização de código;
    - Melhor legibilidade;
    - Facilidade de manutenção;
'''

# Boas práticas

'''
    - Uma função realiza uma tarefa específica;
    - Boas funções são curtas e de fácil compreensão.
'''

# Módulo

'''
    Um módulo é um arquivo de código Python que pode ser instalado e importando em seu projeto;

    Aproveitamento de código;
    Modularização do projeto.
'''

# Importando o módulo math
import math

print(math.sqrt(16)) #imprime: 4.0
