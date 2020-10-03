import io
import webbrowser
import os

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
        graficoRutas()
        #graficar ruta
    elif op == 3:
        graficoMapa()
        #graficar ruta
    elif op == 4:
        print("Bye :  )")
    else:
         menu()


Lexema=list()
Fila_T=list()
columna_T=list()
Token=list()
Error=list()
Fila_E=list()
columna_E=list()
texto_tem=list()
Descripcion=list()

avanzar=['<','>','<','>','<','/','>','<','/','>']

def comprobar(estado,x,y):
    if estado==5:
        u_token = Token[len(Token)-1]
        u_lexema = Lexema[len(Lexema)-1]
        if u_token=="nombre":
            x2=0
            for l in u_lexema:
                if not (l=="@" or l=="#" or l=="_" or l.isalpha() or l.isdigit()):
                    Error.append(l)
                    Descripcion.append(f"No se acepta el siguiente caracter '{l}'")
                    columna_E.append((x-(len(u_lexema)+1)+x2))
                    Fila_E.append(y)
                x2+=1
        elif u_token=="peso":
            x2=0
            for l in u_lexema:
                if not( l=="."or l.isdigit()):
                    Error.append(l)
                    Descripcion.append(f"No se acepta el siguiente caracter '{l}'")
                    columna_E.append((x-(len(u_lexema)+1)+x2))
                    Fila_E.append(y)
                x2+=1
        elif u_token=="estado":
            if not (u_lexema=="disponible" or u_lexema=="cerrada"): 
                Error.append(u_lexema)
                Descripcion.append(f"No se acepta esta respuesta '{u_lexema}'")
                columna_E.append(x-len(u_lexema))
                Fila_E.append(y)
        elif u_token=="color":
            x2=0
            for l in u_lexema:
                if not (l=="#" or l.isdigit() or l=="a"or l=="b"or l=="c"or l=="d"or l=="e"or l=="f"):
                    Error.append(l)
                    Descripcion.append(f"No se acepta el siguiente caracter '{l}'")
                    columna_E.append((x-(len(u_lexema)+1)+x2))
                    Fila_E.append(y)     
                x2+=1     


def q0257(cadena,estado,x,y):
    if cadena==avanzar[estado]:
        comprobar(estado,x,y)
        if estado==0 or estado==2:
            columna_T.append(x)
            Fila_T.append(y)
        estado+=1
        return estado
    else:
        Error.append(cadena)
        Descripcion.append(f"Fuera de la estructura")
        columna_E.append(x)
        Fila_E.append(y)
        return estado
def q13469(cadena,estado,x,y):
    if cadena.isalpha() or cadena.isdigit() or cadena=='.' or cadena=='_' or cadena =='>' or cadena== '<' or cadena=='/' or cadena=="#":
        if cadena==avanzar[estado]:
            if not estado==6 or not estado==9:
                texto=""
                for c in texto_tem:
                    texto+=c
                if estado==1:
                    Token.append(texto)
                    Lexema.append(" ")
                elif estado ==3:
                    Token.append(texto)
                elif estado==4:
                    Lexema.append(texto)
                for i in range(len(texto_tem)):
                    texto_tem.pop()
            if estado==9:
                estado=0
            else:
                estado+=1
        elif not estado==6 or not estado==9:
            texto_tem.append(cadena)
        return estado
    else:
        Error.append(cadena)
        Descripcion.append(f"No se permite el caracter")
        columna_E.append(x)
        Fila_E.append(y)
        return estado

def q8(cadena,estado,x,y):
    if cadena==avanzar[estado]:
        estado+=1
        return estado
    elif cadena.isalpha() or cadena.isdigit() or cadena=='.' or cadena=='_' or cadena =='>' or cadena== '<' or cadena=='/' or cadena=="#":
        columna_T.append(x-1)
        Fila_T.append(y) 
        estado=3
        return q13469(cadena,estado,x,y)
    else:
        Error.append(cadena)
        Descripcion.append(f"No se acepta en el token")
        columna_E.append(x)
        Fila_E.append(y)
        return estado

