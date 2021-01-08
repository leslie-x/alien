import sys
import pygame
from settings import Settings

class AlienInvasion:
    #manage source&action of the game
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
#         self.screen = pygame.display.set_mode((800,600))#(1200,800) is a tuple, define wide & tall of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        #set background color
#         self.bg_color = (230,230,230)
        
    def run_game(self):
        #main code of game
        while True:
            
            #monitor keyboard & mouse action
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #set color
            self.screen.fill(self.settings.bg_color)
                    
            pygame.display.flip()
            
#----------------------------------------------------
if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
    