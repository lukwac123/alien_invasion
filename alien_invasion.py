import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""
    
    
    def __init__(self):
        """Inicjacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)


    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Odświeżanie ekranu w trakcie każdej iteracji pętli.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Wyświetlanie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()
            self.clock.tick(60)
       

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()