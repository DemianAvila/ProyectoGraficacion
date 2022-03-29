"""
//--------------------------------------------
/*###########################################*/
/*# Universidad Nacional Autónoma de México #*/
/*# Facultad de Estudios Superiores Aragón  #*/
/*# Ingeniería en computación               #*/
/*# Algoritmo Bresenham                     #*/
/*###########################################*/
/*# Asignatura:                             #*/
/*# Graficación por computadora             #*/
/*###########################################*/
/*# Alumnos:                                #*/
/*# Amador Taboada Diego Uriel              #*/
/*# Andrade Rios Juan Manuel                #*/
/*# Arredondo Jimenez Alan Daniel           #*/
/*# Avila Romero Josue Demian               #*/
/*# Ramirez Tapia Luis Fernando             #*/
/*# Profesor:                               #*/
/*# Liliana Hernández Cervantes             #*/
/*###########################################*/
/*# Grupo:                                  #*/
/*# 2058                                    #*/
/*# Semestre:                               #*/
/*# 2022-II                                 #*/
/*# Turno:                                  #*/
/*# Vespertino                              #*/
/*# Fecha de entrega:                       #*/
/*# 29/03/2022                              #*/
/*###########################################*/
"""


from modulos.opciones import *
from modulos.recta_poligono import *
from modulos.circulo import *
from modulos.rotacion_y import *
from modulos.transformaciones_sucesivas import *
import pygame
from pygame.locals import *
from pygame import gfxdraw
from math import radians

def main():
    fondo = (0, 0, 0)
    verde= (0,255,0)
    pantalla = pygame.display.set_mode((1000, 600))
    
    # Set the caption of the screen
    pygame.display.set_caption("Proyecto de graficación por computadora")
    
    corriendo = True
    #opciones
    ciclo_opt = 0
    #el ciclo 0 de opciones es el dibujo de una figura
    #el ciclo 1 de opciones son las transformaciones

    while corriendo:
        #PARA CERRAR LA VENTANA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        ######
        
        #INICIALIZA EL MENU DE OPCIONES
        if ciclo_opt==0:
            opt = opciones()
            #CREA UN OBJETO CIRCULO
            if opt["opcion_dibujo"]==1:   
                #POR DEFECTO SE DIBUJA EN EL CENTRO
                circulo = Circulo(opt["radio"],0,0)
                puntos=circulo.puntos_circulo()
                print(puntos)
            #CREA UN OBJETO RECTA
            elif opt["opcion_dibujo"]==2:
                recta = Recta(opt["coordenada_inicio"][0],
                opt["coordenada_inicio"][1],
                opt["coordenada_final"][0],
                opt["coordenada_final"][1])
                puntos=recta.puntos_recta()
            #CREA UN OBJETO POLIGONO
            elif opt["opcion_dibujo"]==3:
                poligono = Poligono(opt["aristas"])
                puntos=poligono.puntos_figura()
        
        #SEGUNDO CICLO DE OPCIONES, LAS TRANSFORMACIONES
        if ciclo_opt==30:
            if opt["opcion_dibujo"]==1:
                transformaciones = opciones_trans(circulo.puntos_circulo())
            elif opt["opcion_dibujo"]==2:
                transformaciones = opciones_trans([recta.get_cord_ini(), recta.get_cord_fin()])
            elif opt["opcion_dibujo"]==3:
                transformaciones = opciones_trans(poligono.get_aristas())
                print(transformaciones)
            #AGRUPA LAS TRANSFORMACIONES
            transformaciones = transformaciones_sucesivas(transformaciones["cumulo_transformaciones"])
            print(transformaciones)
            #CIRCULO
            if opt["opcion_dibujo"]==1:
                #SI HAY ESCALAMIENTOS
                if transformaciones["escala"]!=0:
                    #PARA ESCALAR EL CIRCULO, HAY QUE CAMBIAR SU RADIO
                    n_radio = round((circulo.get_radio()*transformaciones["escala"])/100)
                    circulo.set_radio(n_radio)
                    puntos = circulo.puntos_circulo()
                    print(puntos)
                #SI HAY TRASLACIONES, MOVER CADA UNO DE LOS PUNTOS DEL CIRCULO
                if transformaciones["traslado"]!=[0,0]: 
                    #TRASLADA CADA UNO DE LOS PUNTOS 
                    nvos_puntos = []               
                    for punto in puntos:
                        nvos_puntos.append([punto[0]+transformaciones["traslado"][0],
                            punto[1]+transformaciones["traslado"][1]])
                    puntos = nvos_puntos
                    print(puntos)
                #SI HAY ROTACIONES
                if transformaciones["rotaciones"]!=False:
                    #POR CADA UNO DE LOS PUNTOS A ROTAR
                    nvos_puntos = []    
                    for punto in puntos:
                        for rotacion in transformaciones["rotaciones"]:
                            grados = radians(transformaciones["rotaciones"][rotacion])
                            str_lista = list(map(lambda x: int(x.strip()) , rotacion[1:-1].split(',')))
                            x_ref = str_lista[0]
                            y_ref = str_lista[1]
                            x = punto[0]
                            y = punto[1]
                            x_prim = (x_ref+((x-x_ref)*cos(grados)))-((y-y_ref)*sin(grados))
                            print(f"({x_ref}+(({x}-{x_ref})*cos({grados})))-(({y}-{y_ref})*sin({grados}))")
                            y_prim = (y_ref+((x-x_ref)*sin(grados)))+((y-y_ref)*cos(grados))
                            print(f"({y_ref}+(({x}-{x_ref})*sin({grados})))+(({y}-{y_ref})*cos({grados}))")
                            punto = [round(x_prim), round(y_prim)]
                        nvos_puntos.append(punto)
                    puntos = nvos_puntos
                    print(puntos)
            elif opt["opcion_dibujo"]==2:
                #SI HAY ESCALAMIENTOS
                if transformaciones["escala"]!=0:
                    recta.escalar(transformaciones["escala"])
                #SI HAY TRASLACIONES
                if transformaciones["traslado"]!=[0,0]:
                    recta.trasladar(transformaciones["traslado"][0], transformaciones["traslado"][0])
                #SI HAY ROTACIONES
                if transformaciones["rotaciones"]!=False:
                    #POR CADA UNO DE LOS PUNTOS A ROTAR
                    for punto in transformaciones["rotaciones"]:
                        #ROTAR, CONVIERTE UN STRING A LISTA
                        recta.rotar(list(map(lambda x: int(x.strip()) ,punto[1:-1].split(','))), 
                        transformaciones["rotaciones"][punto])
                puntos= recta.puntos_recta()
            #TRANSFORMACIONES PARA POLIGONO
            if opt["opcion_dibujo"]==3:
                #SI HAY ESCALAMIENTOS
                if transformaciones["escala"]!=0:
                    poligono.escalar(transformaciones["escala"])
                #SI HAY TRASLACIONES
                if transformaciones["traslado"]!=[0,0]:
                    poligono.trasladar(transformaciones["traslado"][0], transformaciones["traslado"][0])
                #SI HAY ROTACIONES
                if transformaciones["rotaciones"]!=False:
                    #POR CADA UNO DE LOS PUNTOS A ROTAR
                    for punto in transformaciones["rotaciones"]:
                        #ROTAR, CONVIERTE UN STRING A LISTA
                        poligono.rotar(list(map(lambda x: int(x.strip()) ,punto[1:-1].split(','))), 
                        transformaciones["rotaciones"][punto])
                puntos = poligono.puntos_figura()
         
        ######
        if ciclo_opt < 40:
            ciclo_opt+=1
        pantalla.fill(fondo)

        for punto in puntos:
            punto = rotacion_y(punto, 600)
            pygame.draw.line(pantalla, verde, (punto[0],punto[1]), (punto[0],punto[1]), 1)
        
        pygame.display.flip()

if __name__=="__main__":
    main()