# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = l = ListNode()

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next

            else:
                l.next = l2
                l2 = l2.next
            l = l.next

        if l1:
            l.next = l1
            l = l.next
            l1 = l1.next
        if l2:
            l.next = l2
            l = l.next
            l2 = l2.next

        return head.next



        