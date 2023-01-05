'''
Intersection
Write a function, intersection, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

test_00:
intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
'''

def intersection(a, b):
  result = []
  for item in range(len(a)):
    if a[item] in b:
      result.append(a[item])
  return result

print(intersection([4,2,1,6], [3,6,9,2,10]))