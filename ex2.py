'''
Escreva um programa em Python que crie uma lista de 5 professores, utilizando o conceito lista de dicionários, contendo os seguintes dados:

o Nome
o CPF
o Idade
o Titulação máxima
o Salário

Após a inserção na lista, faça os seguintes relatórios:

a. Listar todos os professores e, ao final, média dos salários.
b. Listar os professores doutores com idade entre 26 e 47 anos.
'''

lista_professores = []
soma_salarios = 0

for i in range(5):
    nome = input("Insira o nome do professor: ")
    cpf = input(f"Insira o CPF de {nome}: ")
    idade = int(input(f"Insira a Idade de {nome}: "))
    titulacao_maxima = input(f"Insira a titulação máxima de {nome}: ")
    salario = float(input(f"Insira o salário de {nome}: "))
    professor = {'Nome':nome,'CPF':cpf,'Idade':idade,'Titulacao_maxima':titulacao_maxima,'Salario':salario}
    lista_professores.append(professor)
    print("\n")

for professor in lista_professores:
    print(professor)
    soma_salarios += professor['Salario']
print(f"\nA média salarial é {soma_salarios / 5:.2f}")

for professor in lista_professores:
    if professor['Titulacao_maxima'].lower() == "doutor" and professor['Idade'] >= 26 and professor['Idade'] <= 47:
        print(professor)