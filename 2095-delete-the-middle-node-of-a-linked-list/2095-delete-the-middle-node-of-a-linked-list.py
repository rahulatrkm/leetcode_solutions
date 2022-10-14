# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return 
        if not head.next.next:
            head.next = None
            return head
        slow, fast = head, head
        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next
        # print(slow.val)
        if slow.next:
            slow.val = slow.next.val
        if slow.next:
            slow.next = slow.next.next
        
        return head