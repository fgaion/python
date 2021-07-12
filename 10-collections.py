"""
Collections:
módulo collections - high performance data type
https://docs.python.org/3/library/collections.html?highlight=collection#module-collections

counter
default dict
ordered dict
named tuple
deque
"""
#===================================================================================================================
from collections import Counter
print("Counter")
cnt = Counter()
for word in ['vermelho', 'azul', 'vermelho', 'verde', 'azul', 'azul']:
    cnt[word] += 1
print(cnt)

numeros = [1,2,5,2,1,7,6,5,1,3,2,1,8,9,7,6,5,1,3,4,2,1,3,4,5,2,3,7,8,6,5]
res = Counter(numeros)
print(type(res))
print(res)

frase = "Curso de Python - modulo collections counter"
print(Counter(frase))

dicio = {'vermelho':10, 'azul':5, 'verde':20}
print(dicio)
print(Counter(dicio))

texto = """Tribune. Faut-il reprendre la réforme des retraites, et si oui comment ? En France, les évolutions 
démographiques sont marquées par l’augmentation de l’espérance de vie plus que par la diminution de la fertilité.
 L’augmentation de l’espérance et de la qualité de vie est une très bonne nouvelle. Mais elle nécessite des ajustements,
  en particulier de trouver le bon équilibre entre travail et retraite. Sur la base des travaux d’Axel Börsch-Supan et 
  des vingt-trois autres membres de notre commission d’experts sur les grands défis économiques, réunie par le président
   de la République, nous plaidons pour l’adaptation du système de retraite et pour une série de mesures aidant les 
   seniors à travailler plus longtemps et incitant les entreprises à aménager leurs conditions de travail et à les 
   employer plus longtemps s’ils le veulent : par exemple, par un traitement des maladies chroniques en prévention et 
   en réparation, par une formation continue adaptée et par un aménagement des rythmes de travail et de transition 
   vie professionnelle-retraite."""
palavras = texto.split()
#print(palavras)
res = Counter(palavras)
print(f"palavras: {res}")
numPal=10
print(f"As {numPal} palavras mais frequentes: {res.most_common(numPal)}")

#===================================================================================================================
from collections import defaultdict
print("\ndefault dict")
s = [('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(sorted(d.items()))

s = 'curso de linguagem python'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))

dicio = defaultdict(lambda: 0)
print(f"dicio: {dicio}")
dicio['curso']="Linguagem Python"
print(f"dicio: {dicio}")
print(dicio['curso'])
print(dicio['outro'])  #não dá erro de "keyerror" e insere um elemento no dicionário {outro: 0]
print(f"dicio: {dicio}")

#===================================================================================================================
from collections import OrderedDict
print("\nordered dict")
s = [('vermelho', 1), ('verde', 2), ('amarelo', 3)]
dicio = dict(s) #não garante a ordem de inserção dos elementos
dicio['azul'] = 10
print(f"dicio: {dicio}")
dicio = OrderedDict(s) #garante a ordem de inserção dos elementos
dicio['azul'] = 10
print(f"dicio: {dicio}")

dic1 = {'a':1, 'b':2}
dic2 = {'b':2, 'a':1}
print(f"Dicionario tradicional dic1={dic1} e dic2={dic2}: dic1 == dic2  {dic1==dic2}")

dic1 = OrderedDict({'a':1, 'b':2})
dic2 = OrderedDict({'b':2, 'a':1})
print(f"Dicionario ordered dic1={dic1} e dic2={dic2}: dic1 == dic2  {dic1==dic2}")

#===================================================================================================================
from collections import namedtuple
print("\nnamed tuple")
tupla = (1,2,3)
print(f"tupla tradicional = {tupla}")

#declaração da named tuple - forma 1
pessoa = namedtuple('pessoa','nome sexo idade')

#declaração da named tuple - forma 2
pessoa = namedtuple('pessoa','nome, sexo, idade')

#declaração da named tuple - forma 3
pessoa = namedtuple('pessoa',['nome', 'sexo', 'idade'])

#usando uma named tuple
gelina = pessoa(nome="Angelina",sexo="F",idade=20)
print(f"named tuple gelina: {gelina}")
print(f"A pessoa {gelina[0]} tem {gelina[2]} anos")
print(f"A pessoa {gelina.nome} do sexo {gelina.sexo} tem {gelina.idade} anos")

#===================================================================================================================
from collections import deque
print("\ndeque")
d = deque('ghi')
for elem in d:
    print(elem.upper(),end=", ")

d.append('j')
d.appendleft('f')
print("\ndeque = ",d)
print(f"d.pop = {d.pop()}")
print(f"d.popleft = {d.popleft()}")

print("list(d) = ",list(d))
print(f"d[0]={d[0]}  -  d[-1]={d[-1]}")
print("list reversed: ",list(reversed(d)))

print(f"h in deque d : {'h' in d}")

d.extend('jkl')
print("extend jkl em deque = ",d)

d.rotate(1)
print("roatate 1 = ",d)

d.rotate(-1)
print("roatate -1 = ",d)

print("reversed deque: ",deque(reversed(d)))

d.clear()
#d.pop()  #vai gerar um erro - remover de um deque vazio

d.extendleft('abc')
print("deque: ",d)
