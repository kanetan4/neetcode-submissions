class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        u, d = n-1, n

        def dfs(string):
            nonlocal u, d
            if u == 0 and d == 0:
                output.append(string)
                return
            else:
                if u > 0:
                    u -= 1
                    dfs(string + "(")
                    u += 1
                if d > u:
                    d -= 1
                    dfs(string + ")")
                    d += 1
            return
        dfs("(")
        return output