import chess
import chess.svg
import re
import random
import board as br
import pygame as p

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 15 # max fps
IMAGES = {}

board = chess.Board()


def update_board(board):
    holder = str(board)
    returned = re.split('\n| ', holder)
    return returned


def check_legal(move):
    if chess.Move.from_uci(move) in board.legal_moves:
        board.push_san(move)
        return 1
    else:
        return 0

def random_move(board):
    move_holder = list(board.legal_moves)
    move_returned = random.choice(move_holder)
    return move_returned

def game_status(board):
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

if __name__ == "__main__":
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    br.load_images()
    board_state = br.board_init(board)
    running = True
    square_selected = () # last click of the player
    playerInput = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if square_selected == (row,col):
                        square_selected = () # reset square
                        playerInput = [] # reset input
                    else:
                        square_selected = (row,col)
                        playerInput.append(square_selected)
                    if len(playerInput) == 2:
                        from_pos = br.board_position(playerInput[0][0],playerInput[0][1])
                        to_pos = br.board_position(playerInput[1][0],playerInput[1][1])
                        whole_pos = from_pos + to_pos
                        check_legal(whole_pos)
                        square_selected = ()  # reset square
                        playerInput = [] # reset input



        br.draw_game_state(screen, board_state)
        clock.tick(FPS)
        p.display.flip()
        game_status(board)
        move = "a2a3"
        check_legal(move)
        board_state = br.board_init(board)