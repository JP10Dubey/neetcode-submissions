import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_np = np.array(board)
        boardT=board_np.T
        boardT.tolist()
        for row in range(9):
            numbers = [i for i in board[row] if i != "."]
            if len(numbers) != len(set(numbers)):
                return False
            numbersT = [i for i in boardT[row] if i != "."]
            if len(numbersT) != len(set(numbersT)):
                return False
        newboard = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                newboard[i//3][j//3].append(board[i][j])
        for row in range(3):
            for col in range(3):
                numbersNew = [i for i in newboard[row][col] if i != "."]
                if len(numbersNew) != len(set(numbersNew)):
                    return False
        return True