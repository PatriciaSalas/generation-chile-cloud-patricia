edad = input("Ingrese su edad: ")

if int(edad) > 18:
    print("Eres mayor de edad.")

elif int(edad) == 18:
    print("Eres mayor de edad, tienes justo 18 años.")

else:
    print("Eres menor de edad.")


def definir_etapa_vida(edad):
    if int(edad) < 12:
        return "Eres un Niño"
    elif (edad) < 18:
        return "Eres un Adolescente"
    elif(edad) < 65:
        return "Eres un Adulto"
    else:
        return "Eres una Persona Mayor"

