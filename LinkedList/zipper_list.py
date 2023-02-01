'''
Zipper lists
Write a function, zipper_lists, that takes in the head of two linked lists as arguments.

The function should zipper the two lists together into single linked list by alternating nodes.
If one of the linked lists is longer than the other, the resulting list should terminate with the
remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z
'''
def zipper_lists(head1, head2):
  current1 = head1
  current2 = head2

  while current1 is not None or current2 is not None:
    next = current1.next
    current1.next = current2
    current2 = next
