import pygame.font

class Button:
    
    def __init__(self,ai_game,msg):
        
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #set button size and other prosperity
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #creat an object of rect and locate at center
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #creat message of button
        self._prep_msg(msg)
        
        
    def _prep_msg(self,msg):
        """make msg a picture,and show upon the button"""
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)   #render() turn msg to a picture
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
        
    def draw_button(self):
        """first creat a colored button,second draw the text"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        
        
        
        
        