import traceback

def valida_coordenadas(cadena):
    retorno = {}
    #SOLO DEBE TENER UNA COMA
    if cadena.count(',')!=1:
        retorno["comas"] = False
        retorno ["coordenadas"] = None
    else:
        retorno["comas"] = True
    #LOS DOS RESULTADOS DEBEN PODERSE CONVERTIR A ENTERO
    cadena=cadena.strip().split(',')
    try:
        cadena[0]=int(cadena[0].strip())
        cadena[1]=int(cadena[1].strip())
        retorno["coord_enteras"] = True
        retorno ["coordenadas"] = [cadena[0], cadena[1]]
    except:
        retorno["coord_enteras"] = False
        retorno ["coordenadas"] = None
    #RETORNA EL OBJETO
    return retorno
    

#DA UN PROMPT PREGUNTANDO POR DIFERENTES OPCIONES PARA EL PROGRAMA
#RETORNA UN DICCIONARIO DE OPCIONES
def opciones(dibujar=0):
    retorno = {}
    retorno["opcion_dibujo"] = 0
    #PREGUNTA POR LA OPCION DE DIBUJAR 
    if dibujar==0:
        while retorno["opcion_dibujo"]==0:
            print("PROGRAMA DE GRAFICACIÓN\nELIJA UNA OPCION")
            print("1.- DIBUJAR UN CIRCULO")
            print("2.- DIBUJAR UNA RECTA")
            print("3.- DIBUJAR UN POLIGONO")
            try:
                retorno["opcion_dibujo"] = int(input())
            except:
                print("OPCIÓN INCORRECTA, VUELVA A INTENTARLO")
            if retorno["opcion_dibujo"] >3 or retorno["opcion_dibujo"] < 1:
                print("OPCIÓN INCORRECTA, VUELVA A INTENTARLO")
    #DEPENDIENDO DE LA OPCION DE DIBUJO
    #DIBUJA UN CIRCULO
    if retorno["opcion_dibujo"] == 1:
        retorno["radio"] = None
        while retorno["radio"]==None:
            print("INTRODUCE EL RADIO DEL CIRCULO")
            try:
                retorno["radio"] = int(input())
            except:
                print("VALOR INCORRECTO, VUELVA A INTENTARLO")
    #DIBUJA UNA RECTA
    if retorno["opcion_dibujo"] == 2:
        retorno["coordenada_inicio"] = None
        retorno["coordenada_final"] = None
        while retorno["coordenada_inicio"]==None or retorno["coordenada_final"]==None:
            print("INTRODUCE LA COORDENADA DE INICIO, DOS ENTEROS SEPARADOS POR COMA e.g 5,7")
            retorno["coordenada_inicio"] = input()
            retorno["coordenada_inicio"] = valida_coordenadas(retorno["coordenada_inicio"])
            if retorno["coordenada_inicio"]["comas"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE UNA COMA PARA SEPARAR LOS VALORES")
                retorno["coordenada_inicio"] = None
                continue
            elif retorno["coordenada_inicio"]["coord_enteras"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE VALORES ENTEROS EN LAS COORDENADAS")
                retorno["coordenada_inicio"] = None
                continue
            else:
                retorno["coordenada_inicio"]=retorno["coordenada_inicio"]["coordenadas"]
            print("INTRODUCE LA COORDENADA FINAL, DOS ENTEROS SEPARADOS POR COMA e.g 5,7")
            retorno["coordenada_final"] = input()
            retorno["coordenada_final"] = valida_coordenadas(retorno["coordenada_final"])
            if retorno["coordenada_final"]["comas"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE UNA COMA PARA SEPARAR LOS VALORES")
                retorno["coordenada_final"] = None
                continue
            elif retorno["coordenada_final"]["coord_enteras"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE VALORES ENTEROS EN LAS COORDENADAS")
                retorno["coordenada_final"] = None
                continue
            else:
                retorno["coordenada_final"]=retorno["coordenada_final"]["coordenadas"]
    #DIBUJA UN POLIGONO
    if retorno["opcion_dibujo"] == 3:
        retorno["aristas"] = []
        retorno["cierre_fig"] = False
        #PARA QUE EXISTA UN POLIGONO DEBEN HABER AL MENOS 3 ARISTAS
        #SI EL USUARIO ARRIBA DE LAS 3 ARISTAS CIERRA LA FIGURA TAMBIEN ROMPE EL CICLO
        while retorno["cierre_fig"] == False:
            print("INTRODUCE UNA COORDENADA, DOS ENTEROS SEPARADOS POR COMA e.g 5,7")
            #CIERRE DE FIGURA
            print("PARA CERRAR LA FIGURA, NO INTRODUZCAS NADA Y SOLO DA ENTER")
            retorno["coordenada"] = input()
            if retorno["coordenada"].strip() == '':
                #SI AUN NO SON 3 ARISTAS AL MENOS MARCA ERROR
                if len(retorno["aristas"])<3:
                    print("SE REQUIEREN AL MENOS 3 ARISTAS PARA CERRAR UN POLIGONO")
                    continue
                else:
                    #CIERRA LA FIGURA Y EL CICLO
                    retorno["cierre_fig"] = True
                    break
            retorno["coordenada"] = valida_coordenadas(retorno["coordenada"])
            if retorno["coordenada"]["comas"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE UNA COMA PARA SEPARAR LOS VALORES")
                retorno["coordenada"] = None
                continue
            elif retorno["coordenada"]["coord_enteras"] == False:
                print("ERROR, INDTRODUCE SOLAMENTE VALORES ENTEROS EN LAS COORDENADAS")
                retorno["coordenada"] = None
                continue
            else:
                retorno["aristas"].append(retorno["coordenada"]["coordenadas"])

    return retorno

    
    
def opciones_trans(puntos_fig=None):
    retorno = {}
    retorno["cumulo_transformaciones"] = []
    retorno["transformacion_terminada"] = False
    retorno["trans"]=0
    while not retorno["transformacion_terminada"]:
        if retorno["trans"]==0:
            while retorno["trans"]==0:
                print("INTRODUCE LA TRANSFORMACION QUE DESEAS APLICAR")
                print("SI QUIERES TERMINAR EL PROCEDIMIENTO PRESIONA ENTER SIN INTRODUCIR NADA")
                print("1.- ESCALAR")
                print("2.- TRASLADAR")
                print("3.- ROTAR")
                try:
                    retorno["trans"] = input()
                    #SI SE INTENTA TERMINAR EL PROCEDIMIENTO 
                    if str(retorno["trans"].strip())=='':
                        #SI NO SE HA INTRODUCIDO ALGUNA TRANSFORMACION MARCA EL ERROR
                        if len(retorno["cumulo_transformaciones"])==0:
                            print("INTRODUCE AL MENOS UNA TRANSFORMACION")
                        else:
                            retorno["transformacion_terminada"] = True
                            retorno["trans"]=1
                            break
                    else:
                        try:
                            retorno["trans"] = int(retorno["trans"])
                        except:
                            print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                except:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                if retorno["trans"]>3 or retorno["trans"]<1:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                    retorno["trans"]=0
                             
               
        if retorno["transformacion_terminada"]:
            break
        #OPCIONES DE ESCALAMIENTO
        if retorno["trans"]==1:
            escalar={}
            escalar["transformacion"]="escalar"
            escalar["escala"]=0
            #PREGUNTA POR UN NUMERO PORCENTAJE DE ESCALA
            #NO PERMITAS EL 0
            while escalar["escala"]<=0:
                print("INTRODUCE UN PORCENTAJE ENTERO A ESCALAR, MAYOR 0")
                try:
                    escalar["escala"] = int(input())
                except:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                if escalar["escala"]<=0 :
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
            retorno["cumulo_transformaciones"].append(escalar)
            #REGRESA AL MENU DE PREGUNTAS
            retorno["trans"]=0

        #OPCIONES DE TRASLACION
        elif retorno["trans"]==2:
            traslacion={}
            traslacion["transformacion"]="traslacion"
            traslacion["coordenada"]=[0,0]
            trasladado = False
            #PREGUNTA POR UN PAR ORDENADO DE TRASLACION
            while not trasladado:
                print("INTRODUCE UN ENTERO A TRASLADAR EN X Y OTRO EN Y, SEPARADOS POR UNA COMA")
                try:
                    traslacion["coordenada"] = input()
                except:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                traslacion["coordenada"] = valida_coordenadas(traslacion["coordenada"])
                if traslacion["coordenada"]["comas"] == False:
                    print("ERROR, INDTRODUCE SOLAMENTE UNA COMA PARA SEPARAR LOS VALORES")
                    traslacion["coordenada"] = None
                    continue
                elif traslacion["coordenada"]["coord_enteras"] == False:
                    print("ERROR, INDTRODUCE SOLAMENTE VALORES ENTEROS EN LAS COORDENADAS")
                    traslacion["coordenada"] = None
                    continue
                else:
                    traslacion["coordenada"]=(traslacion["coordenada"]["coordenadas"])
                    trasladado = True   
            retorno["cumulo_transformaciones"].append(traslacion)
            #REGRESA AL MENU DE PREGUNTAS
            retorno["trans"]=0
            
        #OPCIONES DE TRASLACION
        elif retorno["trans"]==3:
            rotacion={}
            rotacion["transformacion"]="rotacion"
            rotacion["grados"]=0
            rotacion["coordenada"] = [0,0]
            coordenada = False
            grado = False
            #PREGUNTA POR UNA COORDENADA REFERENCIA
            while not coordenada:
                print("INTRODUCE LA CORDENADA DE REFERENCIA A PARTIR DE LA CUAL SE ROTARÁ, SEPARADOS POR UNA COMA")
                try:
                    rotacion["coordenada"] = input()
                except:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                rotacion["coordenada"] = valida_coordenadas(rotacion["coordenada"])
                if rotacion["coordenada"]["comas"] == False:
                    print("ERROR, INDTRODUCE SOLAMENTE UNA COMA PARA SEPARAR LOS VALORES")
                    rotacion["coordenada"] = None
                    continue
                elif rotacion["coordenada"]["coord_enteras"] == False:
                    print("ERROR, INDTRODUCE SOLAMENTE VALORES ENTEROS EN LAS COORDENADAS")
                    rotacion["coordenada"] = None
                    continue
                else:
                    #rotacion["coordenada"]=(rotacion["coordenada"]["coordenadas"])   
                    #VERIFICA QUE LA COORDENADA SE ENCUENTRE EN LA FIGURA
                    if rotacion["coordenada"]["coordenadas"] not in puntos_fig:
                        #SI NO, MANDA MENSAJE
                        print("EL PUNTO DE REFERENCIA NO PERTENECE A LA FIGURA")
                        continue
                    else:
                        rotacion["coordenada"]=(rotacion["coordenada"]["coordenadas"])
                        coordenada = True
            while not grado:
                print("INTRODUCE LOS GRADOS PARA ROTAR LA FIGURA")
                try:
                    rotacion["grados"] = int(input())
                except:
                    print("OPCION EQUIVOCADA, INTENTALO NUEVAMENTE")
                grado=True
                

            retorno["cumulo_transformaciones"].append(rotacion)
            #REGRESA AL MENU DE PREGUNTAS
            retorno["trans"]=0
    return retorno