class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        length = len(s)

        def expandPalindrome(start: int, end: int):
            count = 0
            while start >= 0 and end < length:
                if s[start] == s[end]:
                    count += 1
                else:
                    break
                start -= 1
                end += 1
            return count

        for index in range(length):
            total += expandPalindrome(index, index)
            total += expandPalindrome(index, index + 1)
        
        return total