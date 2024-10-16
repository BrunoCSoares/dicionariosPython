'''
Escreva um programa em Python que crie uma lista de 5 veículos, utilizando o conceito lista de dicionários, contendo os seguintes dados:

o Marca
o Modelo
o Ano de fabricação
o Cor
o Valor
o IPVA (isento se o tempo de fabricação for superior a 20 anos; caso contrário 4%)

Após a inserção na lista, faça os seguintes relatórios:

a. Listar todos os veículos e, ao final, média dos valores.
b. Listar os veículos da marca Jeep, da cor prata e cujo ano de fabricação esteja entre 5 e 10 anos.
'''

lista_veiculos = []
ano_atual = int(input("Insira o ano atual: "))
soma_valores = 0

for i in range(5):
    print("\n")
    marca = input("Insira a marca do carro: ")
    modelo = input(f"Insira o modelo do {marca}: ")
    ano_fab = int(input(f"Insira o ano de favricação do {modelo}: "))
    cor = input(f"Insira a cor do {modelo}: ")
    valor = float(input(f"Insira o valor do {modelo}: "))
    veiculo = {'marca':marca,'modelo':modelo,'ano_fab':ano_fab,'cor':cor,'valor':valor}
    if ano_atual - ano_fab <= 20:
        veiculo['ipva'] = "40%"
    lista_veiculos.append(veiculo)

for veiculo in lista_veiculos:
    print(veiculo)
    soma_valores += veiculo['valor']
print(f"A média de valor dos veículos é {soma_valores / 5:.2f}")

for veiculo in lista_veiculos:
    if veiculo['marca'].lower() == "jeep" and veiculo['cor'].lower() == "prata" and ano_atual - veiculo['ano_fab'] >= 5 and ano_atual - veiculo['ano_fab'] <= 10:
        print(veiculo)