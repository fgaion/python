"""
Dicionario  -  { chave: valor }
dict comprehension -
"""
import math
import random

idades = {"Ana": 25, "Maria": 32, "João": 41}
print(f"idades: {idades} \nChaves: {idades.keys()} \nValores: {idades.values()}")

numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(f"nuneros: {numeros}")
quadrado = {chave:valor**2 for chave,valor in numeros.items() }
print(f"quadrados: {quadrado}")

print('\nQuadrados de 0 a 10:')
quadrado = {x: x*x for x in range(10)}
#quadrado = dict(list((x, x*x) for x in range(10)))
print(f"quadrados: {quadrado}")

chaves ="xyzkw"
valores =[10,20,30,40,50]
dicio = {chaves[k]:valores[k] for k in range(len(chaves))}
print(f"dicio: {dicio}")

numeros = [1,2,3,4,5,6,7]
dicio = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(f"dicio: {dicio}")