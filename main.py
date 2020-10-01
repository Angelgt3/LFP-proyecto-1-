import io




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
        print("2")
        #graficar ruta
    elif op == 3:
        print("3")
    elif op == 4:
        print("Bye :  )")
    else:
         menu()


Lexema=list()
Fila=list()
columna=list()
Token=list()
Error=list()
texto_tem=list()
avanzar=['<','>','<','>','<','/','>','<','/','>']

def q0257(cadena,estado):
    if cadena==avanzar[estado]:
        estado+=1
        return estado
    else:
        Error.append(cadena)
        return estado
def q13469(cadena,estado):
    if cadena.isalpha() or cadena.isdigit() or cadena=='.' or cadena=='_' or cadena =='>' or cadena== '<' or cadena=='/':
        if cadena==avanzar[estado]:
            if not estado==6 or not estado==9:
                texto=""
                for c in texto_tem:
                    texto+=c
                if estado==1 or estado==3:
                    Token.append(texto)
                elif estado==4:
                    Lexema.append(texto)
                for x in range(len(texto_tem)):
                    texto_tem.pop()
            estado+=1
        elif not estado==6 or not estado==9:
            texto_tem.append(cadena)
        return estado
    else:
        Error.append(cadena)
        return estado

def q8(cadena,estado):
    if cadena==avanzar[estado]:
        estado+=1
        return estado
    elif cadena.isalpha() or cadena.isdigit() or cadena=='.' or cadena=='_' or cadena =='>' or cadena== '<' or cadena=='/':
        estado=3
        return q13469(cadena,estado)

def operacion(caracter,estado):
    if estado==0 or estado==2  or estado==5 or estado==7: 
        estado=q0257(caracter,estado)
    elif estado==1 or estado==3 or estado==4 or estado==6 or estado==9: 
        estado=q13469(caracter,estado)
    elif estado==8:
        estado=q8(caracter,estado)
    elif estado==10:
        estado=0
    return estado


def cargar_archivo():
    #try:
        ruta=str(input("Ingrese la ruta del archivo"))
        archivo=open(ruta, 'r')
        n=0
        estado=0
        for linea in archivo:
            for caracter in linea:
                caracte=caracter.lower()
                caracterf=caracte.strip()
                if caracterf=="":
                    continue   
                n+=1
                #print(f"{caracterf} + {n}")
                estado=operacion(caracterf,estado)
                print(estado)
        print(f'Tokens: {Token}')
        print(f'Lexema: {Lexema}')
        print(f'Error: {Error}')

        archivo.close()

   # except:
    #    print("No se pudo abrir el documento")
     #   menu()


menu()    