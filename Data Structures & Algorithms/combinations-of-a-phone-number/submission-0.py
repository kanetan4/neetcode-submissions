class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keymap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []
        length = len(digits)
        if length == 0: return output
        curr = ""

        def dfs(i):
            nonlocal curr
            if i == length:
                output.append(curr)
                return
            number = digits[i]
            for char in keymap[number]:
                curr += char # add char
                dfs(i+1)
                curr = curr[:-1] # remove last char
        dfs(0)
        return output