# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = dict()
        
        if not (head and head.next): return False
        
        curr = head
        
        while curr:
            if curr in cache: return True
            
            cache[curr] = True
            curr = curr.next
            
        return False