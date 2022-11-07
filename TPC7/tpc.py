import csv
import matplotlib.pyplot as plt


def lerficheiro():
    file = open("D:\ATP2022\datasets\_alunos.csv","r",encoding="UTF8")
    file.readline()
    csv_file= csv.reader(file,delimiter=",")
    lista=[]
    for linha in csv_file:
        lista.append(tuple(linha))
    file.close()

    return (lista)


def distribCurso(lista):
    contar={}
    exemplo=lista[1]
    if len(exemplo)==7:
        for tuplo in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4 = tuplo
            if curso in contar:
                contar[curso]=contar[curso]+1
            else:
                contar[curso]=1
    
    if len(exemplo)==8:
        for tuplo in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = tuplo
            if curso in contar:
                contar[curso]=contar[curso]+1
            else:
                contar[curso]=1
    
    if len(exemplo)==9:
        for tuplo in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = tuplo
            if curso in contar:
                contar[curso]=contar[curso]+1
            else:
                contar[curso]=1
    return(contar)


def medias(lista):
    novosDados=[]

    for tuplo in lista:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4 = tuplo
        media= (int(tpc1)+int(tpc2)+int(tpc3)+int(tpc4))/4
        novoTuplo=(id, nome, curso, tpc1, tpc2, tpc3, tpc4, media)
        novosDados.append(novoTuplo)
    
    return(novosDados)

def tabelaMedia(lista):
    lista = medias(lista)
    for tuplo in lista:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = tuplo
        print(f"{nome:^30}|{media:<10}")
    return


def escaloes(lista):
    lista = medias(lista)
    listaEscalao=[]
    for tuplo in lista:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = tuplo

        if 0<= media <4.5:
            escalao="E"
        if 4.5<= media <8.5:
            escalao="D"
        if 8.5<= media <12.5:
            escalao="C"
        if 12.5<= media <16.5:
            escalao="B"
        if 16.5<= media <=20:
            escalao="A"
        tuploNew = (id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao)
        listaEscalao.append(tuploNew)
    return (listaEscalao)

def tabelaEscalao(lista):
    lista = escaloes(lista)
    for tuplo in lista:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = tuplo
        print(f"{nome:^30}|{media:^10}|{escalao:<5}")
    return

def distribEscalao(lista):
    lista = escaloes(lista)
    contar={}
    for tuplo in lista:
        id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = tuplo
        if escalao in contar:
            contar[escalao] +=1
        else:
            contar[escalao]= 1
    return(contar)


def grafico(distrib):
    import matplotlib.pyplot as plt
    valorX=list(distrib.keys())
    valorY=[]
    for p in valorX:
        valorY.append(distrib[p])

    plt.bar(valorX, valorY)
    plt.show()


def tabelaEscalao(lista):
    distrib = distribEscalao(lista)
    x = list(distrib.keys())
    y = list(distrib.values())
    for i in range(len(x)):
        print(f"|{x[i]:^5}|{y[i]:^5}|")

def tabelaCurso(lista):
    distrib = distribCurso(lista)
    x = list(distrib.keys())
    y = list(distrib.values())
    for i in range(len(x)):
        print(f"|{x[i]:^11}|{y[i]:^5}|")



def menu():
    print("""MENU
    Escolha uma opção:
    1- Distribuição alunos por curso 
    2- Médias
    3- Escalões
    4- Gráfico distribuição
    5- Tabela distribuição
    6- Ver menu
    0- Fechar programa\n""")
    return

def submenuGraph():
    print("""GRÁFICO:
    (1) Curso
    (2) Escalões
    (3) Ver submenu
    (0) Sair\n""")
    return

def submenuTabela():
    print("""TABELA:
    (1) Curso
    (2) Escalões
    (3) Ver submenu
    (0) Sair\n""")
    return