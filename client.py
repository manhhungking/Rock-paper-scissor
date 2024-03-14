import pygame
import time
from network import Network

pygame.font.init()

# set up
WIDTH = 700
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")


class Button:

    def __init__(self, text, x, y, width, height, colour):
        self.text = text
        self.width = width
        self.height = height
        self.colour = colour

        # Adjust x and y to center the button
        self.x = x - self.width // 2
        self.y = y - self.height // 2

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("verdana", 20)
        text = font.render(self.text, 1, (255, 255, 224))
        text_width, text_height = text.get_size()

        win.blit(
            text,
            (
                self.x + round(self.width / 2) - round(text_width / 2),
                self.y + round(self.height / 2) - round(text_height / 2),
            ),
        )

    def click(self, position):
        x1 = position[0]
        y1 = position[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color("lightskyblue3")
        self.color_active = pygame.Color("dodgerblue2")
        self.color = self.color_inactive
        self.text = ""
        self.font = pygame.font.SysFont("verdana", 30)
        self.active = False
        self.text_surface = self.font.render(self.text, True, self.color_active)

    def handle_event(self, event):
        if event == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    # Send the entered ID to the server
                    network.send(f"id:{self.text}")
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = self.font.render(self.text, True, self.color_active)

    def update(self):
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, win):
        width = max(200, self.text_surface.get_width() + 10)
        pygame.draw.rect(win, self.color, self.rect, 2)
        pygame.draw.rect(
            win,
            (255, 255, 255),
            (self.rect.x + 5, self.rect.y + 5, width - 10, self.rect.height - 10),
        )
        win.blit(
            self.text_surface,
            (self.rect.x + 10, self.rect.y + 10, width - 20, self.rect.height - 20),
        )
        pygame.display.flip()


