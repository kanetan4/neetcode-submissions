class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical, box = [], []
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in seen: return False
                seen.add(board[i][j])
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".": continue
                if board[j][i] in seen: return False
                seen.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] == ".": continue
                        if board[x][y] in seen: return False
                        seen.add(board[x][y])

        return True
