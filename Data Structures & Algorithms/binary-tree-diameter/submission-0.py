# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDiameter = 0

        def dfs(node):
            nonlocal maxDiameter
            longest = 0
            if not node.left and not node.right:
                longest = 0
                diam = 0
            elif node.left and not node.right:
                longest = dfs(node.left) + 1
                diam = longest
            elif node.right and not node.left:
                longest = dfs(node.right) + 1
                diam = longest
            else:
                left, right = dfs(node.left) + 1, dfs(node.right) + 1
                diam = left + right
                longest = max(left, right)
            maxDiameter = max(diam, maxDiameter)
            return longest
            
        dfs(root)
        return maxDiameter