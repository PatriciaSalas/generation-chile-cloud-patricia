frutas = []

total_venta = 0.0
#print(f"Tu total de ventas es : {total_venta}")


while True:
    nombre = input("Ingresa el nombre de la fruta a buscar: ")
    if nombre == "salir": 
        print("Saliendo del programa...")
        break  

    precio = float(input(f"Ingresa el precio de {nombre}: "))

    fruta = {
        "nombre": nombre,
        "precio": precio
    }

    frutas.append(fruta)
    print(f"Ingresando la fruta: {nombre} con el precio de {precio}")

    total_venta = 0.0

for fruta in frutas: #calcular el total de venta (precio * cantidad)
    print(fruta["nombre"])
    #Aqui va calculo del total de venta
    total_venta += fruta["precio"]
    

print(f"Ingresando la fruta", frutas)
        
#for para imprimir un ticket de compra a la terminal 

print("\n--- Ticket de Compra ---")

for fruta in frutas:
    print(f"{fruta['nombre']}: ${fruta['precio']}")
print("------------------------")   

print(f"Total de venta: ${total_venta}")
