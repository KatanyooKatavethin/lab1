import pygame
# Your game setup would go here
gameScreen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Mouse Click - Test Game')
rectangle_color = (255,0,0) # Red color
rectangle_position = (400, 300) # Centre of screen
rectangle_dimension = (100, 100) # Width and Height
rectangle = pygame.Rect(rectangle_position, rectangle_dimension)
running = True
while running:
    pygame.draw.rect(gameScreen, rectangle_color, rectangle)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos() # Get click position
            if rectangle.collidepoint(x, y): # Check if click is within rectangle
                print("Rectangle clicked!")
pygame.quit()