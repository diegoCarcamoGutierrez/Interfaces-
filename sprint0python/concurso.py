import random
p=0
a=False

k=0
while k<2:
    j=random.randint(0,2)
    if j==0:
        print ("¿Cuánto es 1+1?")
        print ("-Opción a: 1")
        print ("-Opción b: 2")
        print ("-Opción c: 3")
        print ("Escoja una opción: ")
        a=input()
        if a != "b":
            print("Falso")
            a=False
            p=p-5
        else:
            print("Verdadero")
            a=True
            p=p+10

    elif j==1:
        print ("¿Cuántas caras tiene un dado?")
        print ("-Opción a: 4")
        print ("-Opción b: 6")
        print ("-Opción c: cualquier número superior a 4")
        print ("Escoja una opción: ")
        a=input()
        if a != "c":
            print("Falso")
            a=False
            p=p-5
        else:
            print("Verdadero")
            a=True
            p=p+10
    
    elif j==2:
        print ("¿Cuánto es un pingüino menos un pingüino?")
        print ("-Opción a: Un ningüino")
        print ("-Opción b: 0")
        print ("-Opción c: ¿Es en serio?")
        print ("Escoja una opción: ")

        a=input()

        if a != "a":
            print("Falso")
            a=False
            p=p-5
        else:
            print("Verdadero")
            a=True
            p=p+10
    print("")
    k=k+1


if p<0:
    p=0

print("Tu puntuación es: "+str(p))