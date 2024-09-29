import pygame
pygame.init()
running = True

#Title
pygame.display.set_caption("Deer Crackers! said Nokotan - (Ta) Katanyoo Katavethin")

#Screen size
screen = pygame.display.set_mode((1366,768))



#Setup
background = pygame.image.load("Graphics/Deer Club.png")



deerCracker = pygame.image.load("Graphics/Deer cracker 1.png")

crackerSize = 0.3
deerCrackerSize = pygame.transform.scale_by(deerCracker, crackerSize)

deerCracker_location = deerCracker.get_rect()
deerCracker_location.center = (0,0)

pygame.display.update()





#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouseX, mouseY = pygame.mouse.get_pos()
           deerCracker_location.center = ((mouseX + 120) , (mouseY + 129))
        
        
    deerCracker_location.y = deerCracker_location.y + 5
    if deerCracker_location.y > 670:
     deerCracker_location.y = deerCracker_location.y - 5

            



    screen.blit(background, (0,0))
    screen.blit(deerCrackerSize, deerCracker_location)
    
        
    #All the agents
    #Agent5.moveToTarget()
    #Agent5.update()
    #Agent5.render()

    pygame.display.flip()
pygame.quit()  