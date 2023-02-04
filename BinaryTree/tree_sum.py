'''
tree sum
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

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

tree_sum(a) # -> 21

'''

class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def tree_sum(root):
  if root == None:
      return 0

  stack = [root]
  answer = 0

  while len(stack) > 0:
      last_item = stack.pop()
      answer += last_item.val
      if last_item.right:
          stack.append(last_item.right)
      if last_item.left:
          stack.append(last_item.left)
  return answer

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

print(tree_sum(a))





