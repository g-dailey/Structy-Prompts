'''
Sum list
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
The function should return the total sum of all values in the linked list.

test_00:
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19
test_01:
x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

sum_list(x) # 42
'''

def sum_list(head):
  current = head
  result = 0

  while current is not None:
    result += current.val
    current = current.next

  return result
