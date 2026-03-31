# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_l_s = ListNode()
        new_l = new_l_s
        remainder = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            new_val = val1 + val2 + remainder
            remainder = 0

            if new_val >= 10:
                remainder = 1
                new_val -= 10
                
            new_l.next = ListNode(new_val)
            new_l = new_l.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if remainder:
            new_l.next = ListNode(1)

        return new_l_s.next
            
