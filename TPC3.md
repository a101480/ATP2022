# Aplicação para manipulação de listas de inteiros
~~~python
import random

lista=[]
print("(1) Criar Lista")
print("(2) Ler Lista")
print("(3) Soma")
print("(4) Média")
print("(5) Maior")
print("(6) Menor")
print("(7) estaOrdenada por ordem crescente")
print("(8) estaOrdenada por ordem decrescente")
print("(9) Procura um elemento")
print("(0) Sair")

esc=int(input("Função: "))

while esc!=0:
    if esc==1:
        n=0
        num=int(input("Quantos números terá a lista?"))
        while n<num:
            a=random.randrange(1,101)
            lista.append(a)
            n=n+1
        print(lista)


    if esc==2:
        n=0
        num=int(input("Quantos números terá a lista?"))
        while n<num:
            a=int(input("Número: "))
            lista.append(a)
            n=n+1
        print(lista)


    if esc==3:
        soma=0
        for i in lista:
            soma=soma+i
        print("Soma igual a", soma)
    

    if esc==4:
        soma=0
        for i in lista:
            soma=soma+i
            media=soma/len(lista)
        print("Média igual a", media)


    if esc==5:
        maior=lista[0]
        for i in lista[1:]:
            if i>maior:
                maior=i
            else:
                maior=maior
        print("O maior elemento da lista é:", maior)


    if esc==6:
        menor=lista[0]
        for i in lista[1:]:
            if i<menor:
                menor=i
            else:
                menor=menor
        print("O menor elemento da lista é:", menor)


    if esc==7:
        crescente=[]
        primeiro=lista[0]
        for i in lista[1:]:
            if i>=primeiro:
                primeiro=i
                crescente.append(i)
        if len(crescente)==len(lista):
            print("SIM")
        else:
            print("NÃO")


    if esc==8:
        decrescente=[]
        primeiro=lista[0]
        for i in lista[1:]:
            if i<=primeiro:
                primeiro=i
                decrescente.append(i)
        if len(decrescente)==len(lista):
            print("SIM")
        else:
            print("NÃO")


    if esc==9:
        var=False
        contagem=0
        procurar=int(input("Que número procurar?"))
        if procurar in lista:
            while var!=True:
                for i in lista:
                    contagem=contagem+1
                    if i == procurar:
                        var=True
                        break
                print("O elemento", procurar, "está na posição número", contagem)
        else:
            print("O número não se encontra na lista")

    esc=int(input("Função: "))

if esc==0:
    print(lista)
~~~    
