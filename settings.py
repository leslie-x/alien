class Settings:
    
    def __init__(self):
        
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #set ship
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        
        #set bullet
        self.bullet_speed = 2
       # self.bullet_width = 300
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #bullet num max allowed
        self.bullets_allowed = 10
        
        #set alien
        self.alien_speed = 2
        self.fleet_drop_speed = 50
        #fleet_direction 1--move right, -1--move left
        self.fleet_direction = 1