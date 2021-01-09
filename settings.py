class Settings:
    
    def __init__(self):
        
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #set ship's speed
        self.ship_speed = 1.5
        
        
        #set bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #bullet num max allowed
        self.bullets_allowed = 10