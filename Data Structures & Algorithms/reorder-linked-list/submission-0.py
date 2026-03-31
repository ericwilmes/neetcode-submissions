# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        # reverse second half
        # merge two

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now slow is in the middle, reverse
        print("middle")
        middle = slow

        curr = slow.next
        prev = slow.next = None 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # reversed, now build a new list with combination

        while prev:
            temp1 = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp1

            head = temp1
            prev = temp2

