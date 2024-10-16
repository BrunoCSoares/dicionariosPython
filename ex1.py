'''
Escreva um programa em Python que crie uma lista de 10 funcionários, utilizando o conceito de dicionários, contendo os seguintes dados:

o Nome;
o Cargo;
o Departamento;
o Salário.

Depois da lista criada, faça a busca pelo nome de um funcionário qualquer e mostre seus dados.
'''

lista_funcionarios = []

for i in range(2):
    nome = input("Insira o nome do funcionário: ")
    cargo = input("Insira o cargo do funcionário: ")
    departamento = input("Insira o departamento do funcionário: ")
    salario = float(input("Insira o salário do funcionário: "))
    funcionario = {'Nome':nome,'Cargo':cargo,'Departamento':departamento,'Salario':salario}
    lista_funcionarios.append(funcionario)
    print("\n")

busca_nome = input("Insira o nome do funcionário que deseja encontrar: ")

for funcionario in lista_funcionarios:
    if busca_nome.lower() == funcionario['Nome'].lower():
        for chave, valor in funcionario.items():
            print(f"{chave}: {valor}")
