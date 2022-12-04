import game
import random

MAX, MIN = 10000, -10000

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
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]
rBias = RBias[::-1]

BBias = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
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
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

KBias = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
]
kBias = KBias[::-1]


def pieceVal(board_state):
    total = 0
    for x in enumerate(board_state):
        for y in enumerate(x[1]):
            if y[1] == 'P':
                total += 10 + PBias[x[0]][y[0]]
            elif y[1] == 'p':
                total += -10 + pBias[x[0]][y[0]]
            elif y[1] == 'R':
                total += 50 + RBias[x[0]][y[0]]
            elif y[1] == 'r':
                total += -50 + rBias[x[0]][y[0]]
            elif y[1] == 'N':
                total += 30 + nBias[x[0]][y[0]]
            elif y[1] == 'n':
                total += -30 + nBias[x[0]][y[0]]
            elif y[1] == 'B':
                total += 30 + BBias[x[0]][y[0]]
            elif y[1] == 'b':
                total += -30 + bBias[x[0]][y[0]]
            elif y[1] == 'Q':
                total += 90 + qBias[x[0]][y[0]]
            elif y[1] == 'q':
                total += -90 + qBias[x[0]][y[0]]
            elif y[1] == 'K':
                total += 900 + KBias[x[0]][y[0]]
            elif y[1] == 'k':
                total += -900 + kBias[x[0]][y[0]]
    return total


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
    if i == '8' or i == 'a':
        return 0
    if i == '7' or i == 'b':
        return 1
    if i == '6' or i == 'c':
        return 2
    if i == '5' or i == 'd':
        return 3
    if i == '4' or i == 'e':
        return 4
    if i == '3' or i == 'f':
        return 5
    if i == '2' or i == 'g':
        return 6
    if i == '1' or i == 'h':
        return 7


def createMove(board, board_state, det):
    x = 0
    moves = []
    while (True):
        try:
            moves.append(str(list(board.legal_moves)[x]))
            x += 1
        except:
            break

    if moves == []:
        print("break")
    origPos, origPos2, newPos, newPos2, posActual, nPosActual = [], [], [], [], [], []
    tmp = 0
    for i in moves:
        tmp = convertPos(i[:1])
        origPos.append(tmp)
        tmp = convertPos(i[1:2])
        origPos2.append(tmp)
        tmp = convertPos(i[2:3])
        newPos.append(tmp)
        tmp = convertPos(i[3:4])
        newPos2.append(tmp)
        posActual.append(i[:2])
        nPosActual.append(i[2:])
    p1 = [0]*len(moves)
    i = 0

    createdNode = 0
    while i < len(moves):
        count = 0
        for x in range(createdNode):
            if x != i:
                if p1[x].pos == posActual[i]:
                    (p1[x].nextPos).append(nPosActual[i])
                    (p1[x].x).append(newPos2[i])
                    (p1[x].y).append(newPos[i])
                    count += 1
        if count == 0 or i == 0:
            p1[createdNode] = Piece()
            p1[createdNode].pos = posActual[i]
            (p1[createdNode].nextPos).append(nPosActual[i])
            p1[createdNode].piece = board_state[origPos2[i]][origPos[i]]
            (p1[createdNode].x).append(newPos2[i])
            (p1[createdNode].y).append(newPos[i])
            createdNode += 1
        i += 1
    p1 = list(filter(None, p1))
    if det == 0:
        random.shuffle(p1)
        return p1, createdNode
    elif det == 1:
        return p1


def createTree(board, board_state, depth, alpha, beta):
    p1, createdNode = createMove(board, board_state, 0)
    p1 = createEval(p1, createdNode, board_state)
    if depth == 3:
        if board.turn == False:
            if p1 == []:
                return p1, 900
            lowest = p1[0].eval
            return p1, lowest
        elif board.turn == True:
            if p1 == []:
                return p1, -900
            highest = p1[0].eval
            return p1, highest
    if board.turn == True:
        best = MIN
        for x in range(createdNode):
            for y in range(len(p1[x].x)):
                nboard = game.check_legal((p1[x].pos+p1[x].nextPos[y]), p1[x].pos, p1[x].nextPos[y], p1[x].y[y], p1[x].x[y], board, board_state)
                nboard_state = game.br.board_init(nboard)
                tmp, val = (createTree(nboard, nboard_state, (depth+1), alpha, beta))
                board.pop()
                (p1[x].nodes).append(tmp)
                try:
                    best = max(best, val)
                except:
                    val.append(best)
                    best = max(val)
                alpha = max(alpha,best)

                if beta <= alpha and depth != 0:
                    return p1,best
        if depth != 0:
            return p1, best

    else:
        best = MAX
        for x in range(createdNode):
            for y in range(len(p1[x].x)):
                nboard = game.check_legal((p1[x].pos+p1[x].nextPos[y]), p1[x].pos, p1[x].nextPos[y], p1[x].y[y], p1[x].x[y], board, board_state)
                nboard_state = game.br.board_init(nboard)
                tmp, val = (createTree(nboard, nboard_state, (depth+1), alpha, beta))
                board.pop()
                (p1[x].nodes).append(tmp)
                try:
                    val.append(best)
                    best = min(val)
                except:
                    best = min(best, val)

                beta = min(beta, best)
                if beta <= alpha and depth != 0:
                    return p1,best
        if depth != 0:
            return p1, best
    return p1


def createEval(p1, createdNode, board_state):
    for x in range(createdNode):
        for y in range(len(p1[x].x)):
            p1[x].eval.append(pieceVal(board_state))
    return p1


def searchTree(p1):
    if p1[0].piece == 'p' or p1[0].piece == 'r' or p1[0].piece == 'n' or p1[0].piece == 'b' or p1[0].piece == 'q' or p1[0].piece == 'k':
        try:
            if p1[0].nodes:
                for x in enumerate(p1):
                    for y in enumerate(x[1].nodes):
                        lowest, bestPos, bestNPos = searchTree(y[1])
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
        return lowest, bestPos, bestNPos
    elif p1[0].piece == 'P' or p1[0].piece == 'R' or p1[0].piece == 'N' or p1[0].piece == 'B' or p1[0].piece == 'Q' or p1[0].piece == 'K':
        try:
            if p1[0].nodes:
                for x in enumerate(p1):
                    for y in enumerate(x[1].nodes):
                        highest, bestPos, bestNPos = searchTree(y[1])
                        x[1].eval[y[0]] = highest+x[1].eval[y[0]]
        except:
            print("This try except should fix the error i was having")
        highest = -9999
        for x in p1:
            if highest < max(x.eval):
                highest = max(x.eval)
                bestPos = x.pos
                for y in enumerate(x.eval):
                    if y[1] == highest:
                        bestNPos = x.nextPos[y[0]]
        return highest, bestPos, bestNPos

# created tree of the best moves for ai & randomizes the best move so ai doesnt choice same thing everytime
def getBestMove(self):
    bestMove = self.otherSearchTree(createTree)
    randombestMove = random.choice(bestMove)
    return randombestMove


def AIRunner(board, board_state):
    p1 = createTree(board, board_state, 0, MIN, MAX)
    highest, bestPos, bestNPos = searchTree(p1)
    return bestPos, bestNPos
