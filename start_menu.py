import pygame
import game as g
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 180, 210))

# Upload the background image
background = pygame.image.load("background.png")


class Button:
    """
    This class will create the menue buttons.
    """

    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2,
                             self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('gabriola', 35)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                        self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, position):
        # Position is the mouse position or a tuple of (x,y) coordinates
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                return True
        return False


def redraw_menu_window():
    screen.fill((153, 141, 141))
    # Draw the background image on the screen
    screen.blit(background, (0, 0))
    vs_player_btn.draw(screen, (0, 0, 0))
    vs_AI_btn.draw(screen, (0, 0, 0))
    quit_button.draw(screen, (0, 0, 0))


def redraw_game_window():
    screen.fill((0, 0, 0))


vs_player_btn = Button((255, 239, 213), 100, 200,
                       250, 100, "Player Vs. Player")
vs_AI_btn = Button((255, 239, 213), 450, 200, 250, 100, "Player Vs. Computer")
quit_button = Button((255, 239, 213), 275, 400, 250, 100, "Quit")

game_state = "menu"
run = True
while run:
    if game_state == "menu":
        redraw_menu_window()
    elif game_state == "game":
        redraw_game_window()
    pygame.display.update()

    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vs_player_btn.is_over(mouse_position):
                    print("clicked the button")
                    game_state = "game"
                    g.main(0)  # call main class
                    pygame.quit()
                if vs_AI_btn.is_over(mouse_position):
                    print("clicked the 2button")
                    game_state = "game"
                    g.main(1)  # call main class
                    pygame.quit()
                if quit_button.is_over(mouse_position):
                    print("clicked the 3button")
                    run = False
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEMOTION:
                if vs_player_btn.is_over(mouse_position):
                    vs_player_btn.color = (108, 85, 79, 255)
                else:
                    vs_player_btn.color = (255, 239, 213)
                if vs_AI_btn.is_over(mouse_position):
                    vs_AI_btn.color = (108, 85, 79, 255)
                else:
                    vs_AI_btn.color = (255, 239, 213)
                if quit_button.is_over(mouse_position):
                    quit_button.color = (138, 55, 55)
                else:
                    quit_button.color = (255, 239, 213)
