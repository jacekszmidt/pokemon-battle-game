import pygame


class Character:
    def __init__(self):
        self.health = 70
        self.spells = {"berserk": range(18, 25),
                       "fierce berserk": range(10, 35),
                       "light healing": range(12, 28)}


class Bot(Character):
    pass


class Game:
    def __init__(self):
        pygame.init()
        self.stop_game = False
        self.bg_color = [211, 211, 211]
        self.display_width = 600
        self.display_height = 480
        self.score = 0
        self.fps_number = 15
        self.clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Pokemon_Battle_Game')
        self.character = Character()
        self.character.health = 40
        self.bot = Bot()
        self.health_green = pygame.Color('green')
        self.health_yellow = pygame.Color('yellow')
        self.health_red = pygame.Color('red')
        self.health_color_player = None  # https://stackoverflow.com/questions/40750584/this-inspection-detects-instance-attribute-definition-outside-init-method
        self.health_color_bot = None

    def health_bar(self):
        # hp bar for Character
        if self.character.health > 75:
            self.health_color_player = self.health_green
        elif self.character.health > 50:
            self.health_color_player = self.health_yellow
        else:
            self.health_color_player = self.health_red

        # hp bar for Bot
        if self.bot.health > 75:
            self.health_color_bot = self.health_green
        elif self.bot.health > 50:
            self.health_color_bot = self.health_yellow
        else:
            self.health_color_bot = self.health_red

        pygame.draw.rect(self.game_display, self.health_color_player, [15, 5, self.character.health, 25])  # printing health bar
        pygame.draw.rect(self.game_display, self.health_color_bot, [485, 5, self.bot.health, 25])  # printing health bar for Bot

    # ESC to quit
    def handle_keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.stop_game = True
                if event.key == pygame.K_ESCAPE:
                    self.stop_game = True

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
            self.clock.tick(self.fps_number)
            self.handle_keyboard_input()
            self.health_bar()
            pygame.display.update()
            self.game_over()


Game().game_loop()
