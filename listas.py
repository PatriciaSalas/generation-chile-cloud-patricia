frutas = ["manzana", "banana", "cereza"]    

print(frutas[0]) #obtener el primer elemento de la lista
print(frutas[2]) #obtener el tercer elemento de la lista    
print(frutas[-1]) #obtener el último elemento de la lista
print(frutas[-2]) #obtener el penúltimo elemento de la lista
print(frutas[-3]) #Vuelve a imprimir manzana, el primer elemento de la lista


frutas.sort() #ordena la lista en orden alfabético
print(frutas)

print(sorted(frutas)) #imprime una lista ordenada sin modificar la lista original   


frutas.append("naranja") #agrega un nuevo elemento al final de la lista
frutas.sort()
print(frutas)

frutas.insert(0, "kiwi") #agrega un nuevo elemento en la posición indicada
print(frutas)

