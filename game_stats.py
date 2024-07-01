class GameStats:
    """Monitorowanie danych statystycznych w grze "Inwazja obcych"."""


    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()


        # Najlepszy wynik nigdy nie powinien zostać wyzerowany.
        self.high_score = 0


    def reset_stats(self):
        """
        Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
