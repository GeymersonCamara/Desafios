'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela
ocorre.
'''

texto = input("Digite seu texto sem nenhum caractere especial:").lower()
letra = input("Qual letra deseja encontrar e saber a quantidade?")

if letra in texto:
    print("Encontrado", texto.count(letra))
else:
    print("não existe essa letra no texto.")