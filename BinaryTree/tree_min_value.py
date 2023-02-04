'''
structy-logo
structy
premium
favorite
tree min value
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.

test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
tree_min_value(a) # -> -2

'''

class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def tree_min_value(root):
  answer = root.val

  stack = [root]

  while len(stack) > 0:
    current = stack.pop()
    if current.val < answer:
        answer = current.val
    if current.right:
        stack.append(current.right)
    if current.left:
        stack.append(current.left)
  return answer

a = Node(3)
b = Node(11)
c = Node(float('-inf'))
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_min_value(a))