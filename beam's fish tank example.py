import pygame
import random
import pygame_gui

WIDTH = 1280
HEIGH = 720
MAX_SPEED = 5

SEPARATION_FACTOR = 0.1
ALIGNMENT_FACTOR = 0.1
COHERENCE_FACTOR = 0.01
SEPARATION_DIST = 70

NUMBER_AGENT = 20
NUMBER_OBSTACLE = 5

MAX_HUNGRY = 100
FOOD_COOLDOWN = 150

class Agent:
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-MAX_SPEED, MAX_SPEED), random.uniform(-MAX_SPEED, MAX_SPEED))
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1

        self.sign_range = 30
        self.sign_food = 20

        self.hungry_value = 100
        self.hungry_timer = 0

        self.frame_size = 64
        self.fx = 0
        self.fy = 0
        self.agent_frame = agent_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.time = 0
        self.frame_rate = 5
    
    def animation(self):
        if self.time >  self.frame_rate:
            self.fx = self.fx + 1
            self.fx = self.fx % 4
            self.agent_frame = agent_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                   self.frame_size, self.frame_size))
            self.time = 0
        else:
            self.time = self.time + 1

    def apply_force(self, x, y):
        force = pygame.Vector2(x, y)
        self.acceleration += force / self.mass

    def seeking(self, foods):
        for food in foods:
            vec_target = food.position
            distance = vec_target - self.position
            dist = distance.magnitude()

            if dist <= self.sign_food:
                foods.remove(food)
                self.hungry_value += 5
                if self.hungry_value > 100:
                    self.hungry_value = MAX_HUNGRY
            
            elif dist <= self.sign_range * 5:
                energy = dist / self.sign_range * 5
                max_speed = 1
                speed = energy * max_speed
                distance.normalize() * speed
                seeking_force = distance
                self.apply_force(seeking_force.x, seeking_force.y)
    
    def fleeObstacle(self, obstacles):
        for obstacle in obstacles:
            vec_target = obstacle.position
            distance = vec_target - self.position
            dist = distance.magnitude()

            if dist <= self.sign_range * 3:
                energy = 1 - (dist / self.sign_range * 3)
                max_speed = 1
                speed = energy * max_speed
                distance.normalize() * speed
                flee_force = distance
                self.apply_force(-flee_force.x, -flee_force.y)
    
    def coherence(self, agents):
        center_of_mass = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for agent in agents:
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < 100:
                    center_of_mass += agent.position
                    agent_in_range_count += 1

        if agent_in_range_count > 0:
            center_of_mass /= agent_in_range_count
            d = center_of_mass - self.position
            f = d * COHERENCE_FACTOR  
            self.apply_force(f.x, f.y)

    def separation(self, agents):
        d = pygame.Vector2(0, 0)
        for agent in agents:
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < SEPARATION_DIST:
                    d += self.position - agent.position

        separation_force = d * SEPARATION_FACTOR
        self.apply_force(separation_force.x, separation_force.y)
    
    def alignment(self, agents):
        v = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for agent in agents:
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < 100:
                    v += agent.velocity
                    agent_in_range_count += 1

        if agent_in_range_count > 0:
            v /= agent_in_range_count
            alignment_force = v * ALIGNMENT_FACTOR
            self.apply_force(alignment_force.x, alignment_force.y)
    
    def hungry(self):
        self.hungry_timer += 1
        if self.hungry_timer >= 20:
            self.hungry_value -= 1
            self.hungry_timer = 0

    def update(self):
        self.animation()
        self.hungry()

        self.velocity += self.acceleration
        if self.velocity.length() > 1:
            self.velocity = self.velocity.normalize() * 1
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)
    
    def render(self):
        screen.blit(self.agent_frame, self.position - pygame.Vector2(32, 32))

        if self.hungry_value < 30:
            hungry_text = font.render(f'Hungry: {self.hungry_value}', True, "red")
        elif self.hungry_value < 50:
            hungry_text = font.render(f'Hungry: {self.hungry_value}', True, "orange")
        elif self.hungry_value >= 50:
            hungry_text = font.render(f'Hungry: {self.hungry_value}', True, "white")
        screen.blit(hungry_text, (self.position.x - 25, self.position.y - 50))

class Obstacle:
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)

        self.frame_size = 64
        self.fx = 0
        self.fy = 0
        self.obstacle_frame = obstacle_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.time = 0
        self.frame_rate = 2
    
    def animation(self):
        if self.time >  self.frame_rate:
            self.fx = self.fx + 1
            self.fx = self.fx % 4
            self.obstacle_frame = obstacle_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                   self.frame_size, self.frame_size))
            self.time = 0
        else:
            self.time = self.time + 1
        
    def update(self):
        self.animation()
    
    def render(self):
        self.obstacle_frame = pygame.transform.scale(self.obstacle_frame, (100, 100))
        screen.blit(self.obstacle_frame, self.position  - pygame.Vector2(50, 50))

class Food:
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0.1)

        self.frame_size = 16
        self.fx = 0
        self.fy = 0
        self.food_frame = food_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.time = 0
        self.frame_rate = 30
    
    def animation(self):
        if self.time >  self.frame_rate:
            self.fx = self.fx + 1
            self.fx = self.fx % 3
            self.food_frame = food_sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
            self.time = 0
        else:
            self.time = self.time + 1

    def drop(self, vec_target):
        distance = vec_target - self.position
        distance.normalize() * 0.1
        self.velocity += distance

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.animation()
    
    def render(self):
        screen.blit(self.food_frame, self.position  - pygame.Vector2(8, 8))

agent_sprite = pygame.image.load("Sprite2D/FishTank/SpriteFish.png")
agents = [Agent(random.uniform(0, WIDTH), random.uniform(0, HEIGH))
          for _ in range(NUMBER_AGENT)]

obstacle_sprite = pygame.image.load("Sprite2D/FishTank/SpriteBlackHole.png")
obstacles = [Obstacle(random.uniform(100, WIDTH-100), random.uniform(100, HEIGH-100))
          for _ in range(NUMBER_OBSTACLE)]

food_sprite = pygame.image.load("Sprite2D/FishTank/SpriteFood.png")
foods = []
cooldown_spawnTime = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGH)) # GUI
font = pygame.font.SysFont("Arial", 12) # font
running = True

## ------- Game Loop ------------
while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if pygame.mouse.get_pressed()[0]:
            if current_time - cooldown_spawnTime > FOOD_COOLDOWN:
                food = Food(mousePosition[0], mousePosition[1])
                foods.append(food)
                cooldown_spawnTime = current_time

    screen.fill("skyblue4")

    mousePosition = pygame.mouse.get_pos()
    pygame.draw.circle(screen, "aqua", mousePosition, 5, 2)

    for agent in agents:
        agent.fleeObstacle(obstacles)
        agent.seeking(foods)
        agent.coherence(agents)
        agent.separation(agents)
        agent.alignment(agents)
        agent.update()
        agent.render()

        if agent.hungry_value <= 0:
            agents.remove(agent)

        if agent.position.x > WIDTH:
            agent.position.x = 0
        elif agent.position.x < 0:
            agent.position.x = WIDTH
        if agent.position.y > HEIGH:
            agent.position.y = 0
        elif agent.position.y < 0:
            agent.position.y = HEIGH
    
    for obstacle in obstacles:
        obstacle.update()
        obstacle.render()
    
    for food in foods:
        food.update()
        food.render()
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()