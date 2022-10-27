import chess
import re
import numpy as np
import pygame as p


WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 15 # max fps
IMAGES = {}

#push
def board_init(board):
    holder = str(board)
    temp = re.split("\n| ", holder)
    final = np.array(temp).reshape(8, 8).tolist()
    return final


# load images
def load_images():
    # WHITE
    IMAGES['P'] = p.transform.scale(p.image.load("images/wp.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['R'] = p.transform.scale(p.image.load("images/wr.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['N'] = p.transform.scale(p.image.load("images/wn.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['B'] = p.transform.scale(p.image.load("images/wb.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['Q'] = p.transform.scale(p.image.load("images/wq.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['K'] = p.transform.scale(p.image.load("images/wk.png"), (SQ_SIZE,SQ_SIZE))
    # BLACK
    IMAGES['p'] = p.transform.scale(p.image.load("images/bp.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['r'] = p.transform.scale(p.image.load("images/br.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['n'] = p.transform.scale(p.image.load("images/bn.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['b'] = p.transform.scale(p.image.load("images/bb.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['q'] = p.transform.scale(p.image.load("images/bq.png"), (SQ_SIZE,SQ_SIZE))
    IMAGES['k'] = p.transform.scale(p.image.load("images/bk.png"), (SQ_SIZE,SQ_SIZE))


def draw_game_state(screen,board):
   draw_board(screen)

   draw_pieces(screen,board)


def draw_board(screen):
    colors = [p.Color("white"), p.Color("light gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))



def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != ".":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))