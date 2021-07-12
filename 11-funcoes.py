"""
Funções
nome da função: letras minúsculas separadas por underline
palavra reservada "def"
parâmetros de entrada são opcionais
pode ou não haver retorno na função
corpo da função deve ser indentado
Docstring
*args - é um parâmetro de entrada (param extras como tupla)
**kwargs - parâmetros extras nomeados - transforma em dicionário
ordem dos parâmetros numa função: parâmetros obrigatóris, *args, parâmetros default, **kwargs
"""
import math
from random import random, randint

cores = ['vermelho', 'azul', 'amarelo', 'verde', 'branco']
print(f"cores: {cores}")
numeros = [1,2,5,2,1,7,6,5,1,3,2,1,8,9,7,6,5,1,3,4,2,1,3,4,5,2,3,7,8,6,5]
print(f"numeros: {numeros}")

def hello_word():
    print("Hello Word! - print da função hello_word()")

def equacao_2grau():
    """Docstring: Calcula as raízes de uma equação do 2o grau do tipo ax^2 + bx + c = 0"""
    print("Equação do 2o grau - Entre com os valores de a, b, c na equação ax^2 + bx + c = 0")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    print(f"Equação: {a}x^2 + {b}x + {c} = 0")
    delta = b*b -4*a*c
    if (delta >= 0):
        print("delta = ",delta)
        x1 = (-b + (delta ** 0.5))/(2*a)
        x2 = (-b - (delta ** 0.5))/(2*a)
        print(f"x1 = {x1}  e  x2 = {x2}")
    else:
        print("Equação sem soluções reais")

def soma_numeros():
    return sum(numeros)

def joga_moeda():
    valor = random()
    if ( valor > 0.5):
        return 'cara'
    return 'coroa'

def joga_dado():
    return(randint(1,6))

def soma_lista_numeros(lista_numeros):
    return sum(lista_numeros)

def quadrado(numero):
    return(numero*numero)

def cubo(numero):
    return(numero**3)

def equacao_2grau_param(a,b,c):
    """Docstring: Calcula as raízes de uma equação do 2o grau do tipo ax^2 + bx + c = 0"""
    print(f"Equação: {a}x^2 + {b}x + {c} = 0")
    delta = b*b -4*a*c
    if (delta >= 0):
        print("delta = ",delta)
        x1 = (-b + (delta ** 0.5))/(2*a)
        x2 = (-b - (delta ** 0.5))/(2*a)
        return x1,x2
    else:
        return math.nan, math.nan

def imprime_impares(lista_numero):
    for n in lista_numero:
        if n % 2 != 0:
            print(n,end=", ")
    print("\n")

def exponencial(num, pot=2):
    return(num ** pot)

def distancia_2pontos(xa=0,ya=0,xb=0,yb=0):
    return(math.sqrt((xb-xa)**2 + (yb-ya)**2))

#usando *args
def soma_varios_numeros(*args):
    print(f"args: {args}")
    return(sum(args))

#usando **Kwargs
def pessoas_cores(**kwargs):
    print(f"kwargs: {kwargs}")
    for p,c in kwargs.items():
        print(f"A pessoa {p.title()} gosta da cor {c}")

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} - {kwargs['sobrenome']}"

#Chamadas das funções
hello_word()
hw = hello_word()
hw

#equacao_2grau()

soma = soma_numeros()
print(f"soma lista de números= {soma}")

num_jogadas = 5
for k in range(num_jogadas):
    print(f"moeda - jogada {k+1}: {joga_moeda()}")

num_jogadas = 10
for k in range(num_jogadas):
    print(f"dado - jogada {k+1}: {joga_dado()}")

soma = soma_lista_numeros(numeros)
print(f"soma lista de números= {soma}")

num = 8
print(f"o quadrado de {num} e' {quadrado(num)}")
print(f"o cubo de {num} e' {cubo(num)}")

x1,x2 = equacao_2grau_param(1,0,-4)
print(f"x1 = {x1}  e  x2 = {x2}")
x1,x2 = equacao_2grau_param(b=5,c=2,a=2,)
print(f"x1 = {x1}  e  x2 = {x2}")
print(help(equacao_2grau_param))
print(equacao_2grau_param.__doc__)

print("\nImpares: ",end=" ")
imprime_impares(numeros)

print("Exponencial: ")
print(exponencial(3))
print(exponencial(3,4))

print("Distancia entre dois pontos: ")
print("(5,4) e (1,1): ", distancia_2pontos(4,4,0,1))
print("(4,3) e (0,0): ", distancia_2pontos(4,3,0,0))
print("(4,3) e default(0,0): ", distancia_2pontos(4,3))
print("default(0,0) e default(0,0): ", distancia_2pontos())

print("Usando *args: ")
print("Soma:",soma_varios_numeros())
print("Soma:",soma_varios_numeros(1,2))
print("Soma:",soma_varios_numeros(5,3,7,2))
print("Soma:",soma_varios_numeros(3.14,2.72,0.176,2))
numeros = [3, 10, 6, -8, 12, 7, 0, 2]
print("Soma:",soma_varios_numeros(*numeros))  #*numeros desempacota a lista de numeros

print("Usando **kwargs: ")
pessoas_cores()
pessoas_cores(Gelina='Rosa',Romeu='Azul',Melzinha='Vermelho',Tel='Verde')
pessoas_cores(a=1,b=2,c=3,Gelina='Rosa',Romeu='Azul',Melzinha='Vermelho',Tel='Verde')

nomes = {'nome':'Gelina','sobrenome':'Speaker'}
print("Desempacotando kwargs:", mostra_nomes(**nomes))