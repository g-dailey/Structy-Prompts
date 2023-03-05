'''
breadth first values
Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

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

breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

'''



from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def breadth_first_value(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values

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

print(breadth_first_value(a))








# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.right = None
#         self.left = None

# def breadth_first_value(root):
#     if not root:
#         return []

#     queue = [root]
#     values = []

#     while queue:
#         item = queue[0]
#         values.append(item.val)

#         if item.left:
#             queue.append(item.left)
#         if item.right:
#             queue.append(item.right)
#         queue = queue[1:]
#     return values



# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# print(breadth_first_value(a))













# # class Node:
# #   def __init__(self, val):
# #     self.val = val
# #     self.left = None
# #     self.right = None

# # def breadth_first_values(root):

# #   if root == None:
#   #   return []
#   # queue = [root]
#   # answer = []

#   # while len(queue) > 0:
#   #   first_item = queue[0]
#   #   if first_item.left:
#   #     queue.append(first_item.left)

#   #   if first_item.right:
#   # #     queue.append(first_item.right)
#   # #   answer.append(first_item.val)
#   #   queue = queue[1:]
#   # print(answer)

#   # return answer