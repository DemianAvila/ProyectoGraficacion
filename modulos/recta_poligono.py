from math import sqrt
from math import cos
from math import sin
from math import radians

#--------------------------------------------------
#DEFINICION DE FUNCIONES
#DECLARACION DE LA FUNCION PENDIENTE
#VERIFICA SI LA PENDIENTE ES VERTCAL, 1 si si, 0 si no

def pendiente_vertical(x1, y1, x2, y2):
    divisor= x2-x1
    if (divisor==0):
        return 1
    
    else:
        return 0
    

#VERIFICA SI LA PENDIENTE ES HORIZONTAL, 1 si si, 0 si no
def pendiente_horizontal(x1, y1, x2, y2):
    dividendo= y2-y1
    if (dividendo==0):
        return 1
    
    else:
        return 0
    

#CALCULA LA PENDIENTE DADOS 2 PUNTOS EN UN PLANO CARTESIANO
def pendiente (x1, y1, x2, y2):
    divisor= x2-x1
    dividendo= y2-y1
    #MANEJO DE ERROR
    if (divisor==0):
        return 0
    else:
        return (dividendo/divisor)
    

#CALCULA EL MENOR DE LOS 4 PUNTOS
def menor_arr(x1, y1, x2, y2):
    arr = [x1, y1, x2, y2]
    menor = x1
    for i in range(4):
        if (arr[i] < menor ):
            menor = arr[i]
    return menor


def hipotenusa_al_origen(x, y):
    hipo= sqrt((pow(x,2))+(pow(y,2)))
    return hipo

class Recta:
    def __init__(self, cord_ini_x, cord_ini_y,
        cord_fin_x, cord_fin_y):
        self.coordenada_inicial_x = cord_ini_x
        self.coordenada_inicial_y = cord_ini_y
        self.coordenada_inicial = [cord_ini_x, cord_ini_y]
        self.coordenada_final_x = cord_fin_x
        self.coordenada_final_y = cord_fin_y
        self.coordenada_final = [cord_fin_x, cord_fin_y]

    #GETTERS
    def get_cord_ini_x(self):
        return self.coordenada_inicial_x

    def get_cord_ini_y(self):
        return self.coordenada_inicial_y
    
    def get_cord_ini(self):
        return self.coordenada_inicial

    def get_cord_fin_x(self):
        return self.coordenada_final_x

    def get_cord_fin_y(self):
        return self.coordenada_final_y
    
    def get_cord_fin(self):
        return self.coordenada_final
    
    #SETTERS
    def set_cord_ini_x(self, x):
        self.coordenada_inicial_x = x
        self.coordenada_inicial = [x, self.coordenada_inicial_y]

    def set_cord_ini_y(self,y):
        self.coordenada_inicial_y = y
        self.coordenada_inicial = [self.coordenada_inicial_x, y]
    
    def set_cord_ini(self, x, y):
        self.set_cord_ini_x(x)
        self.set_cord_ini_y(y)

    def set_cord_fin_x(self, x):
        self.coordenada_final_x = x
        self.coordenada_final = [x, self.coordenada_final_y]

    def set_cord_fin_y(self,y):
        self.coordenada_final_y = y
        self.coordenada_final = [self.coordenada_final_x, y]
    
    def set_cord_fin(self, x, y):
        self.set_cord_fin_x(x)
        self.set_cord_fin_y(y)
    
    def cord_in_recta(self, cord):
        if cord==self.get_cord_ini() or cord==self.get_cord_fin():
            return True
        else:
            return False

    #ALGORITMO DE BRESENHAM PARA DIBUJADO DE RECTAS
    def puntos_recta(self):
        #ARREGLO QUE ALMACENA LOS PUNTOS
        coordenadas = []
        #BANDERA QUE INDICA SI LA RECTA TUVO QUE SER TRASLADADA
        traslacion = 0
        #CONTADOR DE INSERCIÓN DE VECTORES
        cont = 0
        #ALMACENA LAS COORDENADAS
        coordenada=[]
        #------------------------------------------------------
        #ALIAS DE LOS PUNTOS
        x1, y1 = self.get_cord_ini()
        x2, y2 = self.get_cord_fin()
        #--------------------------------------------------
        #ALGUNO DE LOS PUNTOS ES NEGATIVO?
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            #DE SER ASI, OBTEN EL MENOR DE LOS PUNTOS
            menor = menor_arr(x1,y1,x2,y2)
            #CONVIERTELO A POSITIVO
            menor = menor*-1
            #CONVIERTE CADA PUNTO A POSITIVO AL SUMARLE EL MENOR CONVERTICO A POSITIVO
            x1 = x1+menor
            y1 = y1+menor
            x2 = x2+menor
            y2 = y2+menor
            #INDICA QUE LA RECTA SE TRASLADO
            traslacion = 1
        
        #--------------------------------------------------------------------
        #REASIGNA PUNTO INICIAL Y PUNTO FINAL EN CASO DE QUE EL FINAL ESTÉ MAS A LA IZQUIERDA
        if hipotenusa_al_origen(x1,y1) > hipotenusa_al_origen(x2,y2):
            tmpx = x1
            tmpy = y1
            x1 = x2
            y1 = y2
            x2 = tmpx
            y2 = tmpy
        #--------------------------------------------------
        #TIPO DE LA PENDIENTE
        #1 VERTICAL, 2 HORIZONTAL, 3 OTRO
        tipo_pendiente=0
        #OBTEN LA PENDIENTE
        #VERIFICA QUE LA PENDIENTE NO EXISTE, ES DECIR, QUE ES VERTICAL
        m_vertical = pendiente_vertical(x1, y1, x2, y2)
        m_no_vert = pendiente(x1, y1, x2, y2)

        if m_vertical==1:
            tipo_pendiente=1
        
        else:
            if pendiente_horizontal(x1,y1,x2,y2)==1:
                tipo_pendiente=2
            
            else:
                tipo_pendiente=3
        #SI EL TIPO DE LA PENDIENTE ES VERICAL, SOLO AUMENTA y hasya que y1=y2
        #----------------------------------------------------------------
        if tipo_pendiente==1:
            #SI EL PRIMER PUNTO ES MENOR QUE EL SEGUNDO, AUMENTALO HASTA QUE LLEGUE A EL
            if y1 < y2:
                while y1 <= y2:
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    y1+=1
                
            
            #SI EL SEGUNDO PUNTO ES MENOR, AUMENTA ESE EN SU LUGAR
            elif y1 > y2:
                while y1 >= y2:
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    y2+=1
                
            
            #SI SON IGUALES, SOLO IMPRIME ESE PUNTO
            else:
                if traslacion == 1:
                    coordenada = [x1-menor, y1-menor]
                    coordenadas.insert(coordenadas.begin() + cont, coordenada)
                    cont+=1
                
                else:
                    coordenada = [x1, y1]
                    coordenadas.append(coordenada)
                    cont+=1
                
            
        
        #SI EL TIPO DE LA PENDIENTE ES HORIZONTAL, AUMENTA X HASTA QUE SEAN IGUALES
        #-----------------------------------------------------------------------
        elif tipo_pendiente==2:
            #DEFINE EL ARRAY DE LOS RESULTADOS
            #SI EL PRIMER PUNTO ES MENOR QUE EL SEGUNDO, AUMENTALO HASTA QUE LLEGUE A EL
            if x1 < x2:
                while x1 <= x2:
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    x1+=1
                
            
            #SI EL SEGUNDO PUNTO ES MENOR, AUMENTA ESE EN SU LUGAR
            elif x1 > x2:
                while y1 >= y2:
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    x2+=1
                
            
            #SI SON IGUALES, SOLO IMPRIME ESE PUNTO
            else:
                if traslacion == 1:
                    coordenada = [x1-menor, y1-menor]
                    coordenadas.append(coordenada)
                    cont+=1
                    
                else:
                    coordenada = [x1, y1]
                    coordenadas.append(coordenada)
                    cont+=1
                    
            
        
        #---------------------------------------------------------------------------
        #SI LA PENDIENTE NO ES VERTICAL NI HORIZONTAL, APLICA BRESENHAM
        elif tipo_pendiente==3:
            #PENDIENTE MENOR A -1
            if m_no_vert < -1:
                temp_x=x1
                temp_y=y1
                x1=x2
                y1=y2
                x2=temp_x
                y2=temp_y

                diff_x = abs(x2-x1)
                diff_y = abs(y2-y1)
                p = (2*diff_y)-diff_x
                for i in range(diff_x):
                    #AÑADE EL PUNTO INICIAL A LA RECTA
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    pix_vert=0
                    while p>0:
                        y1-=1
                        p-=(2*diff_x)
                        if pix_vert>0 :
                            if traslacion == 1:
                                coordenada = [x1-menor, y1-menor]
                                coordenadas.append(coordenada)
                                cont+=1
                            
                            else:
                                coordenada = [x1, y1]
                                coordenadas.append(coordenada)
                                cont+=1
                        pix_vert+=1

                    x1+=1
                    p+=(2*diff_y)
            
            #PENDIENTE MENOR A 1 y mayor a 0
            elif m_no_vert < 0 and m_no_vert>-1:
                diff_x = abs(x2-x1)
                diff_y = abs(y2-y1)
                p = (2*diff_y)-diff_x
                pasos = 0
                #EL NUMERO DE PASOS ES IGUAL AL DIFERENCIAL MAYOR
                if diff_x>=diff_y:
                    pasos = diff_x
                    #pasos = diff_y
                else:
                    pasos = diff_y
                    #pasos = diff_x

                #ARRAY PARA ALMACENAR LOS PASOS
                for i in range(pasos+1):
                    #AÑADE EL PUNTO INICIAL A LA RECTA
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    #SI P ES MENOR A 0, SUMA 1 A X Y ESA SERÁ LA NUEVA X
                    if p<0:
                        x1+=1
                        #LA NUEVA P ES P ANTERIOR + 2 CAMBIO Y
                        p = p+2*diff_y
                    
                    #SI NO, INCREMENTA AMBOS
                    else:
                        x1+=1
                        y1-=1
                        #LA NUEVA  P ES P ANTERIOR +2 CAMBIO Y - 2 CAMBIO x
                        p = p+2*diff_y-2*diff_x
                    
                    #VOLVER A CALCULAR LAS DIFERENCIAS
                    diff_x = abs(x2-x1)
                    diff_y = abs(y2-y1)

            #PENDIENTE MENOR A 1 y mayor a 0
            elif m_no_vert < 1 and m_no_vert>0:
                diff_x = abs(x2-x1)
                diff_y = abs(y2-y1)
                p = (2*diff_y)-diff_x
                pasos = 0
                #EL NUMERO DE PASOS ES IGUAL AL DIFERENCIAL MAYOR
                if diff_x>=diff_y:
                    pasos = diff_x
                    #pasos = diff_y
                else:
                    pasos = diff_y
                    #pasos = diff_x

                #ARRAY PARA ALMACENAR LOS PASOS
                for i in range(pasos+1):
                    #AÑADE EL PUNTO INICIAL A LA RECTA
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    #SI P ES MENOR A 0, SUMA 1 A X Y ESA SERÁ LA NUEVA X
                    if p<0:
                        x1+=1
                        #LA NUEVA P ES P ANTERIOR + 2 CAMBIO Y
                        p = p+2*diff_y
                    
                    #SI NO, INCREMENTA AMBOS
                    else:
                        x1+=1
                        y1+=1
                        #LA NUEVA  P ES P ANTERIOR +2 CAMBIO Y - 2 CAMBIO x
                        p = p+2*diff_y-2*diff_x
                    
                    #VOLVER A CALCULAR LAS DIFERENCIAS
                    diff_x = abs(x2-x1)
                    diff_y = abs(y2-y1)
                
            

            #PENDIENTE MAYOR A 1
            else:
                diff_x = abs(x2-x1)
                diff_y = abs(y2-y1)
                p = (2*diff_x)-diff_y
                pasos = 0
                #EL NUMERO DE PASOS ES IGUAL AL DIFERENCIAL MAYOR
                if diff_x>=diff_y:
                    pasos = diff_x
                
                else:
                    pasos = diff_y
                
                #ARRAY PARA ALMACENAR LOS PASOS
                for i in range(pasos+1):
                    #AÑADE EL PUNTO INICIAL A LA RECTA
                    if traslacion == 1:
                        coordenada = [x1-menor, y1-menor]
                        coordenadas.append(coordenada)
                        cont+=1
                    
                    else:
                        coordenada = [x1, y1]
                        coordenadas.append(coordenada)
                        cont+=1
                    

                    #SI P ES MENOR A 0, SUMA 1 A X Y ESA SERÁ LA NUEVA X
                    if p<0:
                        y1+=1
                        #LA NUEVA P ES P ANTERIOR + 2 CAMBIO Y
                        p = p+(2*diff_x)
                    
                    #SI NO, INCREMENTA AMBOS
                    else:
                        y1+=1
                        x1+=1
                        #LA NUEVA  P ES P ANTERIOR +2 CAMBIO Y - 2 CAMBIO x
                        p = p+(2*diff_x)-(2*diff_y)
                    
                    #VOLVER A CALCULAR LAS DIFERENCIAS
                    diff_x = abs(x2-x1)
                    diff_y = abs(y2-y1)
        print(coordenadas)
        print(m_no_vert)
        return coordenadas
    #[1,2] [5,6] -> 200% -> [2,4] [10,12]
    def escalar(self, factor_entero):
        factor_porcentaje = factor_entero/100
        nvo_ini = list(map(lambda x: x*factor_porcentaje ,self.get_cord_ini()))
        nvo_fin = list(map(lambda x: x*factor_porcentaje ,self.get_cord_fin()))
        self.set_cord_ini(int(nvo_ini[0]), int(nvo_ini[1]))
        self.set_cord_fin(int(nvo_fin[0]), int(nvo_fin[1]))
        return True
        
    def rotar(self, punto_ref, grados):
        print(punto_ref)
        print(grados)
        grados = radians(grados)
        #SI EL PUNTO DE REFERENCIA NO ESTÁ EN LA RECTA, REGRESA ERROR
        if punto_ref not in [self.get_cord_fin(), self.get_cord_ini()]:
            return False
        else:
            if punto_ref == self.get_cord_fin():
                x_ref = self.get_cord_fin_x()
                y_ref = self.get_cord_fin_y()
                x = self.get_cord_ini_x()
                y = self.get_cord_ini_y()
                x_prim = (x_ref+((x-x_ref)*cos(grados)))-((y-y_ref)*sin(grados))
                print(f"({x_ref}+(({x}-{x_ref})*cos({grados})))-(({y}-{y_ref})*sin({grados}))")
                y_prim = (y_ref+((x-x_ref)*sin(grados)))+((y-y_ref)*cos(grados))
                print(f"({y_ref}+(({x}-{x_ref})*sin({grados})))+(({y}-{y_ref})*cos({grados}))")
                self.set_cord_ini(round(x_prim), round(y_prim))
                return True
            elif punto_ref == self.get_cord_ini():
                x_ref = self.get_cord_ini_x()
                y_ref = self.get_cord_ini_y()
                x = self.get_cord_fin_x()
                y = self.get_cord_fin_y()
                x_prim = (x_ref+((x-x_ref)*cos(grados)))-((y-y_ref)*sin(grados))
                print(f"({x_ref}+(({x}-{x_ref})*cos({grados})))-(({y}-{y_ref})*sin({grados}))")
                y_prim = (y_ref+((x-x_ref)*sin(grados)))+((y-y_ref)*cos(grados))
                print(f"({y_ref}+(({x}-{x_ref})*sin({grados})))+(({y}-{y_ref})*cos({grados}))")
                self.set_cord_fin(round(x_prim), round(y_prim))
                return True

    def trasladar(self,x, y):
        self.set_cord_ini_x(self.get_cord_ini_x()+x)
        self.set_cord_ini_y(self.get_cord_ini_y()+y)
        self.set_cord_fin_x(self.get_cord_fin_x()+x)
        self.set_cord_fin_y(self.get_cord_fin_y()+y)        

    
