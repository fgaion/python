"""
Listas  -  [  ]
list comprehension -
"""
import math
import random

quadrados = [x**2 for x in range(10)]
print(f"quadrados: {quadrados}")
quadrados = [(x, x**2) for x in range(10)]
print(f"quadrados: {quadrados}")
quadrados = [(math.sqrt(x), x, x**2) for x in range(10)]
print(f"sqrt(x), x, x^2: {quadrados}")


numeros = [1,2,3,4,5]
res = [num * 10 for num in numeros ]
print(f"numeros: {numeros}  res (x10): {res}")
pares = [num for num in numeros if not num % 2]
impares = [num for num in numeros if num % 2]
print(f"numeros: {numeros}  pares: {pares}")
print(f"numeros: {numeros}  impares: {impares}")

pontos = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f"pontos: {pontos}")
pontos = [(x, y, z) for x in [1,2,3] for y in [4,5,6] for z in [-1,0] ]
print(f"pontos: {pontos}")
arranjo = [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y]
print(f"arranjo (1,2,3) dois em dois: {arranjo}")


numeros = [-5,-3,-1,1,3,5]
res = [x*2 for x in numeros]
print(f"numeros: {numeros}  res(x*2): {res}")
res = [x for x in numeros if x >= 0]
print(f"numeros: {numeros}  res(>=0): {res}")
res = [abs(x) for x in numeros]
print(f"numeros: {numeros}  res(abs): {res}")

#pa com 10 termos com a1=0, r=5
a1,r,n = 0, 5, 10
pa = [x for x in range(a1,a1+r*n,r)]
print(f"pa com {n} termos com a1={a1}, r={r} : {pa}")

res=[str(round(math.pi, i)) for i in range(1, 6)]
print(f"res(pi): {res}")

string = 'abceayuiatreawbeujkautbrdha'
res=[letra.upper() for letra in string if (letra == 'a' or letra == 'b')]
print(f"res(string): {res}")
res=[ x.upper() if x=='a' else x for x in string]
print(f"res(string): {res}")

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
transposta = [[row[i] for row in matrix] for i in range(4)]
print(f"matriz: {matrix}   transposta: {transposta}")

matrix = [ [random.randint(0,10), random.randint(0,10), random.randint(0,10) ] for k in range(3) ]
print(f"matriz: {matrix}")

matrix = [ [random.randint(0,100) for col in range(5)] for lin in range(3)]
print(f"matriz: {matrix}")

matrix = [ ['x' if num%2 ==0 else 'O' for num in range(1,4)] for valor in range(1,4)]
print(f"matriz: {matrix}")
