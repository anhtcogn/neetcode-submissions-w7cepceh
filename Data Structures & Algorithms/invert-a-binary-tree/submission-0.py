# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            val = stack.pop()
            val.left, val.right = val.right, val.left

            if val.left:
                stack.append(val.left)
            if val.right:
                stack.append(val.right)
        return root