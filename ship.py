import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym."""

    def __init__(self, ai_game):
        """Inicjacja statku kosmicznego i jego położenie początkowe."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings()

        # Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.x = float(self.rect.x)

        # Opcje wskazjące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Uaktualnianie położenia statku na podstawie opcji wskazującej na jego ruch."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect na podstawie wartości self x.
        self.rect.x = self.x


    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect) 