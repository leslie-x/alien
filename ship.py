import pygame

class Ship:
    """manage the ship"""
    
    def __init__(self,ai_game):
        #init location
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load ship.bmp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #locate ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #MOVE FLAG
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        """move location according to move flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        
        
    def blitme(self):
        #paint ship at fixed place
        self.screen.blit(self.image,self.rect)