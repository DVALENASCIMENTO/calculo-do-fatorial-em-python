#escreva um programa em python que solicite ao usuário informar um número inteiro.
# O programa deve calcular o valor do fatorial e imprimir o resultado para o usuário.
# Autor: Diego Vale do Nascimento - 07/10/2022
print('Cálculo do Fatorial')
from math import factorial
n = int(input('Digite um número inteiro: '))
f = factorial(n)
print('O fatorial de {} é {}.' .format(n, f))