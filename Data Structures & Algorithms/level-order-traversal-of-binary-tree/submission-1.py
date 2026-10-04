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
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                currNode = queue.popleft()
                level.append(currNode.val)
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)
            output.append(level)

        return output