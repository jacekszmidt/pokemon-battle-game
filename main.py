import pygame


class Character:
    def __init__(self):
        self.health = 100
        self.spells = {"berserk": range(18, 25),
                       "fierce berserk": range(10, 35),
                       "light healing": range(12, 28)}
        self.game = Game()


class Bot(Character):
    pass


class Game:
    def __init__(self):
        pygame.init()
        self.stop_game = False
        self.bg_color = [255, 255, 255]
        self.display_width = 600
        self.display_height = 480
        self.score = 0
        self.fps_number = 15
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Pokemon_Battle_Game')
        self.character = Character()
        self.bot = Bot()
        self.health_green = pygame.Color(255, 160, 122, 255)
        self.health_yellow = pygame.Color(255, 255, 153, 255)
        self.health_red = pygame.Color(255, 0, 0, 255)

    def health_bar(self):
        if self.character.health > 75:
            self.health_color = self.health_green
        elif self.character.health > 50:
            self.health_color = self.health_yellow
        else:
            self.health_color = self.health_red

        pygame.draw.rect(self.game_display, self.health_color, (580, 25, self.character.health, 25))

    def game_over(self):
        if self.character.health <= 0 \
                or self.bot.health <= 0:
            self.stop_game = True
            print("Game Over!")
        else:
            pass

    def game_loop(self):
        while not self.stop_game:
            self.game_display.fill(self.bg_color)
            pygame.display.update()
            self.game_over()
            self.health_bar()


Game().game_loop()
