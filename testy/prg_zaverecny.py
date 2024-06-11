import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("ahoj")
    color = (255, 255, 255)
    screen.fill(color)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()