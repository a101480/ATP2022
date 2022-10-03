# Adivinha o número
## Modalidade 1  -  adivinhar o número do PC
~~~ python
import random

n=random.randrange(1,101)
j=int(input("Escolhe um número:"))
t=0
if n==j:
    print ("Acertou")
    t=t+1
    t=str(t)
    print ("Número de tentativas: " + t)
while n!=j:
    if n>j:
        print ("O número que pensei é Maior")
    if n<j:
        print ("O número que pensei é Menor")
    t=t+1
    j=int(input("Escolhe outro número:"))
t=str(t)
j=str(j)
print ("Acertou")
print ("O número é " + j)
print("Número de tentativas: " + t) 
~~~
## Modalidade 2 - PC adivinha o número
~~~python
import random

tentativas=1
liminf=1
limsup=101
pc=random.randrange(liminf,limsup)
pc=str(pc)
print ("Será o número " + pc + "?")
pc=int(pc)
resposta=input("O número é maior ou menor?")
while resposta!="acertou":
    if resposta=="maior":
        liminf=pc+1
    else:
        liminf=liminf
    if resposta=="menor":
        limsup=pc
    else:
        limsup=limsup
    tentativas=tentativas+1
    pc=random.randrange(liminf,limsup)
    pc=str(pc)
    print ("Será o número " + pc + "?")
    pc=int(pc)
    resposta=input("O número é maior ou menor?")
pc=str(pc)
tentativas=str(tentativas)
print("ACERTEI")
if tentativas=="1":
    print("Precisei de " + tentativas + " tentativa para acertar o número " + pc)
else:
    print("Precisei de " + tentativas + " tentativas para acertar o número " + pc)
~~~
