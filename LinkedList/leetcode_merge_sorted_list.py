# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(None)
        tail = new_head

        current1 = list1
        current2 = list2

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                new_head = current1
                current1 = current1.next
            else:
                new_head = current2
                current2 = current2.next
            tail = tail.next
        if current1 is not None:
            tail.next = current1
        if current2 is not None:
            tail.next = current2
        return new_head.next
