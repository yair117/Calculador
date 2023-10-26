#esto es una calculador con condicion multiple
from math import *
bandera=False
#variables 
X=float(input("Ingresa el valor de X\n"))
Y=float(input("Ingresa el valor de Y\n"))
#Seleccion de operacion 
print("Selecciona la operacion que quiera realizar")
#Opciones de la calculadora 
print("1)Sumar(El primero mas el segundo)")
print("2)Restar(El primero menos el segundo)")
print("3)Multiplicar(El primero por el segundo)")
print("4)Dividir(El primero sobre el segundo)")
print("5)Potencia(El primero a la potencia del segundo)")
print("6)Logaritmo(El algoritmo del primero)\n")
opcion=int(input("Ingresa la operacion que quieras realizar\n"))
#Condiciones anidadas
if opcion==1:
    Z=X+Y
    print(X,"+",Y)
elif opcion==2:
    Z=X-Y
    print(X,"-",Y)
elif opcion==3:
    Z=X*Y
    print(X,"*",Y)
elif opcion==4 and Y==0:
    print("El denominador es igual a 0\nNo se puede realizar la division")
    bandera=True
elif opcion==5:
    Z=pow(X,Y)
    print(X,"^",Y,)
elif opcion==6:
    Z=log(X)
    print("Logaritmo de X es:\n",X)
elif opcion==6 and X<=0:
    print("El valo de X es <= a cero y \n No se puedecalcular el algoritmo")
else:
    print("Opcion desconocida.")

#Se muestra resultado con otra condicion 
if (opcion<7 and bandera==False):
    print("resultado  =", Z)