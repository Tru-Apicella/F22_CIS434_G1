import pygame
import game as g
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 180, 210))


class Button:
    """
    This class will create Start button and Quit button.
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
            font = pygame.font.SysFont('Verdana', 60)
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
    start_button.draw(screen, (0, 0, 0))
    quit_button.draw(screen, (0, 0, 0))


def redraw_game_window():
    screen.fill((0, 0, 0))


start_button = Button((38, 74, 56), 100, 200, 250, 100, "Start")
quit_button = Button((138, 55, 55), 450, 200, 250, 100, "Quit")

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
                if start_button.is_over(mouse_position):
                    print("clicked the button")
                    game_state = "game"
                    g.main() # call main class
                if quit_button.is_over(mouse_position):
                    print("clicked the 2button")
                    run = False
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEMOTION:
                if start_button.is_over(mouse_position):
                    start_button.color = (105, 105, 105)
                else:
                    start_button.color = (38, 74, 56)
                if quit_button.is_over(mouse_position):
                    quit_button.color = (105, 105, 105)
                else:
                    quit_button.color = (138, 55, 55)