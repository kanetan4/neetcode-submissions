class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[','}':'{'}
        stack = []
        for char in s:
            if stack and char in hashmap and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False