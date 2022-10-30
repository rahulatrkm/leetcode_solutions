# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global ans
        ans = None
        def helper(node, cnt):
            global ans
            # print(cnt, node.val)
            if node:
                # print(cnt, node.val)
                cnt = helper(node.left, cnt)
                # print(cnt)
                if cnt >= k:
                    return cnt
                else:
                    cnt += 1
                    if cnt == k:
                        ans = node.val
                        # print(ans)
                        return k
                # print(cnt, node.val)
                cnt = helper(node.right, cnt)
            return cnt   
        
        helper(root, 0)
        return ans