#def mensaje_bienvenida():
    #print("Bienvenido a nuestro programa!") # <-- no aparece porque hay que llamar a la funcion
 # mensaje_bienvenida()<-- Llamada a la funcion



#def saludo(nombre):
    #print(f"Hola, {nombre}! que bueno tenerte de regreso")

#mensaje_bienvenida()
#saludo("Constanza")
#saludo(input("Dime tu nombre: ")) <-- Llamada a la funcion con input 

#def saludo_contabiliza_días_con_edad(nombre, edad):
    #dias_anio = 356
    #dias_totales = dias_anio * edad
    #print(f"Hola, {nombre} que bueno tenerte de regreso, han pasado {dias_totales} desde que naciste")


#nombre = input("Dime tu nombre: ") 
#edad = int(input("Dime tu edad: ") 

#saludo_contabiliza_días_con_edad("Constanza", 27)

def saludo(nombre, edad):
    print(f"Hola, {nombre} que bueno tenerte de regreso, han pasado {calculo_anios_por_edad(edad)} desde que naciste")


def calculo_anios_por_edad(edad):
    dias_anio = 356
    dias_totales = dias_anio * edad
    return dias_totales


saludo("Constanza", 27)
