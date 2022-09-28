import time
from fibbonaci import funcion_fibbonaci
from fibbonaci2 import funcion_fibbonaci2

n=int(input("Introduce un número entero"))


print("Escoja una forma para calcular fibbonaci")
print("a-primer algoritmo")
print("b-segundo algoritmo")
opc=input()
if opc=='a':
    start_time=time.time()
    funcion_fibbonaci(n)
    end_time=time.time()
    elapsed_time=end_time-start_time
    print("El tiempo de ejecución ha sido "+str(elapsed_time)+" segundos")
elif opc=='b':
    start_time=time.time()
    funcion_fibbonaci2(n)
    end_time=time.time()
    elapsed_time=end_time-start_time