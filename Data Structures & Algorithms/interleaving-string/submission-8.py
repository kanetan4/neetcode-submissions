class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l, r = 0, 0
        cache = {} # (l, r): False if exist dont need to explore
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if (l1 + l2) != l3: return False

        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            if l == l1 and r == l2:
                return True
            total = l + r

            left, right = False, False
            if l < l1 and s3[total] == s1[l]:
                left = dfs(l+1, r)
            if r < l2 and s3[total] == s2[r]:
                right = dfs(l, r+1)
            cache[(l, r)] = left or right

            return cache[(l, r)]


        return dfs(l, r)