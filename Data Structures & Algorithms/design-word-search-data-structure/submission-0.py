class TreeNode:
    def __init__(self, char):
        self.char = char
        self.nextchar = {}
        self.isTerminal = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.nextchar:
                curr.nextchar[char] = TreeNode(char)
            curr = curr.nextchar[char]
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        length = len(word)
        # i is index of the word, stop when reach end, if reach end succeed, root is node its searching
        def dfs(i, root):
            if i == length:
                return root.isTerminal
            if word[i] in root.nextchar:
                return dfs(i+1, root.nextchar[word[i]])
            elif word[i] == ".":
                result = False
                for char, treenode in root.nextchar.items():
                    result = result or dfs(i+1, treenode)
                return result
            else:
                return False

        return dfs(0, self.root)
        
