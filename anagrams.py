'''
Anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean
indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

test_00:
anagrams('restful', 'fluster') # -> True

'''

def anagrams (s1, s2):

  obj1 = {}
  obj2 = {}


  if len(s1) != len(s2):
    return False

  for letter1 in s1:
    if letter1 not in obj1.keys():
      obj1[letter1] = 1
    else:
      obj1[letter1] += 1

  for letter2 in s2:
    if letter2 not in obj2.keys():
      obj2[letter2] = 1
    else:
      obj2[letter2] += 1

  if obj1 == obj2:
    return True
  else: return False


print(anagrams('restful', 'fluster'))