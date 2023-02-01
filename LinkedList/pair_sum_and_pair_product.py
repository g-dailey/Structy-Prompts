'''
Pair sum
Write a function, pair_sum, that takes in a list and a target sum as arguments.
The function should return a tuple containing a pair of indices whose elements sum
to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

test_00:
pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)

'''

def pair_sum (list, target):
  result = ()

  for index1, item in enumerate(list):
    for index2, item2 in enumerate(list):
      if item + item2 == target and index1 != index2:
        result = (index2, index1)

  return result

# print(pair_sum([3, 2, 5, 4, 1], 8))

'''

Pair Product
Write a function, pair_product, that takes in a list and a target product as arguments.
The function should return a tuple containing a pair of indices whose elements multiply to the given target.
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

test_00:
pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
'''

def pair_prod (list, target):
  result = ()

  for index1, item in enumerate(list):
    for index2, item2 in enumerate(list):
      if item * item2 == target and index1 != index2:
        result = (index2, index1)

  return result

print(pair_prod([3, 2, 5, 4, 1], 8))