# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = deque() # Tuples of (Node, level)
        currLength = 0
        queue.append((root, currLength))

        while len(queue) > 0:
            currNode, currHeight = queue.popleft()
            if currLength <= currHeight:
                output.append([currNode.val])
                currLength += 1
            else:
                output[currHeight].append(currNode.val)
            if currNode.left: queue.append((currNode.left, currHeight+1))
            if currNode.right: queue.append((currNode.right, currHeight+1))

        return output