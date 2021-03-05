class Settings:
    
    def __init__(self):
        
        #set screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #set ship
        self.ship_limit = 2
        
        
        #set bullet
       # self.bullet_width = 300
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #bullet num max allowed
        self.bullets_allowed = 5
        
        #set alien
        self.fleet_drop_speed = 10
        
        #speed up game rythm
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        #initislize settings which dynamic changed while gaming
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        #fleet_direction 1--move right, -1--move left
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        