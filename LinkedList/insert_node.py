'''
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'x', 2)
# a -> b -> x -> c -> d
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'v', 3)
# a -> b -> c -> v -> d
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):

  new_node = Node(value)
  i = 0
  current = head
  temp = None


  if index == 0:
    temp = Node(value)
    temp.next = head
    return temp

  while current is not None:
    if i != index - 1:
      current = current.next
    else:
      temp = current.next
      current.next = new_node
      new_node.next = temp
    i+=1

  return head