# Elaborado por: Mohamed Ali Hijazi Fecha: 23-06-2021
# INICIO del programa
# DELARACIÓN de variables
# Var. de ENTRADA (aquellas cuyo valor se lee ¿Qué nos dan?)
#Monto
num1 = int
num2 = int

# Var. de SALIDA (aquellas cuyo valor se escribe ¿Qué nos piden?)
Iva=0.16
#lectura de datos
num1 = int(input("Indique un número: "))
num2 = int(input("Indique otro número: "))
# PROCESAMIENTO de datos
suma = num1 + num2
print(suma)
#ejecucion
Monto=int(input("introduzca el precio del producto: "))
Iva=Monto*0.16
MontoSin=Monto - Iva
#Escritura resultado
print("El precio del producto sin IVA es de: " + str(MontoSin))
print("El impuesto del valor agregado al producto es de: " + str(Iva))
#FIN del programa
