import chess
import chess.svg
import re
import random
import board as br
import pygame as p
import AI


WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 15  # max fps
IMAGES = {}
promotion_pos = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8',
                 'h8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
pawn = ['P', 'p']
board = chess.Board()
board_state = br.board_init(board)


def update_board(board):
    holder = str(board)
    returned = re.split('\n| ', holder)
    return returned


def check_legal(move, from_pos, to_pos, y, z, board, board_state):
    check_promo = board_state[z][y]
    print(check_promo)
    print(y, z)
    # check if the piece moving is a pawn to change the input for promotion
    if check_promo == 'p':
        if to_pos in promotion_pos:
            print("we in")
            to_pos = to_pos + "q"
            move = from_pos + to_pos
            print(move)
            print(list(board.legal_moves))
    elif check_promo == 'P':
        if to_pos in promotion_pos:
            to_pos = to_pos + "q"
            move = from_pos + to_pos
            print(move)
            print(list(board.legal_moves))
    if chess.Move.from_uci(move) in board.legal_moves:
        print(list(board.legal_moves))
        board.push_san(move)
        return board
    else:
        print(list(board.legal_moves))
        print("not legal")

# this function has no use currently, but it did help with debugging earlier


def random_move(board):
    move_holder = list(board.legal_moves)
    move_returned = random.choice(move_holder)
    return move_returned


def game_status(board):
    # using is_ functions to check for relevant game rules
    if board.is_checkmate():
        msg = "checkmate: " + str(not board.turn) + " wins!"
        result = not board.turn
        print(msg)
        print(result)
    elif board.is_stalemate():
        msg = "draw: stalemate"
        print(msg)
    elif board.is_fivefold_repetition():
        msg = "draw: 5-fold repetition"
        print(msg)
    elif board.is_insufficient_material():
        msg = "draw: insufficient material"
        print(msg)
    elif board.can_claim_draw():
        msg = "draw: claim"
        print(msg)

# adding a type for main so that when 0 its player vs play and 1 is player vs ai


def main(type):
    p.init()
    x = 0
    screen = p.display.set_mode((WIDTH, 600))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))

    # # hhhhhhhhhhhhhhhhh
    # font = p.font.Font('freesansbold.ttf', 32)
    # text = font.render('GeeksForGeeks', True, (0, 255, 0), (0, 0, 128))
    # textRect = text.get_rect()
    # textRect.center = (200, 550)
    # screen.blit(text, textRect)
    # # hhhhhhhhhhhhhhhhhhhhhh

    # load images once to avoid consuming resources
    br.load_images()
    running = True
    square_selected = ()  # last click of the player
    playerInput = []
    while running:
        if board.turn == True or type == 0:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                # take input using pygame function then converting to actual 2d board position
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    # taking the input and splitting it between from, to, and pawn position if needed
                    if square_selected == (row, col):
                        square_selected = ()  # reset square
                        playerInput = []  # reset input
                    else:
                        x = x + 1
                        print(x)
                        square_selected = (row, col)
                        br.highlightSquares(
                            screen, board_state, board.legal_moves, square_selected)
                        playerInput.append(square_selected)
                    if len(playerInput) == 2:
                        from_pos = br.board_position(
                            playerInput[0][0], playerInput[0][1])
                        to_pos = br.board_position(
                            playerInput[1][0], playerInput[1][1])
                        x = 0
                        z_from = playerInput[0][0]
                        y_from = playerInput[0][1]
                        z = playerInput[1][0]
                        y = playerInput[1][1]
                        check_pawn = board_state[z_from][y_from]
                        print(check_pawn)
                        if check_pawn == 'p':
                            z = z_from
                            y = y_from
                        elif check_pawn == 'P':
                            z = z_from
                            y = y_from
                        whole_pos = from_pos + to_pos
                        print(whole_pos)
                        check_legal(whole_pos, from_pos, to_pos,
                                    y, z, board, board_state)
                        # print whose turn it is for better debugging and player experince
                        if (board.turn == chess.WHITE):
                            print("white")
                            # To show that it's the black turn
                            font = p.font.Font('freesansbold.ttf', 32)
                            text = font.render(
                                'White', True, (0, 255, 0), (0, 0, 128))
                            textRect = text.get_rect()
                            textRect.center = (200, 550)
                            screen.blit(text, textRect)

                        else:
                            print("black")
                            # To show that it's the black turn
                            font = p.font.Font('freesansbold.ttf', 32)
                            text = font.render(
                                'Black', True, (0, 255, 0), (0, 0, 128))
                            textRect = text.get_rect()
                            textRect.center = (200, 550)
                            screen.blit(text, textRect)

                        square_selected = ()  # reset square
                        playerInput = []  # reset input
        elif board.turn == False and type == 1:
            pos, nextPos = AI.AIRunner(board, board_state)
            np0 = AI.convertPos(nextPos[:1])
            np1 = AI.convertPos(nextPos[1:2])
            check_legal((pos+nextPos), pos, nextPos,
                        np0, np1, board, board_state)
        # loop for updating the game board and screen
        board_state = br.board_init(board)
        br.draw_game_state(screen, board_state, check_legal, square_selected)
        clock.tick(FPS)
        p.display.flip()
        game_status(board)


# call main to avoid any errors
if __name__ == "__main__":
    main(0)
