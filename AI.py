import game
import random
import random

MAX,MIN = 10000,-10000
CNODE = 0


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

def pieceVal(board_state):
    total = 0
    for x in enumerate(board_state):
        for y in enumerate(x[1]):
            if y[1] == 'P':
                total+= 10 + PBias[x[0]][y[0]]
            elif y[1] =='p':
                total+= -10 + pBias[x[0]][y[0]]
            elif y[1] == 'R':
                total+= 50 + RBias[x[0]][y[0]]
            elif y[1] =='r':
                total+= -50 + rBias[x[0]][y[0]]
            elif y[1] == 'N':
                total+= 30 + nBias[x[0]][y[0]]
            elif y[1] =='n':
                total+= -30 + nBias[x[0]][y[0]]
            elif y[1] == 'B':
                total+= 30 + BBias[x[0]][y[0]]
            elif y[1] =='b':
                total+= -30 + bBias[x[0]][y[0]]
            elif y[1] == 'Q':
                total+= 90 + qBias[x[0]][y[0]]
            elif y[1] =='q':
                total+= -90 + qBias[x[0]][y[0]]
            elif y[1] == 'K':
                total+= 900 + KBias[x[0]][y[0]]
            elif y[1] =='k':
                total+= -900 + kBias[x[0]][y[0]]
    return total

class Piece:
    def __init__(self):
        self.pos = '0'
        self.piece = '0'
        self.nextPos = []
        self.x = []
        self.y = []
        self.eval = []
        self.boards = []
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
                    nboard = game.check_legal((p1[x].pos+p1[x].nextPos[-1]),p1[x].pos,p1[x].nextPos[-1],p1[x].y[-1],p1[x].x[-1],board, board_state)
                    nboard_state = game.br.board_init(nboard)
                    (p1[x].boards).append(nboard_state)
                    board.pop()
                    count+=1
        if count == 0 or i == 0:
            p1[createdNode] = Piece()
            p1[createdNode].pos = posActual[i]
            (p1[createdNode].nextPos).append(nPosActual[i])
            p1[createdNode].piece = board_state[origPos2[i]][origPos[i]]
            (p1[createdNode].x).append(newPos2[i])
            (p1[createdNode].y).append(newPos[i])
            try:
                nboard = game.check_legal((p1[createdNode].pos+p1[createdNode].nextPos[0]),p1[createdNode].pos,p1[createdNode].nextPos[0],p1[createdNode].y[0],p1[createdNode].x[0],board, board_state)
                nboard_state = game.br.board_init(nboard)
                (p1[createdNode].boards).append(nboard_state)
                board.pop()
            except:
                print("lazy bug fix")
            createdNode+=1
        i+=1
    p1 = list(filter(None, p1))
    if det == 0:
        random.shuffle(p1)
        global CNODE
        h = CNODE + createdNode
        CNODE= h
        return p1,createdNode
    elif det ==1:
        return p1

def createTree(board,board_state, depth,iters,alpha,beta):
    iters+=1
    p1, createdNode = createMove(board,board_state,0)
    p1 = createEval(p1, createdNode,board_state)
    if depth == 3:
        lowest = 9999
        for x in p1:
            if lowest < min(x.eval):
                lowest = min(x.eval)
        return p1, depth, lowest
    if board.turn == True:
        best = MIN
        for x in range(createdNode):
            for y in range(len(p1[x].x)):
                if depth < 3:
                    nboard = game.check_legal((p1[x].pos+p1[x].nextPos[y]),p1[x].pos,p1[x].nextPos[y],p1[x].y[y],p1[x].x[y],board, board_state)
                    nboard_state = game.br.board_init(nboard)
                    depth+=1
                    tmp,depth,val = (createTree(nboard, nboard_state,depth,iters,alpha,beta))
                    depth-=1
                    board.pop()
                    (p1[x].nodes).append(tmp)
                    best = max(best, val)
                    alpha = max(alpha,best)

                    if beta >= alpha:
                        break
        if iters != 1:
            iters-=1
            return p1,depth,best    
                
    else:
        best = MAX
        for x in range(createdNode):
            for y in range(len(p1[x].x)):
                if depth < 3:
                    nboard = game.check_legal((p1[x].pos+p1[x].nextPos[y]),p1[x].pos,p1[x].nextPos[y],p1[x].y[y],p1[x].x[y],board, board_state)
                    nboard_state = game.br.board_init(nboard)
                    depth+=1
                    tmp,depth,val = (createTree(nboard, nboard_state,depth,iters,alpha,beta))
                    depth-=1
                    board.pop()
                    (p1[x].nodes).append(tmp)
                    best = max(best, val)
                    best = max(beta, best)
        
                    if beta >= alpha:
                        break

        if iters != 1:
            iters-=1
            return p1,depth,best
    
    return p1

def createEval(p1, createdNode,board_state):
    for x in range(createdNode):
        for y in range(len(p1[x].x)):
            p1[x].eval.append(pieceVal(board_state))
    return p1

def otherSearchTree(p1):
    try:
        if p1[0].nodes:
            for x in enumerate(p1):
                for y in enumerate(x[1].nodes):
                    lowest, bestPos,bestNPos = otherSearchTree(y[1])
                    x[1].eval[y[0]] = lowest-x[1].eval[y[0]]
    except:
        print("This try except should fix the error i was having")
    lowest = 9999  
    for x in p1:
        if lowest > min(x.eval):
            lowest = min(x.eval)
            bestPos = x.pos
            for y in enumerate(x.eval):
                if y[1] == lowest:
                    bestNPos = x.nextPos[y[0]]
                    
    return lowest, bestPos,bestNPos


#created tree of the best moves for ai & randomizes the best move so ai doesnt choice same thing everytime
def getBestMove(self):
        bestMove = self.otherSearchTree(createTree)
        randombestMove = random.choice(bestMove)
        return randombestMove


def AIRunner(board,board_state):
    p1 = createTree(board,board_state,0,0,MIN,MAX)
    highest, bestPos,bestNPos = otherSearchTree(p1)
    print(CNODE)
    return bestPos,bestNPos



