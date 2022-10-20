# testing numpy for extracting the board

import chess
from chess.svg import board
import re
import numpy as np


board = chess.Board()
holder = str(board)
print(holder)
temp = re.split("\n| ", holder)
final = np.array(temp).reshape(8, 8).tolist()
print(np.array(temp).reshape(8, 8).tolist())
print(final[7][0])