class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        stack = []
        for value in tokens:
            if is_int(value):
                stack.append(int(value))
            else:
                value2 = stack.pop()
                value1 = stack.pop()
                if value == "+": stack.append(value1 + value2)
                elif value == "-": stack.append(value1 - value2)
                elif value == "*": stack.append(value1 * value2)
                elif value == "/": stack.append(int(value1 / value2))
        return stack[-1]