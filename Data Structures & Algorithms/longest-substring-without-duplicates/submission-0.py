class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1: return length
        count = {}
        longest = 0
        l, r = 0, 0
        while r < length:
            if s[r] in count and count[s[r]] > 0:
                while count[s[r]] > 0:
                    count[s[l]] -= 1
                    l += 1

            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            longest = max(longest, (r-l+1))

            r += 1
        return longest