"""
Loops
for item in interval:
    #cmds do loop

Ranges

while
"""
print("\nLooping for")
print("String")
nome = "Curso de Python"
for letra in nome:
    print(letra,end=',')

print("\nLista")
lista = [10, 30, 50, 70, 90]
for elem in lista:
    print(elem,end=' - ')

print("\nRange 1 a 10")
for k in range(1,10):
    print(k,end=' ')
print("\nRange com step")
for k in range(0,20,2):
    print(k,end=' ')

print("\nEnumerate string")
for i,v in enumerate(nome):
    print(i,' ',nome[i],' ',v,end='; ')
print("\nEnumerate lista")
for i,v in enumerate(lista):
    print(i,' ',lista[i],' ',v,end='; ')

print("\nLista a partir de Enumerate")
lenum = list(enumerate(nome))
for elem in lenum:
    print(elem,end=',')

print("\nLista a partir de Enumerate - outra forma")
for valor in enumerate(nome):
    print(valor,end=',')
"""
Tabela de Emojis Unicodes: https://apps.timwhitlock.info/emoji/tables/unicode
Original: U+1F60C
Modificado: U0001F60C
"""
print("\nEmojis")
for num in range(1,5):
    print('\U0001F60C'*num)

#RANGES
print("\nRange forma 1")
for num in range(10):
    print(num,end=' ')

print("\nRange forma 2")
for num in range(10,16):
    print(num,end=' ')

print("\nRange forma 3")
for num in range(50,100,5):
    print(num,end=' ')

print("")
for num in range(200,100,-10):
    print(num,end=' ')

print("\nLista e Range")
lista = list(range(10))
print(lista)

print("\nLooping while")
num=1
while num < 10:
    print(num,end=',')
    num += 1

print("\nLooping while com string")
resp = ''
while resp != 'sim':
    resp = input("Sair (sim/não) ")

print("\nLooping com break")
resp = ''
while True:
    resp = input("Digite fim para sair ")
    if resp == "fim":
        break


