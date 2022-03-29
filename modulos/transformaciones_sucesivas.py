#RECIBE UNA LISTA CON TODAS LAS TRANSFORMACIONES
#LAS AGRUPA PARA HACER TRANSFORMACIONES SUCESIVAS
def transformaciones_sucesivas(lista_opciones):
    retorno = {}
    escalamientos =[]
    traslaciones = []
    #LAS ROTACIONES SOLO SE PUEDEN AGRUPAR SI TIENEN EL MISMO PUNTO REFERENCIA
    rotaciones = {}
    puntos = []
    for transformacion in lista_opciones:
        if transformacion["transformacion"]=="escalar":
            escalamientos.append(transformacion)
        elif transformacion["transformacion"]=="traslacion":
            traslaciones.append(transformacion)
        elif transformacion["transformacion"] == "rotacion":       
            if str(transformacion["coordenada"]) not in rotaciones.keys():
                rotaciones[str(transformacion["coordenada"])] = [transformacion["grados"]]
                puntos.append(transformacion["coordenada"])
            else:
                rotaciones[str(transformacion["coordenada"])].append(transformacion["grados"])
            
    #AGRUPA LOS ESCALAMIENTOS   
    factor = 1
    tras_x = 0
    tras_y = 0
    
    #SI NO EXISTEN ESCALAMIENTOS
    if len(escalamientos)==0:
        retorno["escala"] = 0
    #SI EXISTEN, MULTIPLICALOS
    else:
        print (escalamientos)
        for escalamiento in escalamientos:
            factor = factor*(escalamiento["escala"]/100)
        retorno["escala"] = factor*100
    #SI NO EXISTEN TRASLACIONES
    if len(traslaciones)==0:
        retorno["traslado"] = [0,0]
    #SI SI EXISTEN, SUMALOS
    else:
        for traslacion in traslaciones:
            tras_x = tras_x+traslacion["coordenada"][0]
            tras_y = tras_y+traslacion["coordenada"][1]
        retorno["traslado"] = [tras_x, tras_y]
    #SI NO HAY ROTACIONES
    if len(rotaciones.keys())==0:
        retorno["rotaciones"] = False
    #SI SI HAY, ENTONCES, POR CADA UNO DE LOS PUNTOS A ROTAR, SUMA LOS GRADOS
    else:
        retorno["rotaciones"]={}
        for punto in rotaciones:
            retorno["rotaciones"][str(punto)] = sum(rotaciones[punto])
    
    return retorno