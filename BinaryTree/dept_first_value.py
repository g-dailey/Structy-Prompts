'''


structy-logo
structy
premium
favorite
depth first values
Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

'''

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
  if root == None:
    return []
  answer = [root.val]
  left = []
  right = []
  if root.right:
    right = depth_first_values(root.right)

  if root.left:
    left =  depth_first_values(root.left)

  return answer + left + right