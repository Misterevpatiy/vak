import pygame


class Character:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.side = 50
        self.direction_x = 1
        self.direction_y = 1
        self.speed = 1

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.side, self.side))

    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y
        if self.y == 0:
            self.direction_y = 1
        if self.y == 550:
            self.direction_y = -1
        if self.x == 750:
            self.direction_x = -1
        if self.x == 0:
            self.direction_x = 1


