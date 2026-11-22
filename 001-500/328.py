#Brute Force approach


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        temp = head
        arr = []
        while temp is not None and temp.next is not None:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        temp = head.next
        while temp is not None and temp.next is not None:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)

        i = 0
        temp = head
        while temp is not None :
            temp.val = arr[i]
            i+=1
            temp = temp.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        odd = head
        even = head.next
        evenH = head.next
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        odd.next = evenH
        return head