#EL POLIGONO SE POMPONE DE UNA SERIE DE ARISTAS, LAS CUALES CONFORMAN RECTAS ENTRE SI
class Poligono:
    def __init__(self, aristas):
        self.aristas= aristas
    
    def get_aristas(self):
        return self.aristas
    
    def set_aristas(self, n_aristas):
        self.aristas = n_aristas

    def cord_in_aristas(self, cord):
        if cord in self.get_aristas():
            return True
        else:
            return False
    
    #APLICA BRESENHAM RECURSIVAMENTE PARA CADA UNA DE LAS RECTAS DEL POLIGONO
    def puntos_figura(self):
        puntos=[]
        for index, arista in enumerate(self.get_aristas()):
            #PARA TODAS LAS ARISTAS MENOS LA ULTIMA
            if index<((len (self.get_aristas()))-1):
                #CREA UN OBJETO RECTA PARA CADA PAR DE ARISTAS
                x1 = arista[0]
                y1 = arista [1]
                x2 = self.get_aristas()[index+1][0]
                y2 = self.get_aristas()[index+1][1]
                recta = Recta(x1, y1, x2, y2)
                #OBTEN LOS PUNTOS DE ESA RECTA
                pun = recta.puntos_recta()
                #AÑADE ESOS PUNTOS AL ARREGLO INICIAL
                puntos.extend(pun)
            #EN EL CASO DEL ULTIMO PUNTO
            #OBTEN LA RECTA ENTRE ESE Y EL PRIMERO
            elif index==((len (self.get_aristas()))-1):
                x1 = arista[0]
                y1 = arista [1]
                x2 = self.get_aristas()[0][0]
                y2 = self.get_aristas()[0][1]
                recta = Recta(x1, y1, x2, y2)
                #OBTEN LOS PUNTOS DE ESA RECTA
                pun = recta.puntos_recta()
                #AÑADE ESOS PUNTOS AL ARREGLO INICIAL
                puntos.extend(pun)
        return puntos

    def escalar(self, factor_entero):
        factor_porcentaje = factor_entero/100
        nuevas_aristas = []
        #PARA CADA ARISTA
        for arista in self.get_aristas():
            nueva_arista = [round(arista[0]*factor_porcentaje),
                round(arista[1]*factor_porcentaje)]
            nuevas_aristas.append(nueva_arista)
        
        self.set_aristas(nuevas_aristas)
        return True
        
    def rotar(self, punto_ref, grados):
        nuevas_aristas = []
        aristas_rotadas = self.get_aristas()
        #si el punto de referencia no está en las aristas, da error
        if punto_ref not in aristas_rotadas:
            return False
        #si si, continua el procedimiento
        else:
            aristas_rotadas.remove(punto_ref)
            # PARA CADA UNA DE LAS ARISTAS, APLICA LA ROTACION
            grados = radians(grados)
            for arista in aristas_rotadas:
                x_ref = punto_ref[0]
                y_ref = punto_ref[1]
                x = arista[0]
                y = arista[1]
                x_prim = (x_ref+((x-x_ref)*cos(grados)))-((y-y_ref)*sin(grados))
                print(f"({x_ref}+(({x}-{x_ref})*cos({grados})))-(({y}-{y_ref})*sin({grados}))")
                y_prim = (y_ref+((x-x_ref)*sin(grados)))+((y-y_ref)*cos(grados))
                print(f"({y_ref}+(({x}-{x_ref})*sin({grados})))+(({y}-{y_ref})*cos({grados}))")
                nuevas_aristas.append([round(x_prim), round(y_prim)])
            #AL FINAL VUELVE A AÑADIR EL PUNTO DE REFERENCIA
            nuevas_aristas.append(punto_ref)
            #ESTABLECE DICHO ARREGLO COMO LAS NUEVAS ARISTAS
            self.set_aristas(nuevas_aristas)
            return True                

    def trasladar(self,x, y):
        nuevas_aristas = []
        aristas_trasladar = self.get_aristas()
        for arista in aristas_trasladar:
            nueva_arista = [(arista[0]+x), 
                (arista[1]+y)]
            nuevas_aristas.append(nueva_arista)
        #AÑADIR EL ARREGLO COMO NUEVO CONJUNTO DE ARISTAS
        self.set_aristas(nuevas_aristas)        
