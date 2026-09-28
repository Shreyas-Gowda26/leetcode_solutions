# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp = head
        cnt = 0
        while temp is not None:
            cnt+=1
            temp = temp.next
        
        midNode = (cnt//2)+1
        temp = head
        while temp is not None:
            midNode -= 1
            if midNode == 0:
                break
            temp = temp.next
        return temp
    
#Optimal Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow