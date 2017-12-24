class Settings():
    """ A class to store Alien Invasion Settings """

    def __init__(self):
        # Initialize game's static settings

        # Screen Settings
        self.screen_width = 1400
        self.screen_height = 750
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_speed_factor = 1.1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 51, 153
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        # Direction of 1 = right
        # Direction of -1 = left
        self.fleet_direction = 1

        # how quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        """Initialize settings that change throughout the game"""

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings for movement and scoring"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