def operacion(caracter,estado,x,y):
    if estado==0 or estado==2  or estado==5 or estado==7: 
        estado=q0257(caracter,estado,x,y)
    elif estado==1 or estado==3 or estado==4 or estado==6 or estado==9: 
        estado=q13469(caracter,estado,x,y)
    elif estado==8:
        estado=q8(caracter,estado,x,y)
    return estado



def tablas():
    try:
        f = open('tabla_Error.html','w')
        mensaje="""
        <html>
            <head><title>Tabla</title></head>
            <body>
                <h1>Tabla de error </h1>
                <TABLE BORDER>
                    <TR>
                        <TH>No</TH> <TH>Fila</TH> <TH>Columna</TH><TH>Caracter</TH> <TH>Descripcion</TH>
                    </TR>
            """
        n=0
        mensaje2=""
        for e in Error:
            n+=1
            temp_mensaje=f"""
                        <TR>
                            <TD>{n}</TD> <TD>{Fila_E[n-1]}</TD> <TD>{columna_E[n-1]}</TD><TD>{Error[n-1]}</TD><TD>{Descripcion[n-1]}</TD>
                        </TR>"""
            mensaje3="""
                    </TABLE>
                </body>
            </html>
                """
            mensaje2+=temp_mensaje
        mensajefinal=mensaje+mensaje2+mensaje3
        f.write(mensajefinal)
        f.close()

        g = open('tabla_Token.html','w')
        mensaje="""
        <html>
            <head><title>Tabla</title></head>
            <body>
                <h1>Tabla de Token </h1>
                <TABLE BORDER>
                    <TR>
                        <TH>No</TH> <TH>Lexema</TH> <TH>Fila</TH><TH>Columna</TH> <TH>Token</TH>
                    </TR>
            """
        n=0
        mensaje2=""
        for e in Lexema:
            n+=1
            temp_mensaje=f"""
                        <TR>
                            <TD>{n}</TD> <TD>{Lexema[n-1]}</TD> <TD>{Fila_T[n-1]}</TD><TD>{columna_T[n-1]}</TD><TD>{Token[n-1]}</TD>
                        </TR>"""
            mensaje3="""
                    </TABLE>
                </body>
            </html>
                """
            mensaje2+=temp_mensaje
        mensajefinal=mensaje+mensaje2+mensaje3
        g.write(mensajefinal)
        g.close()

        nombreArchivo = 'C:/Users/angge/tabla_Error.html'
        webbrowser.open_new_tab(nombreArchivo)
        nombreArchivo = 'C:/Users/angge/tabla_Token.html'
        webbrowser.open_new_tab(nombreArchivo)
    except:
        print("No se pudo realizar las tablas")
    
def cargar_archivo():
    try:
        ruta=str(input("Ingrese la ruta del archivo"))
        archivo=open(ruta, encoding="utf8")
        #n=0
        estado=0
        x=0
        y=0
        for linea in archivo:
            y+=1
            x=0
            for caracter in linea:
                x+=1
                caracte=caracter.lower()
                caracterf=caracte.strip()
                if caracterf=="":
                    continue   
            
                estado=operacion(caracterf,estado,x,y)
        tablas()
        archivo.close()
        
        if input()=="exit":
            menu()
    except:
        print("No se pudo abrir el documento")
        menu()


