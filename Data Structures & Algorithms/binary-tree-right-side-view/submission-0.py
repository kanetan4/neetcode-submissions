# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        output = []
        if root == None: return output
        queue.append(root)

        while queue:
            length = len(queue)
            for i in range(length): # go level by level
                node = queue.popleft()
                if i == length - 1:
                    output.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return output