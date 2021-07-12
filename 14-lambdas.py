""""
funções lambdas - funções anônimas
map, filter, reduce, any e all, generators, sorted, min e max, reversed, len, abs, sum, round, zip
"""
#========================= Lambda ===============================================
import math
import random
import statistics as st

print("Lambdas")
def quadrado(x):
    return x*x

num = 5
print(f"(def quadrado) quadrado de {num} é {quadrado(num)}")

q = lambda x: x*x
print(f"(lambda) quadrado de {num} é {q(num)}")

nome_completo = lambda nome,sobrenome : nome.strip().title() + ' ' + sobrenome.strip().title()
a = "  gelina  "
b = "   SPEAKER   "
print(nome_completo(a,b))

autores = ["Raul Pompeia", "Machado de Assis", "Eça de Queiros", "José de Alencar", "Aloisio de Azevedo" ]
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)  #imprime ordenado pelo sobrenome

def gera_quadratica(a,b,c):
    """
    retorna f(x) = a * x^2 + b * x + c
    """
    return lambda x: a*x**2 + b*x + c

teste = gera_quadratica(2,3,-5)
print(teste(0))
print(teste(1))
print(teste(2))
print(gera_quadratica(2,3,-5)(3))

#pa com 10 termos com a1=0, r=5
a1,r,n = 0, 5, 10
pa = [x for x in range(a1,a1+r*n,r)]
print(f"pa com {n} termos com a1={a1}, r={r} : {pa}")

pa = lambda a1, r, n: [x for x in range(a1, a1 + n * r, r)]
print(pa(0,5,10))
print(pa(3,7,5))
print(pa(10,-5,10))

#========================= map ===============================================
print("\nMap")
def areaCirculo(raio):
    return math.pi * raio * raio

ra=2
print(f"Circulo com raio {ra} tem área {areaCirculo(ra)}")

raios = [2,4,5,7,8,10,12]
areas = [areaCirculo(ra) for ra in raios]
print(f"Raios: {raios} Áreas: {areas}")

areas = map(areaCirculo, raios)
print(f"map - areas:{areas} e type(areas): {type(areas)}")
print(f"map - Raios: {raios} Áreas: {list(areas)}")

areas = list(map(lambda r: math.pi*r*r , raios))
print(f"map com lambda type(areas): {type(areas)}")
print(f"map com lambda - Raios: {raios} Áreas: {areas}")

pontos1 = [(x, y) for x in [1,2,3] for y in [3,4] ]
pontos2 = [(x, y) for x in [2,3,4] for y in [2,5] ]
distancias = list(map(lambda p1,p2: (p1,p2,math.dist(p1,p2)), pontos1,pontos2))
print(f"map com lambda distancias: {distancias}")

#========================= filter ===============================================
print("\nFilter")
valores = (1,2,3,4,5,6)
media = sum(valores)/len(valores)
print(f"valores:{valores} e media: {media}")

#filtrar valores acima da média
numDados = 10
dados = [ round(10*random.random(),2) for n in range(numDados)]
media = st.mean(dados)
print(f"Dados: {dados} - Média: {media}")

res = list(filter(lambda x: x > media, dados))
print(f"(Filter) Valores acima da media {media}: {res}")
res = [ x for x in dados if x > media]
print(f"(Lista ) Valores acima da media {media}: {res}")

paises = ['', 'Argentina', '','Brasil','','Chile','','Equador','','','Uruguai','']
print(f"Paises: {paises}")
res = [x for x in paises if x ]
print(f"(Lista) Paises: {res}")
res = filter(None,paises)
print(f"(Filter 1) Paises: {list(res)}")
print(f"Paises (2a listagem vazia): {list(res)}")  #na segunda chamada res fica vazia
res = list(filter(None,paises))
print(f"(Filter 2) Paises: {res}")
print(f"Paises (2a listagem não vazia): {res}")  #na segunda chamada res NÂO fica vazia

usuarios = [
    {"username":"Angelina", "tweets":["msg Ang tweet 1","msg Ang tweet 2","msg Ang tweet 3"]},
    {"username":"Melzinha", "tweets":["msg Mel tweet 1","msg Mel tweet 2"]},
    {"username":"Romeu", "tweets":[]},
    {"username":"Tel", "tweets":["msg Tel tweet 1","msg Tel tweet 2","msg Tel tweet 3"]},
    {"username":"Teco", "tweets":["msg Teco tweet 1","msg Teco tweet 2","msg Teco tweet 3","msg Teco tweet 4"]},
    {"username":"Tom", "tweets":[]},
]
print(f"Usuários: {usuarios}")
inativos = list(filter(lambda usuario: not usuario['tweets'] , usuarios ))
print(f"Usuários inativos: {inativos}")

num_tweets = [ (item['username'],len(item['tweets'])) for item in usuarios ]
print(f"Usuários e Qtde de tweets: {num_tweets}")

#========================= Reduce ===============================================