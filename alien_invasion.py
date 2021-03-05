import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

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
        
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()
        
        self.aliens = pygame.sprite.Group()
        
        self._creat_fleet()
        
        self.play_button = Button(self,"Play")
        
        

#---------------------------------main option------------------------------------
    def run_game(self):
        #main code of game
        while True:
            #detect input keys
            self._check_events()
            
            if self.stats.game_active:
                
                #move ship
                self.ship.update()
                
                #fire bullets
                self._update_bullets()
                
                #aliens move
                self._update_aliens()
            
            
            #refresh screen
            self._update_screen()
            
            
#-----------------------------------------------------------helpers--------------------------------------------------
    
    #use helper method to make task clearly
            
 #--------------------------------------events-----------------------
            
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
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
                
    def _check_play_button(self,mouse_pos):
        """start when user clik play_button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._start_game()
            
    def _start_game(self):
    
        #reset game
        self.stats.game_active = True
        
        #clear aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
        
        #creat new aliens and relocate ship
        self._creat_fleet()
        self.ship.center_ship()
        
        #hide mouse
        pygame.mouse.set_visible(False)
            
            
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
            
        #START game
        elif event.key == pygame.K_p:
            self._start_game()
            
        
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
#----------------------------------------------bullets action--------------------------------
            
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
            #and speed up
            self.settings.increase_speed()
        
        
    
#-----------------------------------------------aliens action------------------------------------
            
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
        
        #detect if collide ship
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            
        self._check_aliens_bottom()
        
        
       
       
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            
            self.stats.ships_left -= 1
            
            self.aliens.empty()
            self.bullets.empty()
            
            self._creat_fleet()
            self.ship.center_ship()
            
            sleep(0.5)
            
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
        
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        
#----------------------------------------------screen show---------------------------
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
        
        #if game is not active then draw button
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        #show the screen
        pygame.display.flip()
        
        
            
#---------------------------------run-------------------
if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
    