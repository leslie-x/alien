import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manage the bullet"""
    
    def __init__(self,ai_game):
        """creat a bullet where the ship located"""
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #creat a rect(a bullet) at (0,0),then move it to the ship mid
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #use float so that u can change the value by a little
        self.y = float(self.rect.y)
        
#-------------------------------------------------------------------------------
    
    def update(self):
        """move bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """draw a bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        