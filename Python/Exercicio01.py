# Atividade proposta:
# Elabore um algoritmo para que o usuário, através da entrada de dados, 
# informe os seus dados pessoais. Alguns desses dados fornecidos pelo usuário precisam ser 
# apresentados na tela quando o algoritmo for executado, são eles:
# - Nome;
# - Endereço;
# - Cidade;
# - CPF
# - RG.

# Solicita ao usuário que insira seus dados pessoais
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
cidade = input("Digite sua cidade: ")
cpf = input("Digite seu CPF: ")
rg = input("Digite seu RG: ")

# Exibe os dados fornecidos pelo usuário
print("\nDados Pessoais:")
print(f"Nome: {nome}")
print(f"Endereço: {endereco}")
print(f"Cidade: {cidade}")
print(f"CPF: {cpf}")
print(f"RG: {rg}")