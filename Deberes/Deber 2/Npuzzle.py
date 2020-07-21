import sys, os, pygame, random
import easygui as eg

class Npuzzle:
    def __init__(self,tamanio_grilla, tamanio_pieza, tamanio_margen):
        self.tamanio_grilla,self.tamanio_pieza,self.tamanio_margen = tamanio_grilla, tamanio_pieza, tamanio_margen

        self.numero_piezas = tamanio_grilla[0] * tamanio_grilla[1]
        self.piezas = [(x,y) for y in range(tamanio_grilla[1]) for x in range(tamanio_grilla[0])]
        self.posicion_correcta_piezas = [(x,y) for y in range(tamanio_grilla[1]) for x in range(tamanio_grilla[0])]
        self.posicion_piezas = {(x,y):(x*(tamanio_pieza + tamanio_margen)+tamanio_margen,y*(tamanio_pieza+tamanio_margen)+tamanio_margen) for y in range(tamanio_grilla[1]) for x in range(tamanio_grilla[0])}
        self.rectangulo = pygame.Rect(0,0,tamanio_grilla[0]*(tamanio_pieza+tamanio_margen)+tamanio_margen,tamanio_grilla[1]*(tamanio_pieza+tamanio_margen)+tamanio_margen) 

        mapache = pygame.transform.smoothscale(pygame.image.load('./mapache.jpg'),self.rectangulo.size)
        
        self.fuente = pygame.font.Font(None,90)
        self.imagenes = []
        self.previa = None

        self.pieza_random = random.randrange(self.numero_piezas - 1)

        for i in range(self.numero_piezas):
            if i != self.pieza_random:
                x,y = self.posicion_piezas[self.piezas[i]]
                imagen = mapache.subsurface(x,y,tamanio_pieza,tamanio_pieza)
                texto = self.fuente.render(str(i+1),2,(200,0,0))
                w,h = texto.get_size()
                imagen.blit(texto,(int((tamanio_pieza-w)/2),int((tamanio_pieza-h)/2)))
                self.imagenes+=[imagen]
            elif self.pieza_random != self.numero_piezas:
                x,y = self.posicion_piezas[self.piezas[i]]
                imagen = mapache.subsurface(x,y,tamanio_pieza,tamanio_pieza)
                imagen.fill((0,0,0))
                self.imagenes+=[imagen]

        for i in range(20):
            self.randomizar()


    def get_pieza_libre(self): return self.piezas[self.pieza_random] 

    def set_pieza_libre(self, posicion): self.piezas[self.pieza_random] = posicion
    
    pieza_libre = property(get_pieza_libre,set_pieza_libre)

    def switch(self, pieza): self.piezas[self.piezas.index(pieza)],self.pieza_libre, self.previa = self.pieza_libre, pieza, self.pieza_libre

    def randomizar(self): 
        adj = self.adjacente()
        self.switch(random.choice([pos for pos in adj if self.en_grilla(pos) and pos!=self.previa]))

    def en_grilla(self,pieza): return pieza[0]>=0 and pieza[0]<=self.tamanio_grilla[0] - 1 and pieza[1]>=0 and pieza[1]<=self.tamanio_grilla[1] - 1

    def adjacente(self): 
        x,y = self.pieza_libre
        return (x-1,y),(x+1,y),(x,y-1),(x,y+1)

    def update(self,dt):
        
        mouse = pygame.mouse.get_pressed()
        posicion_mouse = pygame.mouse.get_pos()

        if mouse[0]:

            x,y = posicion_mouse[0]%(self.tamanio_pieza+self.tamanio_margen), posicion_mouse[1]%(self.tamanio_pieza+self.tamanio_margen)
            if x > self.tamanio_margen and y > self.tamanio_margen:
                pieza = posicion_mouse[0]//self.tamanio_pieza,posicion_mouse[1]//self.tamanio_pieza
                if self.en_grilla(pieza): 
                    if pieza in self.adjacente(): self.switch(pieza)
                    if self.posicion_correcta_piezas == self.piezas:
                        eg.msgbox(msg='Felicidades ha ganado', title='Ganador', ok_button='Continuar')

        

    def draw(self,pantalla):
        for i in range(self.numero_piezas):
            x,y = self.posicion_piezas[self.piezas[i]]
            pantalla.blit(self.imagenes[i],(x,y))

    def eventos(self,evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                for i in range(100): self.randomizar() 