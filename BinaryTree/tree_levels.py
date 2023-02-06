'''
tree levels
Write a function, tree_levels, that takes in the root of a binary tree.
 The function should return a 2-Dimensional list where each sublist represents a level of the tree.

test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]

'''

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
from collections import deque
def tree_levels(root):
  if root is None:
    return []

  if root.right is None and root.left is None:
    return [[root.val]]

  right_edge = tree_levels(root.right)
  for r_edge in right_edge:
    return [root.val, *r_edge]
  left_edge = tree_levels(root.left)
  for l_edge in left_edge:
    return [root.val, *l_edge]

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_levels(a))