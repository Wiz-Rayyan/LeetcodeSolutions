# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # (prev/None==Null)->(1/curr)->(2)->3->4
        while curr: # until curr !== None
            temp = curr.next # 1->2 stored in first iteration
            curr.next = prev # Null<-1/curr
            prev = curr # prev incremented. Null <- 1/prev
            curr = temp # 2 = curr now
        return prev 
