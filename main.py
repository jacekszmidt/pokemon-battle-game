import pygame
import random
import math


class Character:
    def __init__(self):
        self.health = 100
        self.health_placeholder = 100
        self.func_list = [self.spell_berserk, self.spell_fierce_berserk, self.spell_light_healing]

    def spell_berserk(self):
        self.min_dmg = 18
        self.max_dmg = 25

        return random.randint(self.min_dmg, self.max_dmg)

    def spell_fierce_berserk(self):
        self.min_dmg = 10
        self.max_dmg = 35

        return random.randint(self.min_dmg, self.max_dmg)

    def spell_light_healing(self):
        self.min_heal = 12
        self.max_heal = 30

        return random.randint(self.min_heal, self.max_heal)


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
        self.character.health = 100
        self.bot = Bot()
        self.health_green = pygame.Color('green')
        self.health_yellow = pygame.Color('yellow')
        self.health_red = pygame.Color('red')
        self.border_black = pygame.Color('black')
        self.btn_gray = pygame.Color('gray')
        self.btn_dark_gray = pygame.Color('dark gray')
        self.btn_blue = pygame.Color('blue')
        self.health_color_player = None  # https://stackoverflow.com/questions/40750584/this-inspection-detects-instance-attribute-definition-outside-init-method
        self.health_color_bot = None
        self.spells_button = None

    def health_bar(self):
        # hp bar for Character
        if self.character.health > 75:
            self.health_color_player = self.health_green
        elif self.character.health > 49:
            self.health_color_player = self.health_yellow
        else:
            self.health_color_player = self.health_red

        # hp bar for Bot
        if self.bot.health > 75:
            self.health_color_bot = self.health_green
        elif self.bot.health > 49:
            self.health_color_bot = self.health_yellow
        else:
            self.health_color_bot = self.health_red

        pygame.draw.rect(self.game_display, self.health_color_player, [50, 5, self.character.health, 25], 0)  # printing health bar
        pygame.draw.rect(self.game_display, self.border_black, [50, 5, self.character.health_placeholder, 25], 1)  # printing border
        pygame.draw.rect(self.game_display, self.health_color_bot, [460, 5, self.bot.health, 25], 0)  # printing health for Bot
        pygame.draw.rect(self.game_display, self.border_black, [460, 5, self.bot.health_placeholder, 25], 1)  # printing border for Bot

    def display_hp(self):
        font = pygame.font.SysFont("arial", 14)
        text = font.render(f"{self.character.health} / 100", True, (15, 5, 25))
        self.game_display.blit(text, (80, 9))
        text = font.render(f"{self.bot.health} / 100", True, (15, 5, 25))
        self.game_display.blit(text, (490, 9))

    def creating_characters(self):
        # creating Character image
        self.water_priest = pygame.image.load("images/water-mage.png")
        self.game_display.blit(self.water_priest, (10, 50))
        # creating Bot image character
        self.dark_priest = pygame.image.load("images/dark-mage.png")
        self.game_display.blit(self.dark_priest, (360, 50))

    # drawing spell buttons and hover
    def spell_buttons(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # first button
        if 190+50 > mouse[0] > 190 and 5+30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (190, 5, 75, 30))
            if click[0] == 1:
                self.bot.health = self.bot.health - self.character.spell_berserk()
                self.character.health = self.character.health - self.character.spell_berserk()
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (190, 5, 75, 30))
        # second button
        if 270+50 > mouse[0] > 270 and 5+30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (270, 5, 75, 30))
            if click[0] == 1:
                self.bot.health = self.bot.health - self.character.spell_fierce_berserk()
                self.character.health = self.character.health - self.character.spell_fierce_berserk()
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (270, 5, 75, 30))
        # third button
        if 350+50 > mouse[0] > 350 and 5+30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (350, 5, 75, 30))
            if click[0] == 1:
                self.character.health = self.character.health + self.character.spell_light_healing()
                self.bot.health = self.bot.health + self.character.spell_light_healing()
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (350, 5, 75, 30))
        # printing txt on spell_buttons
        font = pygame.font.SysFont("arial", 13)
        text = font.render(f"Berserk", True, (15, 5, 25))
        self.game_display.blit(text, (210, 10))

        font = pygame.font.SysFont("arial", 13)
        text = font.render(f"Fierce Berserk", True, (15, 5, 25))
        self.game_display.blit(text, (272, 10))

        font = pygame.font.SysFont("arial", 13)
        text = font.render(f"Light Healing", True, (15, 5, 25))
        self.game_display.blit(text, (355, 10))

    def quit_button(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 540+55 > mouse[0] > 540 and 445+30 > mouse[1] > 445:
            pygame.draw.rect(self.game_display, self.btn_blue, (540, 445, 55, 30))
            if click[0] == 1:
                pygame.quit()
                quit()

        font = pygame.font.SysFont("arial", 14)
        text = font.render(f"Quit", True, (15, 5, 25))
        self.game_display.blit(text, (555, 450))

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
            self.display_hp()
            self.creating_characters()
            self.spell_buttons()
            self.quit_button()
            pygame.display.update()
            self.game_over()


Game().game_loop()
