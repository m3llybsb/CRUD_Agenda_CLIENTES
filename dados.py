# Importando CSV
import csv


def adicionar_dados(i):
    with open('dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

#função VER DADOS
def ver_dados():
    dados = []
    #acessando csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return dados

# Função REMOVER
def remover_dados(i):
    def adicionar_novalista(t):
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(t)
            ver_dados()

    nova_lista = []
    telefone = i
    with open('dados.csv', 'r') as file:
        ler_csv =  csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)

    #Adicionando nova lista
    adicionar_novalista(nova_lista)
    
# Função ATUALIZAR
def atualizar_dados(i):
    def adicionar_novalista(t):
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(t)
            ver_dados()

    nova_lista = []
    telefone = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv =  csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    tel= i[3]
                    email = i[4]
                    
                    dados = [nome,sexo,tel,email]

                    #Trocando lISTA por INDEX
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados

    #Adicionando nova lista
    adicionar_novalista(nova_lista)


#função PESQUISAR
def pesquisar_dados(i):
    dados = []
    telefone = i

    #acessando csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    return dados
