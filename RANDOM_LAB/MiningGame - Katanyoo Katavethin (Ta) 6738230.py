import pygame
import random
from utility import MarbleBag
from utility import FixedLimit
import time

pygame.init()
running = True

#Title
pygame.display.set_caption("Mining Game - (Ta) Katanyoo Katavethin")


#Time
clock = pygame.time.Clock()
countdown_Seconds = 1
countDown = False

countdown_SecondsMin = 1
countDownMin = False

countdown_SecondsMinGold = 2
countDownMinGold = False

countdown_SecondMinSilver = 2
countDownMinSilver = False

countdown_SecondMinDiamond = 2
countDownMinDiamond = False

#Screen size
screen = pygame.display.set_mode((900, 700))
pygame.display.update()

#Dirt BLock
dirtBlock = pygame.image.load("Mining Graphics/Dirt.png")
dirtBlock_Loc = dirtBlock.get_rect()
dirtBlock_Loc.center = (300, 200)
dirtBlockBroken = pygame.image.load("Mining Graphics/Dirt break.png")

#Gold
gold = pygame.image.load("Mining Graphics/Gold.png")
goldSize = 0.5
goldSizeChanged = pygame.transform.scale_by(gold, goldSize)

#Silver
silver = pygame.image.load("Mining Graphics/Silver.png")

#Diamond
diamond = pygame.image.load("Mining Graphics/Diamond.png")

#Low res Jack Black  
jB = pygame.image.load("Mining Graphics/Low res Jack Black.png")
nM = pygame.image.load("Mining Graphics/No Minerals.png")
jBG = pygame.image.load("Mining Graphics/JB Gold.png")
jBS = pygame.image.load("Mining Graphics/JB Silver.png")
jBD = pygame.image.load("Mining Graphics/JB Diamond.png")

#Background
bG = pygame.image.load("Mining Graphics/Background.png")

mineralsWithNoMinerals = [1,2,3,4,5,6,7,8,9,10]
minerals = MarbleBag (mineralsWithNoMinerals)

dirtBlockBreaks = [0, 1]
block = MarbleBag (dirtBlockBreaks)

#howManyTimes = [10, 4]
#fixed_Limit = FixedLimit (howManyTimes)

#Game loop
while running:
    
    screen.blit(bG)
    screen.blit(dirtBlock, (300, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
             block.draw()
             if block.draw() == 0:
                 countDown = True
                 startHere = pygame.time.get_ticks()
             else:
                 minerals.draw()    
                 if minerals.draw() == 1:
                     countDownMinGold = True
                     startHereMin = pygame.time.get_ticks() 

                 elif minerals.draw() == 2:   
                     countDownMinSilver = True
                     startHereMin = pygame.time.get_ticks() 

                 elif minerals.draw() == 3:   
                     countDownMinDiamond = True
                     startHereMin = pygame.time.get_ticks() 

                 else: 
                     countDownMin = True
                     startHereMin = pygame.time.get_ticks()  
                 
    if countDown:
        milli_To_Seconds = (pygame.time.get_ticks() - startHere) / 1000
        countingDown = countdown_Seconds - milli_To_Seconds

        if countingDown > 0:
            screen.blit(jB)


    if countDownMin:
        milli_To_SecondsMin = (pygame.time.get_ticks() - startHereMin) / 1000
        countingDownMin = countdown_SecondsMin - milli_To_SecondsMin

        if countingDownMin > 0:
            screen.blit(bG)
            screen.blit(dirtBlockBroken, (300, 200))
            screen.blit(nM)


    if countDownMinGold:
        milli_To_SecondsMin = (pygame.time.get_ticks() - startHereMin) / 1000
        countingDownMinGold = countdown_SecondsMinGold - milli_To_SecondsMin

        if countingDownMinGold > 0:
            screen.blit(bG)
            screen.blit(dirtBlockBroken, (300, 200))
            screen.blit(goldSizeChanged, (350, 200))
            screen.blit(jBG)


    if countDownMinSilver:
        milli_To_SecondsMin = (pygame.time.get_ticks() - startHereMin) / 1000
        countingDownMinSilver = countdown_SecondMinSilver - milli_To_SecondsMin

        if countingDownMinSilver > 0:
            screen.blit(bG)
            screen.blit(dirtBlockBroken, (300, 200))
            screen.blit(silver, (350, 200))
            screen.blit(jBS)        


    if countDownMinDiamond:
        milli_To_SecondsMin = (pygame.time.get_ticks() - startHereMin) / 1000
        countingDownMinDiamond = countdown_SecondMinDiamond - milli_To_SecondsMin

        if countingDownMinDiamond > 0:
            screen.blit(bG)
            screen.blit(dirtBlockBroken, (300, 200))
            screen.blit(diamond, (365, 200))
            screen.blit(jBD)   
    


    pygame.display.flip()
    clock.tick(60)
pygame.quit()  