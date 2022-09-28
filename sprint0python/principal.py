import time
from re import A
from fibbonaci import funcion_fibbonaci
from fibbonaci2 import funcion_fibbonaci2

n=int(input("Introduce un número entero"))


print("Escoja una forma para calcular fibbonaci")
print("a-primer algoritmo")
print("b-segundo algoritmo")
opc=input()
if opc=='a':
    start_time=start_time()
    funcion_fibbonaci(n)
    end_time=
elif opc=='b':
    funcion_fibbonaci2(n)