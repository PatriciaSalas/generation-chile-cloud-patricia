#try:
    #numero = int(input("Ingresa un número: "))
    #print("Número válido:", numero)
#except:    
    #print("Error: no ingresaste un número válido.")
 
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.") #<-- mensaje personalizado con raise
    return edad

validar_edad(int(input("ingrese su edad: ")))