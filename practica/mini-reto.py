#crear una funcion: validar_email(email)
#debe contener "@" sino raise ValueError manejar la excepcion

try:
    def validar_email(email):
        if "@" not in email:
            raise ValueError("El email debe contener '@'.")  # mensaje personalizado con raise
        return email

    email_input = input("Ingresa tu email: ")
    validar_email(email_input)
    print("Email válido:", email_input)
except ValueError as e:
    print("Error:", e)