#Bucle para  agregar notas a una lista segun el porcentaje de la nota en la nota final
# Autor: Juan Pablo Salazar Serrano
# Fecha: 23/06/2019 12:00
#------------------------------------------------------------          
# Funcion que calcula la nota final

def calcNota():
    # Lista vacia
    notas = []
    # Bucle para agregar notas
    while True:
        # Ingreso de la nota
        nota = float(input("Ingrese la nota: "))
        # Ingreso del porcentaje
        porcentaje = float(input("Ingrese el porcentaje: "))
        # Agregar la nota a la lista
        notas.append((nota, porcentaje))
        # Pregunta para continuar
        continuar = input("Desea continuar? (s/n): ")
        # Condicion para salir del bucle
        if continuar == "n":
            break
    # Inicializar la variable que acumulara la nota final
    notaFinal = 0
    # Bucle para calcular la nota final
    for nota, porcentaje in notas:
        notaFinal += nota * porcentaje
    # Imprimir la nota final
    print("La nota final es: ", notaFinal)
# Llamado a la funcion
calcNota()

#------------------------------------------------------------
# FIN calcNota.py
#------------------------------------------------------------
#EJemplo pero quiero ver cuanto es el valor de cada nota tambien si se saca un 5 en la nota final   
#------------------------------------------------------------
