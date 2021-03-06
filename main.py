import random
import pygame


class Character:
    def __init__(self):
        self.health = 100
        self.health_placeholder = 100
        self.current_hp = self.health
        self.func_list = [self.spell_berserk, self.spell_fierce_berserk, self.spell_light_healing]

    def spell_berserk(self):
        self.min_dmg = 18
        self.max_dmg = 25
        self.dmg = random.randint(self.min_dmg, self.max_dmg)

        return self.dmg

    def spell_fierce_berserk(self):
        self.min_dmg = 10
        self.max_dmg = 35
        self.dmg = random.randint(self.min_dmg, self.max_dmg)

        return self.dmg

    def spell_light_healing(self):
        self.min_heal = 12
        self.max_heal = 30
        self.hp = random.randint(self.min_heal, self.max_heal)

        return self.hp


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
        self.bot = Bot()
        self.character.health = 100
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
        elif self.character.health <= 0:  # not negative values
            self.character.health = 0
        else:
            self.health_color_player = self.health_red

        # hp bar for Bot
        if self.bot.health > 75:
            self.health_color_bot = self.health_green
        elif self.bot.health > 49:
            self.health_color_bot = self.health_yellow
        elif self.bot.health <= 0:  # not negative values
            self.bot.health = 0
        else:
            self.health_color_bot = self.health_red

    def health_bar_heal(self):
        if self.character.health > 100:
            self.character.health = 100

        if self.bot.health > 100:
            self.bot.health = 100

        pygame.draw.rect(self.game_display, self.health_color_player, [50, 5, self.character.health, 25], 0)  # printing health bar
        pygame.draw.rect(self.game_display, self.border_black, [50, 5, self.character.health_placeholder, 25], 1)  # printing border
        pygame.draw.rect(self.game_display, self.health_color_bot, [460, 5, self.bot.health, 25], 0)  # printing health for Bot
        pygame.draw.rect(self.game_display, self.border_black, [460, 5, self.bot.health_placeholder, 25], 1)  # printing border for Bot

    def display_hp(self):
        font = pygame.font.SysFont("arial", 14)
        text = font.render(f"{self.character.health} / 100", True, (15, 5, 25))
        self.game_display.blit(text, (75, 9))
        text = font.render(f"{self.bot.health} / 100", True, (15, 5, 25))
        self.game_display.blit(text, (485, 9))

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
        if 160 + 85 > mouse[0] > 160 and 5 + 30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (160, 5, 85, 30))
            if click[0] == 1:
                berserk_bot = self.character.spell_berserk()
                self.bot.health = self.bot.health - berserk_bot
                berserk_char = self.character.spell_berserk()
                self.character.health = self.character.health - berserk_char
                print(f'A Bot loses {berserk_bot} hitpoints due to your attack.')
                print(f'You lose {berserk_char} hitpoints due to attack by Bot.')
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (160, 5, 85, 30))

        # second button
        if 265 + 85 > mouse[0] > 265 and 5 + 30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (265, 5, 85, 30))
            if click[0] == 1:
                berserk_bot = self.character.spell_fierce_berserk()
                self.bot.health = self.bot.health - berserk_bot
                berserk_char = self.character.spell_fierce_berserk()
                self.character.health = self.character.health - berserk_char
                print(f'A Bot loses {berserk_bot} hitpoints due to your attack.')
                print(f'You lose {berserk_char} hitpoints due to attack by Bot.')
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (265, 5, 85, 30))
        # third button
        if 370 + 85 > mouse[0] > 370 and 5 + 30 > mouse[1] > 5:
            pygame.draw.rect(self.game_display, self.btn_dark_gray, (370, 5, 85, 30))
            if click[0] == 1:
                berserk_bot = self.character.spell_light_healing()
                self.bot.health = self.bot.health + berserk_bot
                berserk_char = self.character.spell_light_healing()
                self.character.health = self.character.health + berserk_char
                print(f'A Bot healed himself for {berserk_bot} hitpoints.')
                print(f'You healed yourself for {berserk_char} hitpoints.')

        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (370, 5, 85, 30))
        # printing txt on spell_buttons
        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Berserk", True, (15, 5, 25))
        text_rect = text.get_rect(center=(160 + (85 / 2), (5 + (30 / 2))))
        self.game_display.blit(text, text_rect)

        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Fierce Berserk", True, (15, 5, 25))
        text_rect = text.get_rect(center=(265 + (85 / 2), (5 + (30 / 2))))
        self.game_display.blit(text, text_rect)

        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Light Healing", True, (15, 5, 25))
        text_rect = text.get_rect(center=(370 + (85 / 2), (5 + (30 / 2))))
        self.game_display.blit(text, text_rect)

    #  quit button
    def quit_button(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 540 + 55 > mouse[0] > 540 and 445 + 30 > mouse[1] > 445:
            pygame.draw.rect(self.game_display, self.btn_blue, (540, 445, 55, 30))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (540, 445, 55, 30))

        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Quit", True, (15, 5, 25))
        text_rect = text.get_rect(center=(540 + (55 / 2), (445 + (30 / 2))))
        self.game_display.blit(text, text_rect)

    def try_again_button(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 540 + 55 > mouse[0] > 540 and 405 + 30 > mouse[1] > 405:
            pygame.draw.rect(self.game_display, self.btn_blue, (540, 405, 55, 30))
            if click[0] == 1:
                self.game_display.fill(self.bg_color)
                self.character.health = 100
                self.bot.health = 100
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (540, 405, 55, 30))

        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Try Again", True, (15, 5, 25))
        text_rect = text.get_rect(center=(540 + (55 / 2), (405 + (30 / 2))))
        self.game_display.blit(text, text_rect)

    def start_button(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 540 + 55 > mouse[0] > 540 and 405 + 30 > mouse[1] > 405:
            pygame.draw.rect(self.game_display, self.btn_blue, (540, 405, 55, 30))
            if click[0] == 1:
                self.game_loop()
        else:
            pygame.draw.rect(self.game_display, self.btn_gray, (540, 405, 55, 30))

        font = pygame.font.SysFont("arial", 11)
        text = font.render(f"Start", True, (15, 5, 25))
        text_rect = text.get_rect(center=(540 + (55 / 2), (405 + (30 / 2))))
        self.game_display.blit(text, text_rect)

    def char_names(self):
        font = pygame.font.SysFont("arial", 14)
        text = font.render(f"YOU", True, (15, 5, 25))
        self.game_display.blit(text, (15, 9))

        font = pygame.font.SysFont("arial", 14)
        text = font.render(f"BOT", True, (15, 5, 25))
        self.game_display.blit(text, (565, 9))

    def display_hits(self):  # TBC
        pass

    # ESC to quit
    def handle_keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.stop_game = True
                if event.key == pygame.K_ESCAPE:
                    self.stop_game = True

    def draw_game_over(self):
        if self.character.health <= 0:
            self.game_display.fill(self.bg_color)
            font = pygame.font.SysFont('Verdana', 72)
            text = font.render("You Lost!", True, (0, 0, 255))
            self.game_display.blit(text, (int(self.display_width / 2) - text.get_width() // 2,
                                          (int(self.display_height / 2) - text.get_height() // 2)))
            self.try_again_button()
            self.quit_button()
            pygame.display.update()
        elif self.bot.health <= 0:
            self.game_display.fill(self.bg_color)
            font = pygame.font.SysFont('Verdana', 72)
            text = font.render("You win!", True, (0, 0, 255))
            self.game_display.blit(text, (int(self.display_width / 2) - text.get_width() // 2,
                                          (int(self.display_height / 2) - text.get_height() // 2)))
            self.try_again_button()
            self.quit_button()
            pygame.display.update()

    def draw_game_intro(self):
        intro = False
        while not intro:
            pygame.display.set_mode((self.display_width, self.display_height))
            self.game_display.fill(self.bg_color)
            self.clock.tick(self.fps_number)
            font = pygame.font.SysFont('Verdana', 42)
            text = font.render("Battle Game", True, (0, 0, 255))
            self.game_display.blit(text, (int(self.display_width / 2) - text.get_width() // 2,
                                          (int(self.display_height / 2) - text.get_height() // 2)))
            self.start_button()
            self.quit_button()
            pygame.display.update()

    def game_loop(self):
        while not self.stop_game:
            self.game_display.fill(self.bg_color)
            self.clock.tick(self.fps_number)
            self.handle_keyboard_input()
            self.health_bar()
            self.health_bar_heal()
            self.display_hp()
            self.char_names()
            self.creating_characters()
            self.spell_buttons()
            self.quit_button()
            pygame.display.update()
            self.draw_game_over()


Game().draw_game_intro()
Game().game_loop()
