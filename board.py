# testing numpy for extracting the board

import chess
import re
import numpy as np

#push
board = chess.Board()
holder = str(board)
print(holder)
temp = re.split("\n| ", holder)
final = np.array(temp).reshape(8, 8).tolist()
print(np.array(temp).reshape(8, 8).tolist())
print(final[7][0])