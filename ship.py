import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym."""

    def __init__(self, ai_game):
        """Inicjacja statku kosmicznego i jego położenie początkowe."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Opcje wskazjące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Uaktualnianie położenia statku na podstawie opcji wskazującej na jego ruch."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect) 