class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
    

    def __init__(self):
        """Inicjacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #Ustawienia dotyczące obcego
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 1