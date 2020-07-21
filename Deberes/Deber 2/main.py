import sys, os, pygame, random
from Npuzzle import Npuzzle

def main():

    try:
        dimension = int(input('Ingrese la dimension del rompecabezas: '))
    except expression as identifier:
        print('La dimension ingresada no es un numero, programa terminado')
    
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('N puzzle')
    pantalla = pygame.display.set_mode((dimension * 167,dimension * 167))
    fpsclock = pygame.time.Clock()
    puzzle = Npuzzle((dimension,dimension), 160, 5) 

    while True:

        dt = fpsclock.tick()/1000
        pantalla.fill((0,0,0))
        puzzle.draw(pantalla)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            puzzle.eventos(evento)

        puzzle.update(dt)


if __name__ == '__main__':
    main()