# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        head = prev
        beg = ListNode()
        beg.next = head
        prev = beg
        for i in range(n-1):
            temp = head.next
            if temp is None:
                prev.next = None
                break
            prev = head
            head = temp

        if head:
            prev.next = head.next

        # reverse again
        prev = None
        head = beg.next
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev