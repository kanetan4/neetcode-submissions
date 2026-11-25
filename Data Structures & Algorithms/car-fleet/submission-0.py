class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # contain stack of (pos, speed, time taken to finish)
        temp = []
        for index, pos in enumerate(position):
            temp.append((pos, speed[index], (target-pos)/speed[index]))
        temp.sort()
        for item in temp:
            while stack:
                top = stack[-1]
                if top[2] <= item[2]:
                    stack.pop()
                else:
                    break
            stack.append(item)
        
        return len(stack)