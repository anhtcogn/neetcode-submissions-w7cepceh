# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         max_depth = 0
#         stack = [[root, 1]]
#         while stack:
#             node, depth = stack.pop()
#             if node:
#                 max_depth = max(max_depth, depth)
#                 stack.append([node.left, 1 + depth])
#                 stack.append([node.right, 1 + depth])
        
#         return max_depth



# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         q = deque()
#         if root:
#             q.append(root)
        
#         level = 0
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
        
#         return level

        

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)