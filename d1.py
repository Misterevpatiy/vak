
import pygame
from Character import Character

screen = pygame.display.set_mode((800, 600))
character = Character()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    character.move()
    character.display(screen)
    pygame.display.flip()
