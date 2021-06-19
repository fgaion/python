"""
Recebendo dados do usuário
"""
print("Qual o seu nome?: ")
nome = input()

# print("Seja bem vindo(a) %s" %(nome))   #versão 2.x
# print("Seja bem vindo(a) {0}".format(nome)) #versão 3.x
print(f"Seja bem vindo(a) {nome}")

idade = int(input("Qual a sua idade: "))
# print("A pessoa %s tem %s anos" % (nome, idade))   #versão 2.x
# print("A pessoa {0} tem {1} anos".format(nome, idade)) #versão 3.x
print(f"A pessoa de nome {nome} tem {idade} anos")

print(f'A pessoa de nome {nome} nasceu em em {2021 - idade}')