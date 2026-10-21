class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        length = len(s)

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i):
            if i >= length:
                res.append(part[:])
                return
            for j in range(i, length):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            return
        dfs(0)
        return res