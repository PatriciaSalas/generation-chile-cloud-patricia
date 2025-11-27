#Sistema de gestion de alumnos usando listas en Python
#CRUD create, read, update, delete de alumnos

alumnos = []  # Lista vacía para almacenar los nombres de los estudiantes
alumno1 = input("Ingrese el nombre del primer alumno: ")
alumno2 = input("Ingrese el nombre del segundo alumno: ")
alumno3 = input("Ingrese el nombre del tercer alumno: ")
alumno4 = input("Ingrese el nombre del cuarto alumno: ")
alumno5 = input("Ingrese el nombre del quinto alumno: ")

alumnos.append(alumno1)
alumnos.append(alumno2) 
alumnos.append(alumno3)
alumnos.append(alumno4)
alumnos.append(alumno5)

print(alumnos)  # Muestra la lista completa de alumnos

#Actualizamos con un nuevo alumno para la posicion 2
alumnos.insert(1, input("Ingrese el nombre del nuevo alumno para la posición 2: "))
print(alumnos)

alumnos.remove(alumnos[1])  # Elimina el alumno en la posición 2 (índice 1)
#o con "alumnos.pop(1)"    #Remueve o elimina el alumno en la posición 2 (índice 1)


print(alumnos)  # Muestra la lista actualizada de alumnos
