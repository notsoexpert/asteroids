import pygame
from constants import *

class ScoreLabel(pygame.sprite.Sprite):
    def __init__(self, font_name, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        
        self.font = pygame.font.SysFont(font_name, size)
        self.position = (x, y)
        self.__score = 0
        self.update(0)
        
    def add_score(self, value):
        self.__score += value

    def set_text(self, new_text):
        self.__text = new_text

    def update(self, dt):
        self.set_text(f"Score: {self.__score}")
        self.text_surface = self.font.render(self.__text, True, "white")

    def draw(self, screen):
        screen.blit(self.text_surface,self.position)