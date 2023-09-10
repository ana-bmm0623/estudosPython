# Estruturas de Repetição

# Estrutura While

# É uma expressão booleana. Enquanto esta expressão for avaliada como verdadeira, o trecho de código será repitido

# Exemplo 1
i = 0
while i < 10:
    print(i)
    i += 1

# Exemplo 2
numero_sorteado = 12
palpite = 0

'''while palpite != numero_sorteado:
    palpite = int(input("Digite seu palpite (num inteiro    positivo) ou 0 (para encerar o jogo): "))
    if palpite == 0:
        print ("Encerando o jogo.")
        break
else:   
    print("Você acertou! O númeroo era ", numero_sorteado)'''

#Exemplo 3
'''while True:
    number = int(input("Digite um número inteiro positivo: "))
    if number < 0:
        print('Número inválido')
        continue
    fat = 1
    while number > 0:
        fat *= number
        number -= 1
    print("Fatorial: ", fat)'''

# Estrutura for
'''
    Loop contador;
    Relacionado com a função range;
        range(stop)
        range(start, stop)
        range(start, stop, step)
'''

#Exemplo 1
for i in range(1, 10, 2):
    print(i)