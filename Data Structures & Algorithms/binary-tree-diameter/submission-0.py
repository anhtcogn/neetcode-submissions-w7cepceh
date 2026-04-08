# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def height(curr):
            if not curr:
                return 0
            
            left_height = height(curr.left)
            right_height = height(curr.right)
            self.res = max(self.res, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        height(root)
        return self.res
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         leftHeight = self.maxHeight(root.left)
#         rightHeight = self.maxHeight(root.right)
#         diameter = leftHeight + rightHeight
#         sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
#         return max(diameter, sub)

#     def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))