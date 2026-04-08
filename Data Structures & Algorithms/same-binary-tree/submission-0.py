# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dp = deque([p])
        dq = deque([q])

        while dp and dq:
            for _ in range(len(dp)):
                nodep = dp.popleft()
                nodeq = dq.popleft()

                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False
                    
                dp.append(nodep.left)
                dp.append(nodep.right)
                dq.append(nodeq.left)
                dq.append(nodeq.right)
        
        return True

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         stack = [(p, q)]

#         while stack:
#             nodep, nodeq = stack.pop()
#             if not nodep and not nodeq:
#                 continue
#             if not nodep or not nodeq or nodep.val != nodeq.val:
#                 return False
#             stack.append((nodep.left, nodeq.left))
#             stack.append((nodep.right, nodeq.right))
        
#         return True


# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
        
#         if not p or not q or p.val != q.val:
#             return False

#         return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
