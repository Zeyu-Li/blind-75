# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast and slow pointer
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # test edge case
        for _ in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
            
            
        left.next = left.next.next
            
        return dummy.next