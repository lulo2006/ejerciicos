contactos = []

def opción_1():
    print("Agregar contacto")
    nombre = input("Ingrese nombre: ")
    telefono = int(input("Ingrese teléfono: "))
    correo = validar_correo
    contacto = {"Nombre":nombre, "telefono":telefono, "Correo":correo}
    contactos.append(contacto)
    print("Contacto agregado!")

def opción_2():
    if not contactos:
        print("No existen contacto, registre uno en la opción 1!")
    else:
        print("\tLista de contactos")
        for c in contactos:
            print(f"Nombre: {c['Nombre']}")
            print(f"Teléfono: {c['Teléfono']}")
            print(f"Correo: {c['Correo']}\n")

def opción_3():
    if not contactos:
        print("No existen contacto, registre uno en la opción 1!")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")
        import csv
        with open(nombre_archivo+".csv","x",newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["Nombre", "telefono", "correo"])
            escritor.writerows(contactos)
            
def opción_4():
    print("Gracias a Dios!, Amén")
    exit

#########################################validaciones:
def validar_nombres():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print("ERROR! el nombre debe tener al menos 3 caracteres y sólo letras!")

def velidar_telefono():
    while True:
        try:
            tel = int(input("Ingrese número telefónico: "))
            if len(str(tel))==9 and str(tel)[0]=='9':
                return tel
            else:
                print("ERROR! el teléfono debe comenzar con 9 y tener 9 digitos!")
        except:
            print("ERROR! ingrese números enteros")

def validar_correo():
    while True:
        #patterns
        cor = input("Ingrese correo: ")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip())>=13:
            return cor
        else:
            print