class TreeNode:
    def __init__(self, string):
        self.string = string
        self.nextchar = {} # char: TreeNode
        self.terminal = False 

class PrefixTree:
    def __init__(self):
        self.tree = TreeNode("")

    def insert(self, word: str) -> None:
        curr = self.tree
        for char in word:
            if char not in curr.nextchar:
                curr.nextchar[char] = TreeNode(char)
            curr = curr.nextchar[char]
        curr.terminal = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for char in word:
            if char not in curr.nextchar:
                return False
            else:
                curr = curr.nextchar[char]
        return curr.terminal

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for char in prefix:
            if char not in curr.nextchar:
                return False
            else:
                curr = curr.nextchar[char]
        return True
        