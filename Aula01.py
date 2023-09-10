# %%
# Comentário de linha única

# print é uma função que imprime algo na tela. O "Hello world" é o argumento da função
print("Hello World")

''' 
Comentários de múltiplas linhas
'''
# A declaração é fracamente tipada e é dinâmica
nome = 'Maria'

# Inteiros (int) - usado para números inteiros
num = 10
print(num)
print(type(num))  # Saída <class 'int'>

# Números de ponto flutuante (float) - usado para números reais
pi = 3.14
print(pi)
print(type(pi))  # Saída <class 'float'>

# Strings (str) - usados para textos
greeting = 'Hello, World!'
print(greeting)
print(type(greeting))   # Saída: <class 'str'>

# Booleanos (bool) - usados para valores verdadeiros ou falsos
is_python_fun = True
print(is_python_fun)
print(type(is_python_fun))    # Saída: <class 'bool'>

# Listas (list) - usados para coleções ordenadas de valores
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))  # Saída <class 'list'>

# Tuplas (tuple) - semelhante às listas, mas imutáveis
coordinates = (10.0, 20.0)
print(coordinates)
print(type(coordinates))     # Saída: <class 'tuple'>

# Dicionários (dict) - usados para coleções de pares chave-valor
person = {"name": "Alice", "age": 25}
print(person)
print(type(person))  # Saída <class 'dict'>

# Exemplos de Conversão de tipos de dados
text = "10"
num = 5
print(int(text) + num)

a = 10
b = 20
print("a = " + str(a) + "; b = " + str(b))

# Operadores Aritméticos
'''
    Adição: +
    Subtração: -
    Multiplicação: *
    Divisão: /
    Resto de divisão: %
    Potência: **
'''

# Operadores de Atribuição
'''
     = Atribuição simples
    += Soma o valor da variável com outro valor e atribui o resultado
    -= Subtrai o valor da variável com outro valor e atribui o resultado
    *= Multiplica o valor da variável com outro valor e atribui o resultado
'''

# Operadores Relacionais
'''
    == Igual
    != Diferente
    > Maior que
    < Menor que
    >= Maior ou igual
    <= Menor ou igual
'''

# Exemplos de Operadores Relacionais

# Operador ==
if a == b:
    print("a é igual a b")
else:
    print("a é diferente de b")

# Operador !=
if a != b:
    print("a é diferente de b")
else:
    print("a é igual a b")

# Operdor >
if a > b:
    print('a é maior do que b')
else:
    print("a é menor ou igual a b")

# Operdor <
if a < b:
    print('a é menor do que b')
else:
    print("a é maior ou igual a b")

# Operadores Lógicos
'''
    and -> retorna true se ambas as expressões forem verdadeiras
    or -> retorna true se uma das duas expressões for verdadeira
    not -> inverte o valor de uma expressão booleana
'''

# Exemplos de Operadores Lógicos

# Operador and
if a < 100 and b < 100:
    print("a e b são menores que 100")
else:
    print("a e b são maiores ou iguais a 100")

# Operador or
if a < 100 or b < 100:
    print("a ou b é menor que 100")
else:
    print("a ou b são maiores ou iguais a 100")

# Operador not
if not (a > b):
    print("a não é maior que b")
else:
    print("a é maior que b")

# Strings e Indexação
'''
    Strings são sequências de caracteres em Python;

    Podemos acessar caracteres individuais usando indexação;

    A indexação em Python começa em O;
'''

# Exemplos de Indexação

frase = "Python é incrível!"

# Indexação positiva:

frase[0]  # retorna "P"

# Indexação negativa:

frase[-1]  # retorna "!"

# Slicing

# Slicing permite obter partes de uma string usando intervalos de índices

print(frase[7:13])  # Saída "é incr"

# Operador in

'''
    O operador "in" é usado para verificar se um valor está presente em uma sequência (como uma string, lista, tupla, conjunto, etc.);

    O resultado é um valor booleano (True ou False).
'''
texto = "Olá, como você está?"
print('como' in texto)  # Saída: True
print('Python' in texto)  # Saída: False

# Operador is
# O operador "is" é usado para verificar se duas variáveis se referem ao mesmo objeto na memória.
x = [1, 2, 3]
y = x
print(x is y) # Saída: True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # Saída: False

# Importação de módulos

# Em Python,  as bibliotecas são módulos ou pacotes que fornecem funcionalidades adicionais ao código.

# Importando apenas math
import math
print(math.sqrt(16))

# Apelidando math como m
import math as m
print(m.sqrt(16))

# Importando apenas a função sqrt de math
from math import sqrt
print(sqrt(9))