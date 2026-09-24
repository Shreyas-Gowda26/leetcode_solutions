#Optimal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast = head

        for i in range(n):
            fast = fast.next

        # Removing the head
        if fast is None:
            return head.next

        slow = head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return head
    
