#Programa Elaborado por M.hijazi
#Inicio
#Declaracion de variable
Dia = int(input("Introduzca el Dia: "))
Mes = int(input("Intrduzca el Mes: "))
Año = int(input("Introduzca el Año: "))
print("")
#Ejecucion
if Mes == 1 and Dia <=31:
    print("la fecha es real")
elif Mes == 2 and Dia == 29 and Año % 4 == 0:
    print("la fecha es real y ademas es bisiesto")
elif Mes == 2 and Dia <= 28:
    print("la fecha es real")
elif Mes == 3 and Dia <= 31:
    print("la fecha es real")
elif Mes == 4 and Dia <= 30:
    print("la fecha es real")
elif Mes == 5 and Dia <= 31:
    print("la fecha es real")
elif Mes == 6 and Dia <= 30:
    print("la fecha es real")
elif Mes == 7 and Dia <= 31:
    print("la fecha es real")
elif Mes == 8 and Dia <= 30:
    print("la fecha es real")
elif Mes == 9 and Dia <= 31:
    print("la fecha es real")
elif Mes == 10 and Dia <= 30:
    print("la fecha es real")
elif Mes == 11 and Dia <= 31:
    print("la fecha es real")
elif Mes == 12 and Dia <= 30:
    print("la fecha es real")
else:
    print("la fecha no es real")
#FIN DEL PROGRAMA