#  Aplicação para gerir um cinema
~~~python
cinema= [("1",100,[1,2,3,4,5,6],"avatar"),("2",120,[2,5,8,10,18,19,34],"beemovie"),("3",150,[],"dwd"),("4",90,[1,2,3,22,43,56],"smile"),("5",80,[1,2,3,4],"mulan"),("6",110,[1,2,5,8,9,14,22,87],"velocidadef")]

print("(1) Filmes em exibição")
print("(2) Lugares ocupados")
print("(3) Lugar disponível?")
print("(4) Comprar bilhete")
print("(5) Inserir sala")
print("(6) Alterar filme")
print("(0) Sair")

esc=int(input("Função: "))

while esc!=0:
    if esc==1:
        for i in cinema:
            sala,capacidade,ocupados,filmedar=i
            print(sala,"---->",filmedar)

    if esc==2:
        print("Lugares ocupados:")
        for i in cinema:
            sala,capacidade,ocupados,filmedar=i
            print("Sala",sala, "---->", filmedar,"(",ocupados,")")

    if esc==3:
        filme=str(input("Filme: "))
        lugar=int(input("Lugar: "))
        for i in cinema:
            sala, capacidade, ocupados, filmedar=i
            if filme==filmedar:
                if lugar>capacidade:
                    print("O lugar", lugar, "nao existe na", sala)
                else:
                    if lugar in ocupados:
                        disponivel=False
                        print("O lugar", lugar, "esta ocupado")
                    else:
                        disponivel=True
                        print("O lugar", lugar, "nao esta ocupado")
    
    if esc==4:
        filme=str(input("Filme: "))
        lugar=int(input("Lugar: "))
        for i in cinema:
            sala, capacidade, ocupados, filmedar=i
            if filme==filmedar:
                if lugar<=capacidade:
                    if lugar not in ocupados:
                        ocupados.append(lugar)
                        print("Bilhete para o lugar",lugar,"do filme",filme,'comprado')
                        usados=ocupados
                    
                    else: 
                        print("O lugar", lugar, "ja se encontra ocupado")
                        usados=ocupados
                else:
                    print("O lugar", lugar, "nao existe na sala")
        print("--------------------")
        print("Os lugares", usados,"estao ocupados")


    if esc==5:
        print("Nova sala")
        numero=str(input("Número da sala:"))
        pessoas=int(input("Capacidade da sala:"))
        movie=str(input("Filme da sala:"))
        sala=(numero,pessoas,[],movie)
        P=0
        for i in cinema:
            if i[0]==sala[0]:
                P=P+1
        if P>0:
            print("Esta sala ja existe")
        if P==0:
            cinema.append(sala)
            for i in cinema:
                sala,capacidade,ocupados,filmedar=i
                print(sala,"---->",filmedar)


    if esc==6:
        salan=str(input("Sala para trocar filme:"))
        filmenovo=str(input("Novo filme:"))
        for i in cinema:
            sala,capacidade,ocupados,filmedar=i
            if salan==sala:
                if filmenovo==filmedar:
                    print("O filme,",filmenovo,"ja esta a ser exibido na",sala )
                else:
                    filmedar=filmenovo
                    print("Filme da",sala,"alterado para",filmenovo)
                    cinema.remove(i)
                    ocupados=[]
                    j=sala,capacidade,ocupados,filmenovo
                    cinema.append(j)
                    cinema.sort()
                    
                    
                
        print("Atualmente em exibicao:")
        for i in cinema:
            sala,capacidade,ocupados,filmedar=i
            print(sala,"---->",filmedar)
            
    esc=int(input("Função: "))
   ~~~
