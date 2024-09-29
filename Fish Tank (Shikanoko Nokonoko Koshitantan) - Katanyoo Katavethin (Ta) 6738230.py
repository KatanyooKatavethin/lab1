import pygame
import random
pygame.init()
running = True

#Title
pygame.display.set_caption("Deer Crackers! said Nokotan - (Ta) Katanyoo Katavethin")

#Screen size
screen = pygame.display.set_mode((1366,768))


# ----------------------- Setup --------------------------------------

#Background
background = pygame.image.load("Graphics/Deer Club.png")

#Deer crackers
deerCracker = pygame.image.load("Graphics/Deer cracker 1.png")
crackerSize = 0.3
deerCrackerSizeChanged = pygame.transform.scale_by(deerCracker, crackerSize)

#Nokotan
nokotan = pygame.image.load("Graphics/Nokotan.png")
nokotanSize = 1
nokotanSizeChanged = pygame.transform.scale_by(nokotan, nokotanSize)


#Water bottles
bottle = pygame.image.load("Graphics/Bottle.png")
bottleSize = 0.30
bottleSizeChanged = pygame.transform.scale_by(bottle, bottleSize)


MAX_SPEED = 3
NUMBER_AGENT = 10  

COHERENCE_FACTOR = 0.009 
ALIGNMENT_FACTOR = 0.1  
SEPARATION_FACTOR = 0.09  
SEPARATION_DIST = 72  


#Deer cracker's class
class DeerCrackerClass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = deerCrackerSizeChanged
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.position = self.rect.center

    def update(self):
      self.rect.y = self.rect.y + 5
      if self.rect.y > 670:
         self.rect.y = self.rect.y - 5



#Nokotan's class
class NokotanClass:
    def __init__(self, x, y)-> None:
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-MAX_SPEED, MAX_SPEED), random.uniform(-MAX_SPEED, MAX_SPEED))
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1  
        self.range = 10
      

    def updateAnimation(self):
        
         self.agent_frame = nokotanSizeChanged
       

    def updateMovement(self):
        
        # Update velocity and position of the agent based on current acceleration
        self.velocity = self.velocity + self.acceleration
        if self.velocity.length() > MAX_SPEED:
            # Limit the speed to MAX_SPEED
            self.velocity = self.velocity.normalize() * MAX_SPEED
        self.position = self.position + self.velocity
        # Reset acceleration after each update
        self.acceleration = pygame.Vector2(0, 0)

    def updateEverything(self):
        self.updateAnimation()
        self.updateMovement()


    def apply_force(self, x, y):
        # Apply a force to the agent, adjusting acceleration based on mass
        force = pygame.Vector2(x, y)
        self.acceleration = self.acceleration + (force / self.mass)

    def seek(self, cracker):
     
     betweenVec = cracker.position - self.position
     betweenVec.normalize() * 0.1
     distance = betweenVec.magnitude()

     if distance <= self.range:
      #max_speed = 0.5
     # energy = distance / self.range
      #speed = energy * max_speed
      #betweenVec.normalize() * speed
     # self.apply_force(betweenVec.x, betweenVec.y)
     
      self.acceleration = self.acceleration + betweenVec
     


    def bottleFlee(self, bottle):
     betweenVec = bottle.position - self.position
     betweenVec.normalize() * - 0.1
     distance = betweenVec.magnitude()

     if distance <= self.range:
      #max_speed = 0.5
     # energy = distance / self.range
      #speed = energy * max_speed
      #betweenVec.normalize() * speed
     # self.apply_force(betweenVec.x, betweenVec.y)
      self.acceleration = self.acceleration + betweenVec


    def coherence(self, nokotans):
        
        center_of_mass = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for each_nokotan in nokotans:
            if each_nokotan != self:
                distance = self.position.distance_to(each_nokotan.position)
                if distance < 100:  
                    center_of_mass = center_of_mass + each_nokotan.position
                    agent_in_range_count = agent_in_range_count + 1

        if agent_in_range_count > 0:
            center_of_mass /= agent_in_range_count  
            d = center_of_mass - self.position
            f = d * COHERENCE_FACTOR  
            self.apply_force(f.x, f.y)  

    def separation(self, nokotans):
        
        desiredPath = pygame.Vector2(0, 0)
        for each_nokotan in nokotans:
            if each_nokotan != self:
                distance = self.position.distance_to(each_nokotan.position)
                if distance < SEPARATION_DIST:  
                    desiredPath = desiredPath + self.position - each_nokotan.position

        separation_force = desiredPath * SEPARATION_FACTOR  
        
        self.apply_force(separation_force.x, separation_force.y)

    def alignment(self, nokotans):
        
        v = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for each_nokotan in nokotans:
            if each_nokotan != self:
                distance = self.position.distance_to(each_nokotan.position)
                if distance < 100:  
                    v = v + each_nokotan.velocity
                    agent_in_range_count = agent_in_range_count + 1

        if agent_in_range_count > 0:
            v = v / agent_in_range_count  
            alignment_force = v * ALIGNMENT_FACTOR  
            self.apply_force(alignment_force.x, alignment_force.y)


    def draw(self, screen):
     screen.blit(self.agent_frame, self.position - pygame.Vector2(32, 32))



#Bottles class
class Bottle():
    def __init__(self, x, y):
     self.location = bottleSizeChanged.get_rect()
     self.location.center = (x, y)
     self.position = self.location.center

    def drawBottle(self, screen):
     screen.blit (bottleSizeChanged, self.location)




allCrackers = DeerCrackerClass(-200, -200)
crackers = pygame.sprite.Group()
#crackers.add(allCrackers)

nokotans = [NokotanClass(random.uniform(0, 1366), random.uniform(0, 768))
          for _ in range(NUMBER_AGENT)]


bottle1 = Bottle(240, 640)
bottle2 = Bottle(780, 634)
bottle3 = Bottle(1100, 625)
bottle4 = Bottle(1200, 650)

#Game loop
while running:

    screen.blit(background, (0,0))
    bottle1.drawBottle(screen)
    bottle2.drawBottle(screen)
    bottle3.drawBottle(screen)
    bottle4.drawBottle(screen)
    crackers.update()
    crackers.draw(screen)
    crackers.add(allCrackers)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouseX, mouseY = pygame.mouse.get_pos()
           allCrackers = DeerCrackerClass(mouseX, mouseY)
           
 
    for each_Nokotan in nokotans:
        
        each_Nokotan.coherence(nokotans)  
        each_Nokotan.separation(nokotans)  
        each_Nokotan.alignment(nokotans)  
        each_Nokotan.updateEverything()  
        each_Nokotan.draw(screen)  
        each_Nokotan.seek(allCrackers)
        each_Nokotan.bottleFlee(bottle1)

    for each_Nokotan in nokotans:
        if each_Nokotan.position.x > 1388:
            each_Nokotan.position.x = 0
        elif each_Nokotan.position.x < 0:
            each_Nokotan.position.x = 1388
        if each_Nokotan.position.y > 768:
            each_Nokotan.position.y = 0
        elif each_Nokotan.position.y < 0:
            each_Nokotan.position.y = 768

    pygame.display.flip()
pygame.quit()  