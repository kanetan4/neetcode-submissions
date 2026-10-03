# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        def dfs(root):
            if not root.left and not root.right: return
            elif root.left and not root.right:
                dfs(root.left)
                root.right = root.left
                root.left = None
            elif root.right and not root.left:
                dfs(root.right)
                root.left = root.right
                root.right = None
            else:
                dfs(root.left)
                dfs(root.right)
                temp = root.right
                root.right = root.left
                root.left = temp
            return
        dfs(root)
        return root