# functions
def re_draw_window(win, game, player):
    # win.fill((0, 13, 26))
    win.fill((144, 199, 255))

    if not (game.connected()):
        # other player is yet to connect
        font = pygame.font.SysFont("verdana", 36)
        text = font.render("Waiting for another player...", (255, 255, 255), True)
        win.blit(
            text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2)
        )
    else:
        font1 = pygame.font.SysFont("verdana", 28)
        font = pygame.font.SysFont("verdana", 36)
        if player == 0:
            wins = game.wins[0]
            loses = game.wins[1]
        else:
            wins = game.wins[1]
            loses = game.wins[0]

        text_wins = font1.render("Wins: {}".format(wins), 1, (0, 0, 0))
        text_loses = font1.render("Loses: {}".format(loses), 1, (0, 0, 0))
        text_draws = font1.render("Draws: {}".format(game.draws), 1, (0, 0, 0))
        window.blit(text_wins, (WIDTH // 2 - 200, 50))
        window.blit(text_loses, (WIDTH // 2 - 50, 50))
        window.blit(text_draws, (WIDTH // 2 + 95, 50))
        text = font.render("Your Move", 1, (35, 49, 179))
        win.blit(text, (100, 200))

        text = font.render("Opponent's", 1, (35, 49, 179))
        win.blit(text, (400, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.both_went():
            text1 = font.render(move1, 1, (0, 102, 102))
            text2 = font.render(move2, 1, (0, 102, 102))
        else:
            # check if we need to hide opponents move
            if game.p1_went and player == 0:
                text1 = font.render(move1, 1, (0, 102, 102))
            elif game.p1_went:
                text1 = font.render("Locked in", 1, (0, 102, 102))
            else:
                text1 = font.render("Waiting...", 1, (0, 102, 102))

            if game.p2_went and player == 1:
                text2 = font.render(move2, 1, (0, 102, 102))
            elif game.p2_went:
                text2 = font.render("Locked in", 1, (0, 102, 102))
            else:
                text2 = font.render("Waiting...", 1, (0, 102, 102))

        if player == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for button in buttons:
            button.draw(win)

    pygame.display.update()


enter_id_button = Button(
    "Enter the ID of the player", WIDTH // 2, 450, 300, 50, (102, 0, 51)
)

buttons = [
    Button("Rock", 180, 500, 150, 100, (226, 164, 153)),
    Button("Scissors", 365, 500, 150, 100, (49, 189, 133)),
    Button("Paper", 550, 500, 150, 100, (14, 99, 247)),
]

input_box = InputBox(WIDTH // 2 - 150, 450, 300, 50)


# functions
def introduction_screen():
    run = True
    clock = pygame.time.Clock()

    intro_text1 = "Welcome to Rock-Paper-Scissors Online!"
    intro_text2 = "Gameplay: Each player has a maximum of 3 points,"
    intro_text3 = "and the first player that reaches 3 points wins the game."

    while run:
        clock.tick(60)
        window.fill((144, 199, 255))
        font = pygame.font.SysFont("verdana", 20)

        text1 = font.render(intro_text1, 1, (0, 5, 10))
        text2 = font.render(intro_text2, 1, (0, 5, 10))
        text3 = font.render(intro_text3, 1, (0, 5, 10))

        window.blit(text1, (WIDTH / 2 - text1.get_width() / 2, 50))
        window.blit(text2, (WIDTH / 2 - text2.get_width() / 2, 100))
        window.blit(text3, (WIDTH / 2 - text3.get_width() / 2, 150))

        instruction_image = pygame.image.load("Rock-paper-scissors.png")
        instruction_image_scaled = pygame.transform.scale(instruction_image, (400, 400))
        image_rect = instruction_image_scaled.get_rect()
        image_rect.center = (350, 400)  # center image
        window.blit(instruction_image_scaled, image_rect)

        button_font = pygame.font.SysFont("verdana", 24)

        play_random_button = Button(
            "Play with a random player", WIDTH / 2, 640, 300, 50, (51, 102, 0)
        )

        play_random_button.draw(window)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return "quit"
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if play_random_button.click(position):
                    return "random"


def menu_screen(network):
    run = True
    clock = pygame.time.Clock()

    input_box = InputBox(
        WIDTH // 2 - 150, 500, 300, 40
    )  # Adjust position and size as needed

    entering_id = False  # Flag to indicate if entering ID mode

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if enter_id_button.click(position):
                    entering_id = True
                elif entering_id and input_box.rect.collidepoint(position):
                    entering_id = True
                else:
                    run = False

            # Handle events for the input box only when entering_id is True
            if entering_id:
                input_box.handle_event(event)

        window.fill((144, 199, 255))

        font = pygame.font.SysFont("verdana", 40)
        text = font.render("Click anywhere to play!", 1, (0, 5, 10))
        window.blit(
            text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2)
        )

        pygame.display.update()

    player_choice = introduction_screen()

    if player_choice == "quit":
        pygame.quit()
    elif player_choice == "random":
        # Connect to the server and send the player choice
        network.connect()
        network.send("random")

        # Start the game
        main(network)
    elif player_choice == "id":
        # Get the ID from the input box only if entering_id is True
        player_id = input_box.text if entering_id else ""

        # Connect to the server and send the player choice
        network.connect()
        network.send(f"id:{player_id}")

        # Start the game
        main(network)


# main function
def main(network):
    run = True
    clock = pygame.time.Clock()
    player = int(network.get_player())
    print("You are player number: {}".format(player))

    while run:
        clock.tick(60)
        try:
            game = network.send("get")
        except:
            run = False
            print("Could not retrieve game from server - game failed locally")
            break

        if game.both_went():
            re_draw_window(window, game, player)
            try:
                game = network.send("soft-reset")
            except:
                run = False
                print("Could not retrieve game from server")
                break

            font = pygame.font.SysFont("verdana", 90)
            if player == 0:
                game = network.send("find-winner")
            winner = game.find_winner()

            if (winner == 1 and player == 1) or (winner == 0 and player == 0):
                text = font.render("Win!", 1, (207, 181, 59))

            elif winner == -1:
                text = font.render("Draw!", 1, (211, 211, 211))

            else:
                text = font.render("Lose!", 1, (194, 26, 26))

            window.blit(
                text,
                (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height()),
            )
            pygame.display.update()
            time.sleep(3)
            # if game.check_end() == -1:
            #     network.send("soft-reset")
            if game.check_end() == player:
                re_draw_window(window, game, player)
                text = font.render("You Win!", 1, (232, 181, 59))
                window.blit(
                    text,
                    (
                        WIDTH / 2 - text.get_width() / 2,
                        HEIGHT / 2 - text.get_height(),
                    ),
                )
                pygame.display.update()
                time.sleep(3)
                network.send("hard-reset")
            elif game.check_end() == 1 - player:
                re_draw_window(window, game, player)
                text = font.render("You lose!", 1, (194, 26, 26))
                window.blit(
                    text,
                    (
                        WIDTH / 2 - text.get_width() / 2,
                        HEIGHT / 2 - text.get_height(),
                    ),
                )
                pygame.display.update()
                time.sleep(3)
                network.send("hard-reset")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                for button in buttons:
                    if button.click(position) and game.connected():
                        if player == 0:
                            if game.p1_went is False:
                                # check if player has not made a move
                                # if not, send move to server
                                network.send(button.text)
                        else:
                            if game.p2_went is False:
                                # check if player has not made a move
                                # if not, send move to server
                                network.send(button.text)

        re_draw_window(window, game, player)


while True:
    network = Network()
    menu_screen(network)
