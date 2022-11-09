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
FPS = 15 # max fps
IMAGES = {}
promotion_pos = ['a8','b8','c8','d8','e8','f8','g8','h8','a1','b1','c1','d1','e1','f1','g1','h1']
pawn = ['P','p']
board = chess.Board()
board_state = br.board_init(board)


def update_board(board):
    holder = str(board)
    returned = re.split('\n| ', holder)
    return returned


def check_legal(move , from_pos , to_pos, y, z):
    check_promo = board_state[z][y]
    print(check_promo)
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
    x = 0
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    br.load_images()
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
                        x = x + 1
                        print(x)
                        square_selected = (row,col)
                        playerInput.append(square_selected)
                    if len(playerInput) == 2:
                        from_pos = br.board_position(playerInput[0][0],playerInput[0][1])
                        to_pos = br.board_position(playerInput[1][0],playerInput[1][1])
                        x = 0
                        z = playerInput[0][0]
                        y = playerInput[0][1]
                        whole_pos = from_pos + to_pos
                        print(whole_pos)
                        check_legal(whole_pos , from_pos, to_pos, y,z)
                        if (board.turn == chess.WHITE):
                            print("white")
                        else:
                            print("black")
                        square_selected = ()  # reset square
                        playerInput = [] # reset input



        br.draw_game_state(screen, board_state)
        clock.tick(FPS)
        p.display.flip()
        game_status(board)
        board_state = br.board_init(board)