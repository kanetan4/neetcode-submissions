class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        seen = {}
        wordlength = len(word)

        def dfs(i, j, length):
            if (i, j) in seen: return False
            if length == wordlength:
                return True
            seen[(i, j)] = True
            nextchar = word[length]
            result = False
            if i-1 >= 0 and nextchar == board[i-1][j]:
                result = dfs(i-1, j, length+1) or result 
            if i+1 < height and nextchar == board[i+1][j]:
                result = dfs(i+1, j, length+1) or result 
            if j-1 >= 0 and nextchar == board[i][j-1]:
                result = dfs(i, j-1, length+1) or result 
            if j+1 < width and nextchar == board[i][j+1]:
                result = dfs(i, j+1, length+1) or result 
            del seen[(i, j)]
            return result
            

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True
        return False