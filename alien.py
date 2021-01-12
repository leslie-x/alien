import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """represent an alien"""
    
    def __init__(self,ai_game):
        """init alien"""
        super().__init__()
        self.screen = ai_game.screen
        
        #load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #init location top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store float
        self.x = float(self.rect.x)
        