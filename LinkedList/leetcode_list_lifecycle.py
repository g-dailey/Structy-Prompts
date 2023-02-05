# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        answer = {}
        index = 0

        while current is not None:
            if current.val not in answer.keys():
                answer[current.val] = 1
                index +=1
                current = current.next
            else:
                return True
                break
        return False