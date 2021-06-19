"""
dir -> apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinado dado ou variável

help -> apresenta a documentação (ajuda) para um detreminado item

"""
# import this
print(dir("Python"))
print("PYTHON".lower())
print("python".upper())
print("python".title())
# help("PYTHON".lower)
print("curso.python.dir.e.help.split.com.ponto".split(sep="."))
print("curso python dir e help split com espaço".split())

print(dir(4))
num=4
# help(num.real)
num = 4 + 3j
print(f"{num}: parte real: {num.real}, parte imaginária: {num.imag}")
