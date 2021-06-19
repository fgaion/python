"""
if
elif
else

operadores
binários: and, or
unários: not, is
"""

idade = 18
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

ativo = False
logado = True

if ativo and logado:
    print("Bem vindo usuário")
else:
    print("Você precisa ativar sua conta")

if ativo or logado:
    print("Bem vindo usuário")
else:
    print("Você pŕecisa ativar sua conta")

if not ativo:
    print("Ativar conta!")
else:
    print("Conta ativada!")

if ativo is False:
    print("Ativar Conta!")

print(type(idade))
if isinstance(idade,int):
    print("Integer")
