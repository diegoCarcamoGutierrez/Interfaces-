import time
def funcion_fibbonaci(n):
    resu=0
    o=2
    i=0
    j=1

    while o<=n:
        resu=i+j
        i=j
        j=resu
        o=o+1
    print (str(resu))