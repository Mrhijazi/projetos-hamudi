#Programa que determina el promedio de dos números y
#si este es o no mayor que 10
#Elaborado por: M.hijazi  Fecha: 14-07-2021

#INICIO del programa
#DECLARACÓN de variables
#Var. de ENTRADA (aquellas cuyo valor se lee ¿Qué nos dan?)
num1 = int
num2 = int
#Var. de SALIDA (aquellas cuyo valor se escribe ¿Qué nos piden?)
prom = float
#Var. de PROCESO (aquellas cuyo valor ni se lee ni se escribe ¿Cómo lograrlo?)

#LECTURA de datos
num1 = int(input("indique un numero: "))
num2 = int(input("indique otro numero: "))
#INICIALIZACION de variables

#PROCESAMIENTO de datos
suma = num1 + num2
prom = suma / 2
#Escritura de resultados
print("el promedio es: " + str (prom))
if prom > 10:
    print("el promedio es mayor que 10")
else:
    print("el promedio no es mayor que 10")
#FIN del programa