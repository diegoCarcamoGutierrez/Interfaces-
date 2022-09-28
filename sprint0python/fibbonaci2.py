import math


def funcion_fibbonaci2(n):
    a=(((1+math.sqrt(5))/2))
    b=((((1-math.sqrt(5))/2)))
    resu=((a**n)-b**n)//math.sqrt(5)
    
    print(str(resu))


