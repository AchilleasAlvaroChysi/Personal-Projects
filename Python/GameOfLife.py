import pygame, sys, math, time, numpy, math
from random import randint


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GRAY =  (100,100,100)

width = 500
height = 500
N = 10
cellSize = int(width/N)

cell = numpy.zeros((cellSize,cellSize), dtype = numpy.int)
secCell = numpy.zeros((cellSize,cellSize), dtype = numpy.int)
for x in range (0,width,N):
    for y in range (0,height,N):
        cell[int(x/N)][int(y/N)]= randint(0,1)
        
def findNeighbors(cell, x, y):
    temp = numpy.copy(cell)
    if 0 < x < len(temp) - 1:
        xi = (0, -1, 1)
    elif x > 0:
        xi = (0, -1)
    else:
        xi = (0, 1)

    if 0 < y < len(temp[0]) - 1:
        yi = (0, -1, 1)
    elif y > 0:
        yi = (0, -1)
    else:
        yi = (0, 1)

    for a in xi:
        for b in yi:
            if a == b == 0:
                continue
            yield temp[x + a][y + b]

def updateCell(cell, x, y):
    temp = numpy.copy(cell)
    neighbors = findNeighbors(temp, x, y)
    alive = 0
    for i in neighbors:
        if i == 1:
            alive+=1

    #if current cell is alive
    if temp[x][y] == 1:
        #kill if less than 2 or more than 3 alive neighbors
        if (alive < 2) or (alive > 3):
            return 0
        else:
            return 1
    #if current cell is dead
    elif temp[x][y] == 0:
        #make alive if 3 alive neighbors
        if alive == 3:
            return 1
        else:
            return 0
    


pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("El Game-o Of Life-o")

def clear():
    screen.fill(WHITE)

done = False;
clock = pygame.time.Clock()

while not done:
    clock.tick(30)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    clear()
    for x in range(0,cellSize):
        for y in range(0,cellSize):
            secCell[x][y] = updateCell(cell,x,y)

    cell = numpy.copy(secCell)
    for x in range (0, cellSize,1):
        for y in range (0,cellSize,1):
            if cell[x][y] == 1:
                pygame.draw.rect(screen, BLACK, [x*N,y*N,width,height])
            else:
                pygame.draw.rect(screen, GRAY, [x*N,y*N,width,height])

    pygame.display.flip()
    
pygame.quit()
