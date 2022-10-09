# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        nums.sort()
        ans = None
        curr = None
        for num in nums:
            if not curr:
                curr = ListNode(num)
                ans = curr
            else:
                curr.next = ListNode(num)
                curr = curr.next
        return ans