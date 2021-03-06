import sys
import pygame
from settings import Settings
from ship import Ship

#-------------------------------------------------------------------------
class AlienInvasion:
    #manage source&action of the game
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
#         self.screen = pygame.display.set_mode((800,600))#(1200,800) is a tuple, define wide & tall of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)        

#---------------------------------------------------------------------
    def run_game(self):
        #main code of game
        while True:
            #detect input keys
            self._check_events()
            
            #move ship
            self.ship.update()
            
            #refresh screen
            self._update_screen()
            
#--------------------------------------------------------------
    
    #use helper method to make task clearly
    
    def _check_events(self):
        #monitor keyboard & mouse action
        for event in pygame.event.get():
            #detect if quit 
            if event.type == pygame.QUIT:
                sys.exit()
            #detect if keydown
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #when push right-buttom ship keep moving to right 1 step
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False 
            
        
        
    def _update_screen(self):
        #set color
        self.screen.fill(self.settings.bg_color)
        #locate a ship
        self.ship.blitme()
        #show the screen
        pygame.display.flip()
        
        
            
#----------------------------------------------------
if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
    