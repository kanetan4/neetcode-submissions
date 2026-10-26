class TreeNode:
    def __init__(self, char):
        self.char = char
        self.isTerminal = False
        self.nextChar = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # start by creating prefix tree
        root = TreeNode("")
        for word in words:
            curr = root
            for char in word:
                if char not in curr.nextChar:
                    curr.nextChar[char] = TreeNode(char)
                curr = curr.nextChar[char]
            curr.isTerminal = True
        
        # next run through each cell and use DFS + caching to find words
        visited = set() # set
        output = set()
        height, width = len(board), len(board[0])

        def dfs(i, j, root, word):
            nonlocal output
            if i < 0 or i == height or j < 0 or j == width or board[i][j] not in root.nextChar or (i,j) in visited:
                return

            node = root.nextChar[board[i][j]]
            word = word + board[i][j]  
            if node.isTerminal:
                output.add(word)
            visited.add((i, j))
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(i+dx, j+dy, node, word)
            visited.remove((i,j))
            return

        for i in range(height):
            for j in range(width):
                if (i, j) not in visited:
                    dfs(i, j, root, "")
        return list(output)
