"""
Dicionários  -  { chave : valor  }
Coleções do tipo chave/valor
não pode haver chaves repetidas
"""

print(type({}))
idades = {"Ana": 25, "Maria": 32, "João": 41}
print(type(idades))
print(dir(idades))
print(f"idades: {idades} \nChaves: {idades.keys()} \nValores: {idades.values()}")
print(f"Idades itens: {idades.items()}")
print("Idade da Ana: ",idades["Ana"])
#print("Idade da Jose: ",idades["Jose"])    #key error
print("Idade da Maria: ",idades.get("Maria"))
print("Idade da Jose: ",idades.get("Jose"))   # retorna None
print("Idade da Jose: ",idades.get("Jose","chave não encontrada"))


idades2 = dict(Jose=16, Gelina=20, Mel=84, Teco=30)
print(f"idades2: {idades2}")

idades3 = idades.copy()
idades3.update(idades2)
print(f"idades3: {idades3.items()}")

print("Inserindo Dados")
idades['Mel'] = 90
novo = {'Tel': 35}
idades.update(novo)
idades.update({'Tom':47})
print(f"idades: {idades}")

print("Atualizando Dados")
idades['Mel'] = 80
idades.update({'Tom':50})
print(f"idades: {idades}")

print("Removendo Dados")
nome = 'Ana'
x = idades.pop(nome)
print(f"Removido {nome} de idade {x} - idades: {idades}")
nome = 'Tel'
x = idades.pop(nome)
print(f"Removido {nome} de idade {x} - idades: {idades}")
nome = 'Maria'
del(idades['Maria'])
print(f"Removido {nome} de idade {x} - idades: {idades}")

#Remoção tipo Pilha - LIFO
x = idades.popitem()
print(f"Removido {x} - idades: {idades}")
x = idades.popitem()
print(f"Removido {x} - idades: {idades}")

print('Percorrendo um dicionário:')
for x in idades3:
    print(f"{x} tem {idades3[x]} anos",end='; ')
print('\nOutra maneira de fazer o mesmo:')
for x,y in idades3.items():
    print(f"{x} tem {y} anos",end='; ')

print('\nQuadrados de 0 a 10:')
quadrado = dict(list((x, x*x) for x in range(11)))
print(f"quadrados: {quadrado}")