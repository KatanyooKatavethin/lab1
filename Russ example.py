import pygame

pygame.init()

pygame.display.set_caption("Sprite Groups")

#create game window
screen = pygame.display.set_mode((1366, 768))

background = pygame.image.load("Graphics/Deer Club.png")
#frame rate
clock = pygame.time.Clock()
FPS = 60


#create class for squares
class deerCrackerClass(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Graphics/Deer cracker 1.png")
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def update(self):
    self.rect.y = self.rect.y + 5
    if self.rect.y > 670:
      self.rect.y = self.rect.y - 5

#create sprite group 
crackers = pygame.sprite.Group()

#create cracker1 and add to crackers group
cracker1 = deerCrackerClass( 0,0)
crackers.add(cracker1)

#game loop
run = True
while run:

  
  clock.tick(FPS)

  screen.blit(background, (0,0))

  #update sprite group
  crackers.update()

  #draw sprite group
  crackers.draw(screen)

  print(crackers)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      #get mouse coordinates
      pos = pygame.mouse.get_pos()
      #create square
      cracker1 = deerCrackerClass( pos[0], pos[1])
      crackers.add(cracker1)
    #quit program
    if event.type == pygame.QUIT:
      run = False


  
  #update display
  pygame.display.flip()

pygame.quit()