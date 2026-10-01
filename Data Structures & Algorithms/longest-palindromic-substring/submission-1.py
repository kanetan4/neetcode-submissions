class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlength = 1
        longest = s[0]
        length = len(s)

        # expansion helper function
        def expand(start: int, end: int):
            while start >= 0 and end < length:
                if s[start] != s[end]:
                    break
                start -= 1
                end += 1
            if end - start == 1:
                return (0, "")
            return (end - start - 1, s[start+1:end])

        for index, char in enumerate(s):
            length1, substring1 = expand(index, index)
            if length1 > strlength:
                strlength = length1
                longest = substring1
            length2, substring2 = expand(index, index + 1)
            if length2 > strlength:
                strlength = length2
                longest = substring2
        return longest