# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDepth = 1

        def dfs(node, counter):
            if not node.left and not node.right: 
                return counter
            elif node.left and not node.right:
                return dfs(node.left, counter+1)
            elif node.right and not node.left:
                return dfs(node.right, counter+1)
            else:
                return max(dfs(node.left, counter+1), dfs(node.right, counter+1))

        return dfs(root, maxDepth)