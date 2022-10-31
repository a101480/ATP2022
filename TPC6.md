# Processando um dataset em CSV
~~~python
import csv
global obras 
global distrib
obras=[]
distrib={}
global lista 
lista=[]

def lerObras():
    file = open("obras.csv","r",encoding="UTF8")
    file.readline()
    csv_file= csv.reader(file,delimiter=";")

    for linha in csv_file:
        lista.append(tuple(linha))
    return lista


def contaObras(obras):
    print(len(obras))


def tabelaObras(obras):
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        print(f"{nome[:25]:25} | {desc[:30]:30} | {ano[:15]:15} | {ano[:6]:6}")


def ordenaValores1elem(v):
    return v[0] 
def listaAlfabetica(obras):
    listaAlfabetica=[]
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        tuplo=(nome,ano)
        listaAlfabetica.append(tuplo)
    listaAlfabetica.sort(key= ordenaValores1elem)
    print(listaAlfabetica)


def ordenaValores2elem(v):
    return v[1]

def listaCrescente(obras):
    listaCrescente=[]
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        tuplo=(nome,ano)
        listaCrescente.append(tuplo)
    listaCrescente.sort(key= ordenaValores2elem)
    print(listaCrescente)


def ordenaCompositores(obras):
    compositores=[]
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        compositores.append(compositor)
    compositores.sort()
    print(compositores)


def grafico(distrib):
    import matplotlib.pyplot as plt
    valoresX=list(distrib.keys())
    #print(valoresX)
    alturaBarras=[]
    for p in valoresX:
        alturaBarras.append(distrib[p])  
    #print(alturaBarras)
    
    plt.bar(valoresX, alturaBarras)
    plt.xticks(rotation='vertical')
    plt.show()


def distribPeriodo(obras):
    distrib={}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if periodo in distrib:
            distrib[periodo]=distrib[periodo]+1
        else:
            distrib[periodo]=1
    print(distrib)
    return distrib


def distribAno(obras):
    distrib={}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if ano in distrib:
            distrib[ano]=distrib[ano]+1
        else:
            distrib[ano]=1
    print(distrib)
    return distrib


def distribCompositor(obras):
    distrib={}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if compositor in distrib:
            distrib[compositor]=distrib[compositor]+1
        else:
            distrib[compositor]=1
    print(distrib)
    return distrib
        

def autorTitulo(obras):
    listaTuplos=[]
    lista=[]
    lista2=[]
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if compositor not in lista:
            lista.append(compositor)
        lista.sort()
    for pessoa in lista:
        for obra in obras:
            nome, desc, ano, periodo, compositor, duracao, id = obra
            if str(compositor)==str(pessoa):
                lista2.append(nome)
                lista2.sort()
        tuplo=(pessoa,lista2)
        lista2=[]
        listaTuplos.append(tuplo)

    #################################

    print("==========================================") 
    for tuplo in listaTuplos:
        compositor, nome= tuplo
        print(f"  {compositor:<35}")
        for livro in nome:
            print(f"      --> {livro[:30]:30}")
        print("==========================================")

##############################################################
    

print("""MENU
escolha uma opção:
1- quantas obras existem 
2- tabela(obra,descrição,compositor,ano de criação)
3- tuplos ordenados ordem alfabetica
4- tuplos ordenados ordem crescente
5- lista ordenada compositores
6- distrib obras por periodo
7- sistrib obras ano
8- distrib obras compositor
9- compositores e suas obras
0- fechar programa""")
print("====================")


file = open("obras.csv","r",encoding="UTF8")
file.readline()
csv_file= csv.reader(file,delimiter=";")

for linha in csv_file:
    obras.append(tuple(linha))
file.close()

esc=int(input("Escolha uma função: "))
while esc!=0:
    if esc==1:
        contaObras(obras)

    if esc==2:
        tabelaObras(obras)

    if esc==3:
        listaAlfabetica(obras)

    if esc==4:
        listaCrescente(obras)
    
    if esc==5:
        ordenaCompositores(obras)

    if esc==6:
        grafico(distribPeriodo(obras))

    if esc==7:
        grafico(distribAno(obras))

    if esc==8:
        grafico(distribCompositor(obras))

    if esc==9:
        autorTitulo(obras)

    print("====================")
    esc=int(input("Escolha uma função: "))

print("Programa terminado")
~~~
