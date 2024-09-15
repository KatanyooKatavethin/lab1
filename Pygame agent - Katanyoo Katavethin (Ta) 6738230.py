import pygame
pygame.init()
running = True

#Title
pygame.display.set_caption("Pygame Agent - (Ta) Katanyoo Katavethin")

#Screen size
screen = pygame.display.set_mode((900,700))

screen.fill((0, 0, 0))
pygame.display.update()

#Set max speed here
maxSpeed = 0.1

#Agent's class
class Agent:
    def __init__(self, x, y):
     self.position = pygame.math.Vector2(x, y)
     self.velocity = pygame.math.Vector2(0, 0)
     self.acceleration = pygame.math.Vector2(0, 0)

    def moveToTarget(self):
     #Find the vector between the target(& mouse)'s position and the Agent's position
     betweenVec = (pygame.mouse.get_pos() - self.position)

     #Normalize it (Magnitude becomes 1) and multiply by any number
     betweenVec.normalize() * maxSpeed

     #Add to acceleration
     self.acceleration = self.acceleration + betweenVec
     

    def update(self):
     #Add to velocity
     self.velocity = self.velocity + self.acceleration
     
     #Multiply velocity by 2
     self.velocity = self.velocity * 2

     #Set the length/magnitude of the velocity vector
     self.velocity.scale_to_length(maxSpeed)
   
     #Make the agent move    
     self.position = self.position + self.velocity
        
     #Stop the agent at the target
     self.acceleration = self.acceleration - self.acceleration


    def render(self):
           pygame.draw.circle(screen, (237, 60, 63), (self.position), 23)
           

#The 5 Agents
Agent1 = Agent(300, 405)
Agent2 = Agent(340, 220)
Agent3 = Agent(150, 223)
Agent4 = Agent(200, 196)
Agent5 = Agent(555, 682)

#Game loop
while running:
    screen.fill((0, 0, 0))
    
    #The target
    mouseX, mouseY = pygame.mouse.get_pos()
    target = pygame.draw.circle(screen, (255, 192, 203), (mouseX, mouseY), 45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
    #All the agents
    Agent1.moveToTarget()
    Agent1.update()
    Agent1.render()

    Agent2.moveToTarget()
    Agent2.update()
    Agent2.render()

    Agent3.moveToTarget()
    Agent3.update()
    Agent3.render()

    Agent4.moveToTarget()
    Agent4.update()
    Agent4.render()

    Agent5.moveToTarget()
    Agent5.update()
    Agent5.render()

    pygame.display.flip()
pygame.quit()  