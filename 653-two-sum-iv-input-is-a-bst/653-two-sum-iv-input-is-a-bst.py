# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        global seen
        seen = set()
        
        def helper(node):
            global seen
            if node:
                if k-node.val in seen:
                    return True
                seen.add(node.val)
                if helper(node.left):
                    return True
                if helper(node.right):
                    return True
                return False
                
        
        return helper(root)
                