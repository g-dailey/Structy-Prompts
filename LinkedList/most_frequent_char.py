'''
Most frequent char
Write a function, most_frequent_char, that takes in a string as an argument.
The function should return the most frequent character of the string.
If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

test_00:
most_frequent_char('bookeepr') # -> 'e'

'''

def most_freq_char(s):
  result = {}
  num = 0
  the_char = ''

  for letter in s:
    if letter not in result.keys():
      result[letter] = 1
    else: result[letter] += 1

  for key, value in result.items():
    if value == num:
      continue
    elif value > num:
      num = value
      the_char = key

  return the_char

print(most_freq_char('bookeeper'))