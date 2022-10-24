# Análise de dados: doença cardíaca
~~~python
global pop
global classe
global valoresClasse
pop=[]
classe=[]
valoresClasse=[]



file=open("myheart.csv","r") 
listapopulacao=[]
file.readline() 
for linha in file:
    pessoa=linha.split(",")
    listapopulacao.append(pessoa)
for pessoa in listapopulacao:
    pessoa[-1]=pessoa[-1].replace("\n","")
    utente=(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5])
    pop.append(utente)
file.close()



def sexoUtente(lista):
    global classe
    global valoresClasse

    classe=["homem","mulher"]
    masculino=0
    feminino=0
    for utente in lista:
        if str(utente[1])=="M":
            masculino=masculino+1
        if str(utente[1])=="F":
            feminino=feminino+1
        valoresClasse=[masculino,feminino]
    
    


def sexoUtenteDoenca(lista):
    global classe
    global valoresClasse

    classe=["homem","mulher"]
    masculino=0
    feminino=0
    for utente in lista:
        if str(utente[5])=="1":
            if str(utente[1])=="M":
                masculino=masculino+1
            if str(utente[1])=="F":
                feminino=feminino+1
            valoresClasse=[masculino,feminino]
   



def minmaxi(lista,i):
    lista2=[]
    for utente in lista:
        lista2.append(int(utente[i]))
    lista2.sort()
    #print(lista2)
    min=lista2[0]
    max=lista2[-1]
   



def escalaoEtario(lista):
    global classe
    global valoresClasse

    classe=[]
    valoresClasse=[]
    menor=25
    utentesCom=0
    while menor<=73:
        for utente in lista:
            idade,sexo,tensão,colesterol,batimento,temDoenca=utente
            temDoenca=int(temDoenca)
            if temDoenca!=0:
                if int(idade)>=menor and int(idade)<=menor+4:
                    utentesCom=utentesCom+1
        classe.append("["+ str(menor) + ";" + str(menor+4) + "]")
        valoresClasse.append(str(utentesCom))
        menor=menor+5
        utentesCom=0




def escalaoColesterol(lista):
    global classe
    global valoresClasse

    lista2=[]
    for utente in lista:
        lista2.append(int(utente[3]))
    lista2.sort()
    maior=lista2[-1]
    classe=[]
    valoresClasse=[]
    menor=0
    utentesCom=0
    while menor<=maior:
        for utente in lista:
            idade,sexo,tensão,colesterol,batimento,temDoenca=utente
            temDoenca=int(temDoenca)
            if temDoenca!=0:
                if int(colesterol)>=menor and int(colesterol)<=menor+9:
                    utentesCom=utentesCom+1
        classe.append("["+ str(menor) + ";" + str(menor+9) + "]")
        valoresClasse.append(str(utentesCom))
        menor=menor+10
        utentesCom=0
 
    


def tabelas(classe,valoresClasse):
    i=0
    while i < len(classe):
        print(classe[i],"|",valoresClasse[i])
        i=i+1
    


print("====================")
print("MENU")
print("====================")
print("(1) Distribuição da doença por sexo")
print("(2) Distribuição da doença por escalões etários")
print("(3) Distribuição da doença por níveis de colesterol")
print("(0) Fechar programa")
print("====================")
esc=int(input("Escolha uma função: "))
while esc!=0:
    if esc == 1:
        sexoUtenteDoenca(pop)
        print("Sexo|Distribuição")
        print("--------------------")
        tabelas(classe,valoresClasse)

    if esc == 2:
        escalaoEtario(pop)
        print("Idade|Distribuição")
        print("--------------------")
        tabelas(classe,valoresClasse)


    if esc == 3:
        escalaoColesterol(pop)
        print("Nivel colesterol|Distribuição")
        print("--------------------")
        tabelas(classe,valoresClasse)

    
    if esc != (1,2,3):
        print("A função escolhida não existe, escolha uma das presentes no menu")

    print("====================")
    esc=int(input("Escolha uma função: "))
print("Programa terminado")
~~~
