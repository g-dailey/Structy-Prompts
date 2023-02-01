'''

Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

Say we wanted to compute 621 + 354 normally. The sum is 975:

   621
 + 354
 -----
   975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
 --------------
    5 -> 7 -> 9
test_00:
#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

add_lists(a1, b1)
# 5 -> 7 -> 9

'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  values_1= ''
  current_1 = head_1

  values_2 = ''
  current_2 = head_2

  while current_1 is not None:
    values_1 = str(current_1.val) + values_1
    current_1 = current_1.next

  while current_2 is not None:
    values_2 = str(current_2.val) + values_2
    current_2 = current_2.next

  sum_str = str(int(values_1) + int(values_2))
  new_nodes = ''
  for item in sum_str:
    new_nodes = item + new_nodes

  new_head = None
  current = None

  for node in new_nodes:
    if new_head == None:
      new_head = Node(int(node))
      current = new_head
    else:
      current.next = Node(int(node))
      current = current.next
  return new_head
