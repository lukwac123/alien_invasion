import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""
    
    
    def __init__(self):
        """Inicjacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Uruchamianie gry w trybie pełnoekranowym (wiersz 17 zastępujemy tymi poniżej):
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
                sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawnisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Uaktualnianie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        # Uaktualnianie położenia pocisków.
        self.bullets.update()


        # Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Sprawdzenie czy działa poprawnie usuwanie pocisków, które znajdą się poza ekranem
        # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reakcja na kolizję między pociskiem i obcym."""       
        # Sprawdzenie, czy którykolwiek pocisk trafił obcego.
        # Jeżeli tak, usuwamy zarówno pocisk jak i obcego.
        # Jeżeli chcemy utworzyć superpocisk, który po zestrzeleniu pierwszego obcego
        # poleci dalej to pierwszą z wartości True zmieniamy na False.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


        if not self.aliens:
            # Pozbycie się istniejących pocisków i utworzenie nowej floty.
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """
        Sprawdzanie, czy flota obcych znajduje się przy krawędzi,
        a następnie uaktualnianie położenia wszystkich obcych we flocie.
        """
        self._check_fleet_edges()
        self.aliens.update()



    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        # Utworzenie obcego i dodawanie kolejnych obcych, którzy zmieszczą się w rzędzie.
        #Odległość pomiędzy obcymi jest równa szerokości obcego.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width


            # Ukończenie rzędu, wyzerowanie wartości x oraz inkrementacja wartości y.
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Utworzenie obcego i umieszczenie go w rzędzie."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona poruszała."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        

    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)


        pygame.display.flip()
       

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()