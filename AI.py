import board as br
import game
import chess
'''
proccess: random move -> assign evaluation to the move -> put in binary tree -> continue for all moves ->
eval n number of furture moves for all previous moves -> put in binary tree -> parse tree to find move with lowest/highest eval
stuff done: piece bias and eval of each piece
stuff needed: functuion to create random legal moves, function to create binary tree with eval nums,  
function to search binary tree to find the highest/lowest eval total, and probably add alpha beta pruning
'''
PBias = [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]
pBias = PBias[::-1]

RBias = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]
rBias = RBias[::-1]

BBias = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]
bBias = BBias[::-1]

nBias = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]

qBias = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

KBias = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]
kBias = KBias[::-1]

def pieceVal(piece,x,y):
    if piece == 'P':
        return 10 + PBias[x][y]
    elif piece =='p':
        return -10 - pBias[x][y]
    elif piece == 'R':
        return 50 + RBias[x][y]
    elif piece =='r':
        return -50 - rBias[x][y]
    elif piece == 'N':
        return 30 + nBias[x][y]
    elif piece =='n':
        return -30 - nBias[x][y]
    elif piece == 'B':
        return 30 + BBias[x][y]
    elif piece =='b':
        return -30 - bBias[x][y]
    elif piece == 'Q':
        return 90 + qBias[x][y]
    elif piece =='q':
        return -90 - qBias[x][y]
    elif piece == 'K':
        return 900 + KBias[x][y]
    elif piece =='k':
        return -900 - kBias[x][y]

class Piece:
    def __init__(self):
        self.pos = '0'
        self.piece = '0'
        self.nextPos = []
        self.x = []
        self.y = []
        self.eval = []
        self.nodes = []

def convertPos(i):
    if i =='8' or i =='a':return 0
    if i =='7' or i =='b':return 1
    if i =='6' or i =='c':return 2
    if i =='5' or i =='d':return 3
    if i =='4' or i =='e':return 4
    if i =='3' or i =='f':return 5
    if i =='2' or i =='g':return 6
    if i =='1' or i =='h':return 7

#createMove creates nodes for every move that contain piece current position and next position
def createMove(board,board_state):
    x = 0
    moves = []
    while(True):
        try:
            moves.append(str(list(board.legal_moves)[x]))
            x+=1
        except:
            break
    
    origPos, origPos2, newPos, newPos2, posActual,nPosActual = [],[],[],[],[],[]
    tmp = 0
    for i in moves:
        tmp = convertPos(i[:1])
        origPos.append(tmp)
    for i in moves:
        tmp = convertPos(i[1:2])
        origPos2.append(tmp)
    for i in moves:
        tmp = convertPos(i[2:3])
        newPos.append(tmp)
    for i in moves:
        tmp = convertPos(i[3:])
        newPos2.append(tmp)
    for i in moves:
        posActual.append(i[:2])
    for i in moves:
        nPosActual.append(i[2:])
    p1 = [0]*len(moves)
    i = 0
    
    createdNode=0
    while i < len(moves):
        count = 0
        for x in range(createdNode):
            if x!=i:
                if p1[x].pos == posActual[i]:
                    (p1[x].nextPos).append(nPosActual[i])
                    (p1[x].x).append(newPos2[i])
                    (p1[x].y).append(newPos[i])
                    count+=1
        if count == 0 or i == 0:
            p1[createdNode] = Piece()
            p1[createdNode].pos = posActual[i]
            (p1[createdNode].nextPos).append(nPosActual[i])
            p1[createdNode].piece = board_state[origPos2[i]][origPos[i]]
            (p1[createdNode].x).append(newPos2[i])
            (p1[createdNode].y).append(newPos[i])
            createdNode+=1
        i+=1
    createTree(p1,createdNode)

#another alternate way of moving the piece and checking for legal and illgeal moves??? (could use some code from the createMove and
# input it into the class ai portion)
class AI:
    infinite = 10000000
    def GetAiMove(chessboard, invalid_moves):
        best_move = 0
        best_score = AI.infinite
        for move in chessboard.get_possible_moves(Piece.Piece.BLACK):
            if (AI.is_invalid_move(move, invalid_moves)):
                continue

            #need to put in code to actually move the piceces
     
        #checkmate move
        if (best_move == 0):
            return 0


def createTree(p1,createdNode):
    for x in range(createdNode):
        for y in range(len(p1[x].x)):
            p1[x].eval.append(pieceVal(p1[x].piece, p1[x].x[y],p1[x].y[y]))
    game.check_legal((p1[0].pos+p1[0].nextPos[0]),p1[0].pos,p1[0].nextPos[0],p1[0].x[0],p1[0].y[0])


def searchTree():
    print('placeholder')
