import os, time
from fun_1 import *

while True:
    os.system('cls')
    print("Menú de contactos")
    print("1. Agregar contacto\n2. Ver contacto\n3. Explorar archivo CSV\n4. Salir")
    opc = int(input("Ingrese opción:"))

    os.system('cls')
    if opc==1:
        opción_1()
    elif opc==2:
        opción_2()
    elif opc==3:
        opción_3()
    else:
        opción_4()
    time.sleep(3)