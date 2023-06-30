personas = []

def grabar():
    nif = input("Ingrese el NIF: ")
    nombre = input("Ingrese el nombre de la persona: ")
    if len(nombre) >= 8:
        print('ingrese el nombre otra vez. (recuerda mas de 8 letras)')
        return
    edad = int(input("ingrese la edad de la persona: "))
    if len(edad) >= 0:
        print('edad invalida')
        return
    persona = {
        "El NIF es: " : nif,
        "El nombre es: " : nombre,
        "La edad es: " : edad
    }

    personas.append(persona)
    print("Datos guardados correctamente ")

def buscar():
    nif = input("ingrese el NIF a buscar: ")
    for persona in personas:
        if persona ["NIF"] == nif:
            print("Informacion de la persona: ")
            print(f"NIF: {persona['NIF ']}" )
            print(f"Nombre: {persona['Nombre ']}" )
            print(f"Edad: {persona['Edad ']}" )
            if persona['NIF'][:2] == 'ES':
                print('Pertenece a la union europea ')
            else:
                print('No pertenece a la union europea ')
            return
    print('No se encontro a una persona con ese NIF ')  

def imprimir_certificados():
    for persona in personas:
      print('Certificado de Nacimiento: ')  
      print(f"Nombre: {persona['nombre']}")
      print(f"NIF: {persona['NIF']}")
      print('******')
      print("Certificado de estado conyugal: ")
      print(f"Nombre: {persona['Nombre']}")
      print(f"NIF: {persona['NIF']}")
      print('******')
      print('Certificado de pertenencia a la Unión Europea: ')
      print(f"Nombre: {persona['Nombre']}")
      print(f"NIF: {persona['NIF']}")



while True:
    print("Menú: ")
    print("1. Guardar")
    print("2. Buscar")
    print("3. Imprimir certificado")
    print("4. Salir")

    opcion = input('seleccione una opcion: ')

    if opcion == '1':
        grabar()
    elif opcion == '2':
        buscar()
    elif opcion == '3':
        imprimir_certificados()
    elif opcion == '4':
        print("Saliendo del programa, Muchas Gracias")
        break
    else:
        print("Opcion invalida. porfavor ingrese una de las opciones")