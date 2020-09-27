
def mostrar():
    print(
        "<><><><><><><><><><><><><><><><><><><><><><><><>\nlENGUAJES FORMALES Y DE PROGRAMACION  SECCION A-\n Angel Geovany Aragón Pérez   201901055\n<><><><><><><><><><><><><><><><><><><><><><><><>")
    print(
        "Eliga una opcion: \n 1.Cargar Archivo \n 2.Graficar Ruta \n 3.Graficar Mapa \n 4. Salir \n<><><><><><><><><><><><><><><><><><><><><><><><>")
    opcion = int(input())
    return opcion

def menu():
    op = mostrar()
    if op == 1:
        cargar_archivo()
        #cargar archivo
        elif op == 2:
            #graficar ruta
            pass
        elif op == 3:

            pass
        elif op == 4:
            print("Bye :  )")
        else:
            menu()
def cargar_archivo():
    ruta=input("Ingrese la ruta del archivo")
    archivo=open(ruta, 'r')
    for linea in archivo:
         metodo=linea.splitlines()
    if des=="exit":
        redireccion()
menu()    