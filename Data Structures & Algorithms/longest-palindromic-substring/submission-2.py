class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlength = 1
        longest = s[0]
        length = len(s)

        def expand(i, j): # returns strlength and string
            while i >= 0 and j < length:
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return (j-i-1, s[i+1:j])

        for i in range(length):
            strlen1, str1 = expand(i, i)
            if strlen1 > strlength:
                strlength = strlen1
                longest = str1
            strlen2, str2 = expand(i, i+1)
            if strlen2 > strlength:
                strlength = strlen2
                longest = str2
        return longest