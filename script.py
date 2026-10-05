print("Hola aprendiendo python")
apellido:str = "Lazaro"
nombre:str = "Adrian"
print(f"Soy {nombre} {apellido}")
edad:int = 27
ciudad:str = "Valencia"
tengo_carnet:bool = True
print(f"Soy {nombre} {apellido}, tengo {edad} años, vivo en {ciudad} y tengo carnet de conducir: {tengo_carnet}")
print(nombre.upper()+" "+apellido.lower())
print(len(nombre))
print(nombre[0])
print(apellido[-1]) #-1 siempre muestra la ultima letra de la cadena
persona = {"nombre":nombre, "apellido":apellido, "edad":edad, "ciudad":ciudad, "soltero":False}
print(persona["nombre"])
compra = ["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(2, "verduras")
compra.pop(-1)
print(compra)
culpable:bool = True
if culpable == True:
    print("Eres culpable")
else:
    print("Eres inocente")
    