import pygame
import random

class Food:
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.position = [random.randrange(1, (self.window_x//10)) * 10,
                         random.randrange(1, (self.window_y//10)) * 10]
        self.food_spawn = True
        self.spawn()

    def spawn(self):
        if self.food_spawn:
            self.position = [random.randrange(1, (self.window_x//10)) * 10,
                             random.randrange(1, (self.window_y//10)) * 10]
            self.food_spawn = False
        return self.position

    def draw(self, white):
        pygame.draw.rect(pygame.display.get_surface(), (white),
                         pygame.Rect(self.position[0], self.position[1], 10, 10))
