import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

#-------------------------------class define------------------------------------------
class AlienInvasion:
    #manage source&action of the game
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        #show game in fullscreen
#         self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#         self.settings.screen_width = self.screen.get_rect().width
#         self.settings.screen_height = self.screen.get_rect().height
        
#         self.screen = pygame.display.set_mode((800,600))#(1200,800) is a tuple, define wide & tall of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()

#---------------------------------main option------------------------------------
    def run_game(self):
        #main code of game
        while True:
            #detect input keys
            self._check_events()
            
            #move ship
            self.ship.update()
            
            #fire bullets
            self._update_bullets()
            
            #refresh screen
            self._update_screen()
            
            
#-----------------------------------helpers---------------------------
    
    #use helper method to make task clearly
    
    def _check_events(self):
        #monitor keyboard & mouse action
        for event in pygame.event.get():
            
            #detect if quit 
            if event.type == pygame.QUIT:
                sys.exit()
                
            #detect if keydown
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            
            
    def _check_keydown_events(self,event):
        
        if event.key == pygame.K_RIGHT:
            #when push right-buttom ship keep moving to right 1 step
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            
        #press Q to quit out
        elif event.key == pygame.K_q:
            sys.exit()
            
        #fire
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
        
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
            
    def _fire_bullet(self):
        """creat a bullet and put in group"""
        #if bullets num in screen is less than allowed then creat
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
        
    def _update_bullets(self):
        """relocate bullets"""
        self.bullets.update()

        #delet outframe bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #debug to see how many bullets still remain
        #print(len(self.bullets))
    
        
    def _update_screen(self):
        #set color
        self.screen.fill(self.settings.bg_color)
        #locate a ship
        self.ship.blitme()
        #show bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #show the screen
        pygame.display.flip()
        
        
            
#---------------------------------run-------------------
if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
    