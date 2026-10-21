class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        length = len(s)

        def expandPalindrome(start: int, end: int):
            nonlocal total
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    total += 1
                else:
                    break
                start -= 1
                end += 1
            return

        for index in range(length):
            expandPalindrome(index, index)
            expandPalindrome(index, index + 1)
        
        return total