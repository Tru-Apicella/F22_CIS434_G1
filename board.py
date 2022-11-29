import chess
import re
import numpy as np
import pygame as p




WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 15  # max fps
IMAGES = {}

# push


def board_init(board):
    holder = str(board)
    temp = re.split("\n| ", holder)
    final = np.array(temp).reshape(8, 8).tolist()
    return final


def board_position(x, y):
    chess_pos = [
        ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
        ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
        ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    ]
    return chess_pos[x][y]


# load images
def load_images():
    # WHITE
    IMAGES['P'] = p.transform.scale(p.image.load(
        "images_1/wp.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['R'] = p.transform.scale(p.image.load(
        "images_1/wr.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['N'] = p.transform.scale(p.image.load(
        "images_1/wn.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['B'] = p.transform.scale(p.image.load(
        "images_1/wb.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['Q'] = p.transform.scale(p.image.load(
        "images_1/wq.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['K'] = p.transform.scale(p.image.load(
        "images_1/wk.png"), (SQ_SIZE, SQ_SIZE))
    # BLACK
    IMAGES['p'] = p.transform.scale(p.image.load(
        "images_1/bp.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['r'] = p.transform.scale(p.image.load(
        "images_1/br.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['n'] = p.transform.scale(p.image.load(
        "images_1/bn.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['b'] = p.transform.scale(p.image.load(
        "images_1/bb.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['q'] = p.transform.scale(p.image.load(
        "images_1/bq.png"), (SQ_SIZE, SQ_SIZE))
    IMAGES['k'] = p.transform.scale(p.image.load(
        "images_1/bk.png"), (SQ_SIZE, SQ_SIZE))


# highlights the square selected and shows possible moves the player can make
def highlightSquares(screen, board_state, check_legal, square_selected):
    if square_selected != ():
        row, col = square_selected
        if board_state[row][col][0] == ('white' if chess.WHITE else 'black'):
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)  # transperancy value
            s.fill(p.Color('yellow'))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

           #highlight moves from that square (check legal variable needs to be change possibly to get to work)
           ''' s.fill(p.Color('blue'))
           for move in legal_move:
            startRow = AI.convertPos(move[:1])
            startCol = AI.convertPos(move[1:2])
            screen.blit(s,(SQ_SIZE*startRow, SQ_SIZE*startCol))'''

def draw_game_state(screen, board, check_legal, square_selected):
    draw_board(screen)
    highlightSquares(screen, board, check_legal, square_selected)
    draw_pieces(screen, board)


def draw_board(screen):
    colors = [p.Color("white"), p.Color("light gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(
                c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != ".":
                screen.blit(IMAGES[piece], p.Rect(
                    c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
