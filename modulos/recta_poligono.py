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

   
    #[1,2] [5,6] -> 200% -> [2,4] [10,12]
    def escalar(self, factor_entero):
        factor_porcentaje = factor_entero/100
        nvo_ini = list(map(lambda x: x*factor_porcentaje ,self.get_cord_ini()))
        nvo_fin = list(map(lambda x: x*factor_porcentaje ,self.get_cord_fin()))
        self.set_cord_ini(int(nvo_ini[0]), int(nvo_ini[1]))
        self.set_cord_fin(int(nvo_fin[0]), int(nvo_fin[1]))
        return True
        
    def rotar(self, punto_ref, grados):
        print(grados)
        grados = radians(grados)
        """
        #SI EL PUNTO DE REFERENCIA NO ESTÁ EN LA RECTA, REGRESA ERROR
        if punto_ref not in [self.get_cord_fin(), self.get_cord_ini()]:
            pass
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
        """
        puntos = [self.get_cord_ini(), self.get_cord_fin()]
        for index, punto in enumerate(puntos):
            x_ref = punto_ref[0]
            y_ref = punto_ref[1]
            x = punto[0]
            y = punto[1]
            x_prim = (x_ref+((x-x_ref)*cos(grados)))-((y-y_ref)*sin(grados))
            print(f"({x_ref}+(({x}-{x_ref})*cos({grados})))-(({y}-{y_ref})*sin({grados}))")
            y_prim = (y_ref+((x-x_ref)*sin(grados)))+((y-y_ref)*cos(grados))
            print(f"({y_ref}+(({x}-{x_ref})*sin({grados})))+(({y}-{y_ref})*cos({grados}))")
            if index==0:
                self.set_cord_ini(round(x_prim), round(y_prim))
            elif index==1:
                self.set_cord_fin(round(x_prim), round(y_prim))

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
        """
        if punto_ref not in aristas_rotadas:
            pass
        #si si, continua el procedimiento
        else:
        """
        #aristas_rotadas.remove(punto_ref)
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
        #nuevas_aristas.append(punto_ref)
        #ESTABLECE DICHO ARREGLO COMO LAS NUEVAS ARISTAS
        self.set_aristas(nuevas_aristas)
        print(self.get_aristas())
        return True                

    def trasladar(self,x, y):
        nuevas_aristas = []
        aristas_trasladar = self.get_aristas()
        for arista in aristas_trasladar:
            nueva_arista = [(arista[0]+x), 
                (arista[1]+y)]
            nuevas_aristas.append(nueva_arista)
        #AÑADIR EL ARREGLO COMO NUEVO CONJUNTO DE ARISTAS
        print(nuevas_aristas)
        self.set_aristas(nuevas_aristas)        
