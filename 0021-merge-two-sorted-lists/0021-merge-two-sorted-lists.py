# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()  # Placeholder node
            current = dummy     # Pointer to build the merged list
            
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next  # Move pointer forward

            # Attach remaining nodes (if any)
            current.next = list1 if list1 else list2
            
            return dummy.next  # The actual merged list starts from dummy.next
