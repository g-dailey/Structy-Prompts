'''

structy-logo
structy
premium
favorite
tree includes
Write a function, tree_includes, that takes in the root of a binary tree and a target value.
The function should return a boolean indicating whether or not the value is contained in the tree.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

tree_includes(a, "e") # -> True

'''

class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def tree_includes(root, target):
  if root is None:
      return False
  if root.val == target:
      return True
  stack = [root]

  while len(stack) > 0:
      current = stack.pop()
      if current.val == target:
          return True
          break
      if current.right:
          stack.append(current.right)
      if current.left:
          stack.append(current.left)

  return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_includes(a, "a"))