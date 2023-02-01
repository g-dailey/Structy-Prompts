'''

Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.

test_00:
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

is_univalue_list(a) # True
test_01:
a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

is_univalue_list(a) # False

'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  value = head.val
  current_1 = head.next

  while current_1 is not None:
    if current_1.val != value:
      return False
    current_1 = current_1.next

  return True
