class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {} # (i s1, i s2): False, if reach (len(s1), len(s2)) means its True already
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2) != len3: return False

        def dfs(index, position1, position2):
            if (position1, position2) in cache: 
                return cache[(position1, position2)]
            if index == len3:
                return True
            
            left, right = False, False
            if position1 < len1 and s3[index] == s1[position1]:
                left = dfs(index+1, position1+1, position2)
            if position2 < len2 and s3[index] == s2[position2]:
                right = dfs(index+1, position1, position2+1)
            cache[(position1, position2)] = left or right
            return cache[(position1, position2)]

        return dfs(0,0,0)