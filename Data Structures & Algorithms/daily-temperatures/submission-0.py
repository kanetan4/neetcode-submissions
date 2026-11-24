class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        output = [0] * length
        for index, temp in enumerate(temperatures):
            while stack:
                if temp > temperatures[stack[-1]]:
                    top = stack.pop()
                    output[top] = index - top
                else:
                    break
            stack.append(index)
        return output