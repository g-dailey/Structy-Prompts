'''
how high
Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.

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

how_high(a) # -> 2

'''

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def how_high(node, depth=0):

  if node is None:
    return -1

  max_depth = float('-inf')
  max_depth = max(max_depth, depth)

  right_depth = how_high(node.right, depth+1)
  left_depth = how_high(node.left, depth+1)

  return max(max_depth, right_depth, left_depth)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
f.right = g

print(how_high(a, 0))