"""
Tipo Inteiro
+  -  *  /  //  %  **
+=  -=  *=  /= //=
help(symbols)
CTRL + L limpa o console
"""

print("Tipo Inteiro")
num=55
print(num, "  ",1000000,"  ",1_000_000)
print(num,"  ",type(num))
num /= 2
print(num, "  ",type(num))
print(dir(num))
v1,v2 = 3, 14
print(f"v1 = {v1} e v2 = {v2}")

print("Tipo Float e Complexo")
valor = 3, 14   # tupla
print(f"{valor} - {type(valor)}")
valor = 3.14    # float
print(f"{valor} - {type(valor)}")

vint = int(valor)
print(f"Parte inteira de {valor} é {vint}")

numc = 3 + 4j
print(f"{numc} - {type(numc)}")
print(f"{numc} - parte real {numc.real}, parte imaginária {numc.imag} - ao quadrardo {numc ** 2}")

print("Tipo Booleano - True , False")
ativo = True
print(f"ativo: {ativo}, not ativo: {not ativo} - {type(ativo)}")
print(dir(ativo))

cond1, cond2 = True, False
print(f"cond1: {cond1}, cond2: {cond2}, cond1 and cond2: {cond1 and cond2}, cond1 or cond2: {cond1 or cond2}")
# cond1 and not cond2
print(f"5>6 {5>6}, 5<6 {5<6}, 7==7 {7==7}, 4!=7 {4!=7}")


print("Operações matemáticas básicas")
a = 11
b = 3
print(a, b)

print(f'A soma de {a} e {b} é {a + b}')
print(f'A subtração entre {a} e {b} é {a - b}')
print(f'A divisão entre {a} e {b} é {a/b}')
print(f'A multiplicação entre {a} e {b} é {a * b}')
print(f'O resto da divisão entre {a} e {b} é {a % b}')
print(f'A divisão inteira entre {a} e {b} é {a // b}')
print(f'{a} elevado a {b} é', a**b)

x = min(6, 12, 28, 2)
y = max(6, 12, 28, 2)
print(f"Máximo: {y}, Mínimo: {x}")

x = -17
print(f'módulo de {x} é {abs(x)}')

print("Operações matemáticas - import math")
import math
num = 81
print(f"Raiz quadrada de {num} é {math.sqrt(num)}")

num = math.pi
x = math.ceil(num)
y = math.floor(num)
print(f"{num}: Ceil: {x}, floor: {y}")

num = math.e
x = round(num)
y = math.trunc(num)
print(f"{num}: round: {x}, trunc: {y}")

num = math.pi/6
x,y,z = math.sin(num), math.cos(num), math.tan(num)
print(f"angulo de {round(math.degrees(num))} graus: sin: {x}, cos: {y}, tan: {z}")

p = [3]
q = [1]
print (math.dist(p, q))

p = [3, 3]
q = [6, 12]
print (math.dist(p, q))

print(math.exp(65))
print(math.exp(-6.89))

print(math.log(100))
print(math.log(math.exp(65)))
print(math.log(math.e))
print(math.log(1))