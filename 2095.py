# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        temp = head
        cnt = 0
        if head is None or head.next is None:
            return None
        while temp is not None:
            cnt+=1
            temp = temp.next
        
        midNode = (cnt//2)
        temp = head
        while temp is not None:
            midNode -= 1
            if midNode == 0:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head
    
    #Optimal Approach
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        fast = fast.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head