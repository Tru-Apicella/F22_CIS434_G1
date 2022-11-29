import board as br
import game
import random

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



#randomizes all the moves the legal move the ai can make
def getRandomMove(self):
        legalMoves = list(game.check_legal)
        randomMove = random.choice(legalMoves)
        return randomMove

#createMove creates nodes for every move that contain piece current position and next position
def createMove(board,board_state,det):
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
    p1 = list(filter(None, p1))
    if det == 0:
        return p1,createdNode
    elif det ==1:
        return p1

def createTree(board,board_state, depth,iters):
    iters+=1
    p1, createdNode = createMove(board,board_state,0)
    p1 = createEval(p1, createdNode)

    for x in range(createdNode):
        for y in range(len(p1[x].x)):
            if depth < 2:
                nboard = game.check_legal((p1[x].pos+p1[x].nextPos[y]),p1[x].pos,p1[x].nextPos[y],p1[x].y[y],p1[x].x[y],board, board_state)
                nboard_state = br.board_init(nboard)
                depth+=1
                tmp,depth = (createTree(nboard, nboard_state,depth,iters))
                depth-=1
                board.pop()
                (p1[x].nodes).append(tmp)
            elif depth == 2:
                return p1, depth
    if iters != 1:
        iters-=1
        return p1,depth
    
    print("placeholder")
    otherSearchTree(p1)


def createEval(p1, createdNode):
    for x in range(createdNode):
        for y in range(len(p1[x].x)):
            p1[x].eval.append(pieceVal(p1[x].piece, p1[x].x[y],p1[x].y[y]))
    return p1

def otherSearchTree(p1):
    if p1[0].nodes:
        for x in enumerate(p1):
            for y in enumerate(x[1].nodes):
                highest, bestPos,bestNPos = otherSearchTree(y[1])
                x[1].eval[y[0]] = highest+x[1].eval[y[0]]
    highest = -9999  
    for x in p1:
        if highest < max(x.eval):
            highest = max(x.eval)
            bestPos = x.pos
            for y in enumerate(x.eval):
                if y[1] == highest:
                    bestNPos = x.nextPos[y[0]]
                    
    return highest, bestPos,bestNPos


#created tree of the best moves for ai & randomizes the best move so ai doesnt choice same thing everytime
def getBestMove(self):
        bestMove = self.otherSearchTree(createTree)
        randombestMove = random.choice(bestMove)
        return randombestMove




