import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        
        self.aliens = pygame.sprite.Group()
        
        self._creat_fleet()

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
            
            #aliens move
            self._update_aliens()
            
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
                
        self._check_bullet_alien_collisions()
                
        
            
    def _check_bullet_alien_collisions(self):
        #check if bullet hit alien,if hit then delete them
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        
        if not self.aliens:
            #if no aliens then creat a new group
            self.bullets.empty()
            self._creat_fleet()
        
        
    
        
    def _creat_fleet(self):
        """creat a group of aliens"""
        alien = Alien(self)
        
        #how many aliens in a row?
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        num_aliens_x = available_space_x // (2*alien_width)
        
        #how many rows?
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3*alien_height) - ship_height)
        num_rows = available_space_y // (2*alien_height)
        
        #creat rows of aliens
        for row_num in range(num_rows):
            for alien_num in range(num_aliens_x):
                self._creat_alien(alien_num,row_num)
            
            
    def _creat_alien(self,alien_num,row_num):
        """creat aliens in the row"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        #get location
        alien.x = alien_width + 2*alien_width*alien_num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_num
        self.aliens.add(alien)
        
        
    def _check_fleet_edges(self):
        """check if hit edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
        
    def _change_fleet_direction(self):
        """move down"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        


    def _update_aliens(self):
        """update aliens location"""
        self._check_fleet_edges()
        self.aliens.update()
       
        
    def _update_screen(self):
        #set color
        self.screen.fill(self.settings.bg_color)
        #locate a ship
        self.ship.blitme()
        #show bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #show aliens
        self.aliens.draw(self.screen)
        
        #show the screen
        pygame.display.flip()
        
        
            
#---------------------------------run-------------------
if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
    