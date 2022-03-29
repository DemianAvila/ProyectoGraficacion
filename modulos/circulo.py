class Circulo:
    def __init__(self, radio, centro_x, centro_y,
        escala=1, traslacion=[0,0], punto_rot=None,
        grados_rot=0): 
        self.radio = radio
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.centro = [centro_x, centro_y]
        self.escala = escala
        self.traslacion = traslacion
        self.punto_rot = punto_rot
        self.grados_rot = grados_rot
    
    def get_escala(self):
        return self.escala

    def set_escala(self, n_escala):
        self.escala = n_escala

    def get_traslacion(self):
        return self.traslacion

    def set_traslacion(self, n_traslacion):
        self.traslacion = n_traslacion

    def get_punto_rot(self):
        return self.punto_rot

    def set_punto_rot(self, n_punto_rot):
        self.punto_rot = n_punto_rot

    def get_grados_rot(self):
        return self.grados_rot

    def set_grados_rot(self, n_grados_rot):
        self.grados_rot = n_grados_rot

    def get_radio(self):
        return self.radio
    
    def get_centro_x(self):
        return self.centro_x
    
    def get_centro_y(self):
        return self.centro_y
    
    def get_centro(self):
        return self.centro

    def set_radio(self, n_radio):
        self.radio = n_radio
    
    def set_centro_x(self, x):
        self.centro_x = x
        self.centro = [x, self.get_centro_y()]

    def set_centro_y(self, y):
        self.centro_y = y
        self.centro= [self.get_centro_x(), y]
    
    def set_centro(self, x, y):
        self.set_centro_x(x)
        self.set_centro_y(y)

    #APLICAR ALGORITMO DE PTO MEDIO
    def puntos_circulo(self):
        #INICIALIZACI�N DE LAS VARIABLES, EN ESTE CASO, EL RADIO
        radio = self.get_radio()
       
        #VALOR INICIAL DEL PARAMETRO DE DECISION
        p0 = 1-radio
        #COORDENADAS INICIALES
        x = 1
        y = radio
        #VECTOR 2D QUE ALMACENA LOS VALORES DE X Y Y
        coordenadas = []
        #CONTADOR DE INSERCI�N DE VECTORES
        cont = 0
        #ALMACENA LAS COORDENADAS
        coordenada = []
        #MIENTRAS X SEA MENOR QUE Y
        while x<=y:
            #A�ADE LAS COORDENADAS AL VECTOR
            coordenada = [x, y]
            coordenadas.append(coordenada)
            cont+=1
            #VERIFFICA EL PARAMETRO DE DECISI�N
            if p0<0:
                x+=1
                p0 = p0+(2*x)+1
            
            else:
                x+=1
                y-=1
                p0 = p0+(2*x)+1-(2*y)
            

        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #INVIERTE LOS VALORES Y,X -> X,Y
        #OMITE EL ULTIMO
        #2
        tamanio = len(coordenadas)
        for i in range(tamanio-1):
            coordenada = [coordenadas[i][1], coordenadas[i][0]]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #INVIERTE LOS VALORES Y,X -> X,Y
        #NO OMITE EL ULTIMO
        #Y NEGATIVO
        #3
        for i in range(tamanio):
            coordenada = [coordenadas[i][1], (coordenadas[i][0])*-1]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #NO INVERTIR LOS VALORES Y,X
        #OMITE EL ULTIMO
        #X NEGATIVO
        #4
        for i in range (tamanio-1):
            coordenada = [coordenadas[i][0], (coordenadas[i][1])*-1]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #NO INVERTIR LOS VALORES Y,X
        #NO OMITE EL ULTIMO
        #X NEGATIVO Y NEGATIVO
        #5
        for i in range (tamanio):
            coordenada = [(coordenadas[i][0])*-1, (coordenadas[i][1])*-1]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #INVIERTE LOS VALORES Y,X -> X,Y
        #OMITE EL ULTIMO
        #Y NEGATIVO, X NEGATIVO
        #6
        for i in range (tamanio-1):
            coordenada = [(coordenadas[i][1])*-1, (coordenadas[i][0])*-1]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #INVIERTE LOS VALORES Y,X -> X,Y
        #NO OMITE EL ULTIMO
        #X NEGATIVO
        #7
        for i in range(tamanio):
            coordenada = [(coordenadas[i][1])*-1, (coordenadas[i][0])]
            coordenadas.append(coordenada)
            cont+=1
        
        #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1
        #NO INVERTIR LOS VALORES Y,X
        #OMITE EL ULTIMO
        #Y NEGATIVO
        #8
        for i in range(tamanio-1):
            coordenada = [(coordenadas[i][0])*-1, (coordenadas[i][1])]
            coordenadas.append(coordenada)
            cont+=1
    
        return coordenadas
    
