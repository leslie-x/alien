import pygame

class Ship:
    """manage the ship"""
    
    def __init__(self,ai_game):
        #init location
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #load ship.bmp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #locate ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #let x be float because speed step is a float
        #since rect.x is an int not a float so instead by .x
        self.x = float(self.rect.x)
        
        #MOVE FLAG
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        """move location according to move flag"""
        #refresh the ship's x by ship_speed 
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        #rect.x restores .x's int like 1.5+1.5=3 rect.x=3
        self.rect.x = self.x
        
        
    def blitme(self):
        #paint ship at fixed place
        self.screen.blit(self.image,self.rect)