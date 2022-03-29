def rotacion_y(punto, tamanio_y):
    eje_espejo = int(tamanio_y/2)
    nvo_pto_y = eje_espejo-punto[1]+eje_espejo
    return [punto[0], nvo_pto_y]


    #600
    #3,2
    #Espejo

    #600/2=300
    #300-2+300=298+300=598