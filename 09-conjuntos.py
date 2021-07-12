"""
sets ou Conjuntos  -  { valor1, valor2, valor3 ...  }
Teoria dos cojuntos da matemática
os conjuntos não possuem valores duplicadoe nem ordenados
os elementos de um conjunto não são indexados
"""

frutas = {"banana", "maça", "laranja" }
numeros = set({1,3,2,10,3,5,5,1,6,7,9,8,1,4,2})
letras = set("Curso de Python")
listaset = set([8,3,1,8,4,2,4,2,4,8])
print("frutas: ",frutas)
print(type(frutas))
print("numeros: ",numeros)
print(dir(numeros))
print("letras: ",letras)
print("listaset: ",listaset)

num = 3
if num in numeros:
    print(f"O numero {num} pertence a {numeros}")
else:
    print(f"O numero {num} não pertence a {numeros}")

lista = [1,3,2,10,3,5,5,1,6,7,9,8,1,4,2]
print(f"lista: {lista} - tam: {len(lista)}")
tupla = (1,3,2,10,3,5,5,1,6,7,9,8,1,4,2)
print(f"tupla: {tupla} - tam: {len(tupla)}")
dicio = {}.fromkeys((lista),'xpto')
print(f"dicionario: {dicio} - tam: {len(dicio)}")
conj = {1,3,2,10,3,5,5,1,6,7,9,8,1,4,2}
print(f"conjunto: {conj} - tam: {len(conj)}")

for x in frutas:
    print(x,end=", ")
print("\n")
frutas.add("pera")
frutas.add("uva")
print(f"frutas: {frutas}")
fr = "banana"
frutas.remove(fr)   #remove gera erro se o elemento não existe
print(f"remove: {fr} - frutas: {frutas}")
frutas.discard("banana")  #discard não gera erro se o elemento não existe
print(f"discard: {fr} - frutas: {frutas}")
x = frutas.pop()  # remove o primeiro elemento
print(f"pop x: {x} - frutas: {frutas}")
frutas.clear()
print(f"frutas: {frutas}")

print("\nOperaões em conjuntos:")
frutas1 = {"banana", "maça", "laranja" }
frutas2 = {"banana","pera","uva"}
print(f"frutas1: {frutas1}")
print(f"frutas2: {frutas2}")

print("União")
frutas = frutas1.union(frutas2)
#frutas = frutas1 | frutas2
print(f"frutas1: {frutas1}  union  frutas2: {frutas2} = frutas: {frutas}")
frutas1.update(frutas2)
print(f"frutas1.update(frutas2): {frutas1}")
x = frutas2.issubset(frutas)
if x:
    print(f"{frutas2} é um subconjunto de {frutas}")

print("Diferença")
frutas1 = {"banana", "maça", "laranja" }
frutas2 = {"banana","pera","uva"}
frutas = frutas1.difference(frutas2)
#frutas = frutas1 - frutas2
print(f"frutas1: {frutas1}  diference  frutas2: {frutas2} = frutas: {frutas}")
frutas1.difference_update(frutas2)
print(f"frutas1.difference_update(frutas2): {frutas1}")

print("Intersecção")
frutas1 = {"banana", "maça", "laranja" }
frutas2 = {"banana","pera","uva"}
frutas = frutas1.intersection(frutas2)
#frutas = frutas1 & frutas2
print(f"frutas1: {frutas1}  intersection  frutas2: {frutas2} = frutas: {frutas}")
frutas1.intersection_update(frutas2)
print(f"frutas1.intersection_update(frutas2): {frutas1}")

print("Symetric")
frutas1 = {"banana", "maça", "laranja" }
frutas2 = {"banana","pera","uva"}
frutas = frutas1.symmetric_difference(frutas2)
print(f"frutas1: {frutas1}  symetric_difference  frutas2: {frutas2} = frutas: {frutas}")
frutas1.symmetric_difference_update(frutas2)
print(f"frutas1.symetric_difference_update(frutas2): {frutas1}")