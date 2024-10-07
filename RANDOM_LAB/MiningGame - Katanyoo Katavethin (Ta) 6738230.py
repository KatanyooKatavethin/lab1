import pygame
import random
from utility import MarbleBag
from utility import FixedLimit


pygame.init()
running = True

#Title
pygame.display.set_caption("Mining Game - (Ta) Katanyoo Katavethin")

#Screen size
screen = pygame.display.set_mode((900,700))

screen.fill((0, 0, 0))
pygame.display.update()


#Dirt BLock
dirtBlock = pygame.image.load("Mining Graphics/Dirt.png")
dirtBlockBroken = pygame.image.load("Mining Graphics/Dirt break.png")

#Gold
gold = pygame.image.load("Mining Graphics/Gold.png")
goldSize = 0.7
goldSizeChanged = pygame.transform.scale_by(gold, goldSize)

#Silver
silver = pygame.image.load("Mining Graphics/Silver.png")

#Diamond
diamond = pygame.image.load("Mining Graphics/Diamond.png")


mineralsWithNoMinerals = [1,2,3,4,5,6,7,8,9,10]
minerals = MarbleBag (mineralsWithNoMinerals)

dirtBlockBreaks = [0, 1]
block = MarbleBag (dirtBlockBreaks)

#Game loop
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
             block.draw()
             if block.draw() == 0:
                 screen.fill((0, 0, 0))
                 screen.blit(dirtBlock, (300, 200))
             else:
                 screen.fill((0, 0, 0))
                 screen.blit(dirtBlockBroken, (300, 200))
                 minerals.draw()    
                 if minerals.draw() == 1:
                      screen.fill((0, 0, 0))
                      screen.blit(goldSizeChanged, (324, 200)) 

                 if minerals.draw() == 2:   
                      screen.fill((0, 0, 0)) 
                      screen.blit(silver, (345, 200))

                 if minerals.draw() == 3:   
                      screen.fill((0, 0, 0)) 
                      screen.blit(diamond, (365, 200))

    pygame.display.flip()
pygame.quit()  