# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root == None: return count

        def dfs(root, highest):
            nonlocal count
            if root.val >= highest:
                count += 1
                highest = max(root.val, highest)
            if root.left:
                dfs(root.left, highest)
            if root.right:
                dfs(root.right, highest)
            return

        dfs(root, root.val)
        return count
