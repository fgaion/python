"""
Tipo string
Entre aspas simples ''
Entre aspas simples ""
Entre aspas simples triplas ''' '''
Entre aspas duplas triplas
caracter de escape \  exemplos \\  \"  \'
"""

nome = 'Curso de python'
print(nome)
print(type(nome))

nome = "Python's Curse"
print(nome)

nome = 'Curso \n Python'
print(nome)

nome = """Curso
Python"""
print(nome)

nome="c:\\home\\user\\normas"
print(nome)

nome = 'CUrSo dE PytHon'
print("upper: ",nome.upper())
print("lower: ",nome.lower())
print("capitalize: ",nome.capitalize())
print("title: ",nome.title())
print("split espaço: ",nome.split())
print("len(nome): ",len(nome))

nome = "ab, cd, ef, gh, ij, kl"
print(nome.split(),sep=',')
print(nome[0:6])
tam=len(nome)
print(nome[tam-6:tam])
print(nome[-6:-1],nome[-1])
print(nome[::-1])

print(nome.replace(',',';'))

a = 'programação python'
print(a)
c = a.replace('o', 'a')
print(c)
print(f"posição a: {c.find('a')}, posição m: {c.find('m')}, psoição y: {c.find('y')}")

#remove espaços em branco do início e do inal
c = "     programação     linguagem      python      "
print(f"|{c}|")
f = c.strip()
print(f)
f = c.replace(' ','')
print(f)