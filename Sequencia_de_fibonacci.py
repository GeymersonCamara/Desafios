'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele
calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

import math

def quadradoPerfeito(x):
    raizQ = int(math.sqrt(x))
    return raizQ * raizQ == x

def fibonacci(n):
    # Verifica as duas condições
    return quadradoPerfeito(5 * n * n + 4) or quadradoPerfeito(5 * n * n - 4)

anterior = 0
proximo = 0
qtd = int(input("Até qual número deseja ver a sequencia fibonacci?"))

n = int(input("Qual número positivo você que verificar? "))

if (fibonacci(n)):
    print(f"{n} pertence à série de Fibonacci.")
else:
    print(f"{n} não pertence à série de Fibonacci.")
    
while(proximo < qtd):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1
print("...")
    

'''
    Para fazer esse desafio eu usei a biblioteca math do python.
    
    Fiz duas funções, uma para calcular o quadrado perfeito e outra
    duas sentenças matematicas para verificar se o numero pertence a serie
    de fibonacci.
    
    Em seguda fiz uma estrutura de seleção composta para devolver para o usuario
    o que ele deseja.
'''