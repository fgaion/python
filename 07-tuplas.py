"""
Tuplas ou Tuples  -  (  )
PArecidas com listas mas tem 2 diferenças
1) representadas por parênteses ()
2) são imutáveis
"""
print(type(()))
tupla1 = (1 ,2, 3)
print(type(tupla1))
print(dir(tupla1))
print(f'Tupla 1: {tupla1}')

tupla2 = 1, 2, 3, 4, 5, 6
print(f'Tupla 2: {tupla2}')

tupla3 = (10)  # não é uma tupla
print(f'tupla3 = (10)  type: {type(tupla3)}')
tupla3 = (10, )  # é uma tupla
print(f'tupla3 = (10, )  type: {type(tupla3)}')

tupla4 = tuple(range(11))
print(f'Tupla 4: {tupla4}')
tupla4 = tuple((x, x*x, x*x*x) for x in range(11))
print(f'Tupla 4: {tupla4}')

tupla5 = ("Curso de Python","Django essencial")
c1,c2 = tupla5
print(f'c1 = {c1}  c2 = {c2}')

# numa tupla que contenha uma lista, a lista pode ser mudada
t1 = (1, "teste", 3.14 , [2,5,6])
print("t1=",t1)
t1[3][0] =10
print("t1=",t1)
t1[3].append(15)
print("t1=",t1)
# t1[0] = 13.57 #erro - nã0 pode alterar o valor
# print("t1=",t1)

print(f"tupla1 + tupla2 :{tupla1+tupla2}")
print(f"2*tupla1 + 3*tupla2 :{2*tupla1+3*tupla2}")

for k in t1:
    print(k,end='; ')

print("\n")
for ind,k in enumerate(t1):
    print(f"ind: {ind}  valor: {k}", end='  ;  ')