"""
Listas  -  [  ]
funcionam como arrays dinâmicos e armazenam qualquer tipo de dados
"""
type([])
dir([])

lista1 = [1, 99, 4, 27, 13, 22, 3, 14, 44, 42, 27]
print(lista1)
lista2 = [ 'C', 'u', 'r', 's', 'o' ]
print(lista2)
lista3 = []
print(lista3)
lista4 = list(range(11))
print(lista4)
lista5 = list("Curso de Python")
print(lista5)

num =5
# num = int(input("Digite um número: "))
if num in lista4:
    print(f"Encontrei o número {num} na lista: {lista4}")
else:
    print(f"Não encontrei o número {num} na lista: {lista4}")

lista1.sort()
print(lista1)

lista5 = list("O Curso de Python".lower())
lista5.sort(reverse=True)
print(lista5)
letra = 'o'
print(f"Numero de letras {letra} em {lista5} é {lista5.count(letra)}")

print("Insert e Append")
print(lista1)
lista1.append(13)
print(lista1)
lista1.insert(0,13)
lista1.insert(1,13)
print(lista1)

lista1.extend([39,89,101])
print(lista1)
lista1 = lista1 + [40, 90, 102]
print(lista1)
lista2.extend(" de Python 3.x")
print(lista2)

print("Juntando duas listas e vendo o tamanho da lista")
lista6 = lista1 + lista2
#lista1.extend(lista2)
#lista6 = lista1
print(f"Lista6: {lista6} tem tamanho {len(lista6)}")

print("Invertendo uma lista")
print(lista1)
lista1.reverse()
print(lista1)
print(lista2)
print(lista2[::-1])

print("Copinado uma listaa")
lista6 = lista1.copy()
lista7 = lista1
print("Lista1:         ",lista1)
print("Lista6 (copia): ",lista6)
print("Lista7 ( = )    ",lista7)
lista6[0], lista7[0] = 1000, 2000
print("Lista1:         ",lista1)
print("Lista6 (copia): ",lista6)
print("Lista7 ( = )    ",lista7)

print("Removendo o último elemento da Lista - pop()")
lista1 = list(range(11))
print(lista1)
elem = lista1.pop()
print(f"Elemento removido: {elem} - Lista 1: {lista1}")

print("Removendo um elemento de uma posição da Lista - pop(ind)")
lista1 = list(range(10,21))
print(lista1)
elem = lista1.pop(4)
print(f"Elemento da posição {elem} removido - Lista 1: {lista1}")
elem = lista1.pop(0)
print(f"Elemento da posição {elem} removido - Lista 1: {lista1}")

lista1 = list(range(10,21))
elem=15
print("Lista1: ",lista1)
lista1.remove(15)
print(f"Elemento {elem} removido - Lista 1: {lista1}")

print("Lista1: ",lista1)
lista1.clear()
print("Limpando a lista com clear - Lista1: ",lista1)

print("Replicando várias vezes uma lista")
lista6 = 3 * [1,2,3]
print(lista6)
lista7 = 3 * list("teste,")
print(lista7)

curso = "Curso de Python, capítulo coleções: listas, tuplas, dicionários, etc"
print(curso," ->(split espaço )-> ",curso.split())
print(curso," ->(split virgula)-> ",curso.split(","))

listaCurso = curso.split()
print("listaCurso: ", listaCurso)
print("Transformando listaCurso em string")
curso = " ".join(listaCurso)
print("curso: ",curso)
curso = "_".join(listaCurso[::-1])
print("curso: ",curso)

lista6 = [2, 3.14, True, "Python", [1,10,100], 'X', 3+8J, 546783773627, (5, 8 , 12)]
print(f"Lista6: {lista6} - Type: {type(lista6)}")
for elem in lista6:
    print(f"Elem: {elem} - Type: {type(elem)}", end=" ; ")

print("\nSoma e produto dos elementos de uma lista com for")
lista1 = list(range(10,21))
soma,produto = 0,1
for elem in lista1:
    print(elem,end=", ")
    soma += elem
    produto *= elem
print(f"Soma = {soma} , produto = {produto}")

print("Percorrendo a lista nos dois sentidos\nLista 1: ",lista1)
for k in range(len(lista1)):
    print(lista1[k],lista1[-k-1],sep=",",end=" ; ")

print("\nLista e enumerate")
cores = ["azul", "verde", "amarelo", "vermelho"]
for ind,cor in enumerate(cores):
    print(f"indice: {ind}, cor: {cor}",end="; ")

cores2 = list(enumerate(cores))
print("\nCores2: ",cores2)

cor = "amarelo"
print(f"Indice do elemento {cor}: {cores.index(cor)}")

lista1 = [1, 27, 4, 99, 27, 13, 22, 3, 14, 44, 27, 42, 27]
listaInd = []
numero = 27
inicio = 0
print(f"Encontrar os indices do numero {numero} em {lista1}")
while True:
    try:
        ind = lista1.index(numero, inicio)
    except:
        break
    listaInd.append(ind)
    inicio = ind + 1

print(f"Lista de indices do elem {numero}: {listaInd}")

inic,fim,passo = 0, 10, 2
print("lista1: ",lista1)
print(f"Slice lista1[{inic}:{fim}:{passo}]: {lista1[inic:fim:passo]}")
inic,fim,passo = -1, -10, -2
print(f"Slice lista1[{inic}:{fim}:{passo}]: {lista1[inic:fim:passo]}")

print("\nTramsformando lista em tupla")
tupla1 = tuple(lista1)
print(tupla1," - ",type(tupla1))

print("Desempacotando uma lista")
n1,n2,n3 = lista1[0:3]
print("n1 = ",n1," n2 = ",n2," n3 = ",n3)