def graficoMapa():
    try:
        archivo=open('graficaMapa.dot', 'w')
        contenido="digraph mapa{"
        n=0
        estamos="nada"
        Nodo_nombre=list()
        Nodo_color=list()
        Nodo_estado=list()
        C_nombre=list()
        C_peso=list()
        C_fin=list()
        C_inicio=list()
        for p in Token:
            texto_tem=""
            if Token[n]=="estacion":
                estamos="estacion"
            elif Token[n]=="ruta":
                estamos="ruta"
            elif Token[n]=="nombre" and estamos=="estacion":
                Nodo_nombre.append(Lexema[n])
            elif Token[n]=="color" and estamos=="estacion":
                Nodo_color.append(Lexema[n])
            elif Token[n]=="estado" and estamos=="estacion":
                Nodo_estado.append(Lexema[n])
            elif Token[n]=="nombre" and estamos=="ruta":
                C_nombre.append(Lexema[n])
            elif Token[n]=="peso" and estamos=="ruta":
                C_peso.append(Lexema[n])
            elif Token[n]=="inicio" and estamos=="ruta":
                C_inicio.append(Lexema[n])
            elif Token[n]=="fin" and estamos=="ruta":
                C_fin.append(Lexema[n])
            n+=1
        n=0
        for p in Nodo_nombre:
            temp_contenido=f""" 
{Nodo_nombre[n]} [label="{Nodo_nombre[n]}
{Nodo_estado[n]}" style="filled" fillcolor="{Nodo_color[n]}"];
"""
            contenido+=temp_contenido
            n+=1
        n=0
        for p in C_nombre:
            temp_contenido=f""" 
{C_inicio[n]}->{C_fin[n]}[label="{C_nombre[n]} 
peso: {C_peso[n]}" ];
"""
            contenido+=temp_contenido
            n+=1
        contenido+="}"
        archivo.write(contenido)
        archivo.close()
        
        os.system('dot -Tpng grafica.dot -o imagenlab.png')
    except:
        menu()

def graficoRutas():
        v_inicio=str(input("Ingresar la estacion de inicio"))
        v_fin=str(input("Ingresar la estacion final"))
        estamos="nada"
        estaciones=list()
        Nodo_color=list()
        Nodo_estado=list()
        C_nombre=list()
        C_peso=list()
        C_fin=list()
        C_inicio=list()
        n=0
        for p in Token:
            if Token[n]=="estacion":
                estamos="estacion"
            elif Token[n]=="ruta":
                estamos="ruta"
            elif Token[n]=="nombre" and estamos=="estacion":
                estaciones.append(Lexema[n])
            elif Token[n]=="color" and estamos=="estacion":
                Nodo_color.append(Lexema[n])
            elif Token[n]=="estado" and estamos=="estacion":
                Nodo_estado.append(Lexema[n])
            elif Token[n]=="nombre" and estamos=="ruta":
                C_nombre.append(Lexema[n])
            elif Token[n]=="peso" and estamos=="ruta":
                C_peso.append(Lexema[n])
            elif Token[n]=="inicio" and estamos=="ruta":
                C_inicio.append(Lexema[n])
            elif Token[n]=="fin" and estamos=="ruta":
                C_fin.append(Lexema[n])
            n+=1
        q=0
        for p in estaciones:
            if p==v_inicio or p==v_fin:
                q+=1 
        posicion=list()
        cabeza=list()
        if  q==2:
            n=0
            k=len(C_inicio)-1
            cabeza.append(v_inicio)
            try:
                while True:
                    if cabeza[len(cabeza)-1]==v_fin:
                        cabeza.append(v_fin)
                        break
                    elif cabeza[len(cabeza)-1]==C_inicio[n]:
                        cabeza.append(C_fin[n])
                        posicion.append(n)
                        n=0
                    elif k==n:
                        cabeza.pop()
                        posicion.pop()
                        posicion[len(posicion)-1]+=1
                        n=0
                    n+=1
            except:
                print("Error al intentar encontrar una ruta")
                menu()
        print(cabeza)
        print(posicion)

        archivo=open('graficaRuta.dot', 'w')
        contenido="digraph Ruta{"

        n=0
        k=0
        posciones2=list()
        for p in estaciones:

            if k==(len(cabeza)-1):
                break
            elif p==cabeza[k]:
                posciones2.append(n)
                k+=1
            n+=1

        for p in posciones2:
            temp_contenido=f""" 
{estaciones[p]} [label="{estaciones[p]}
{Nodo_estado[p]}" style="filled" fillcolor="{Nodo_color[p]}"];
"""
            contenido+=temp_contenido

        for p in posicion:
            temp_contenido=f""" 
{C_inicio[p]}->{C_fin[p]}[label="{C_nombre[p]} 
peso: {C_peso[p]}" ];
"""
            contenido+=temp_contenido
        contenido+="}"
        archivo.write(contenido)
        archivo.close()



    
menu()   