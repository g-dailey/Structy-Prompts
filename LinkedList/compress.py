'''
Compress
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where consecutive occurrences of the same characters are
compressed into the number of occurrences
followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.

'''

string = 'cccaat'
def compress(s):
  result = ''
  i = 0
  j = 0
  count = 1


  while j <= len(s) - 1:
    if j != len(s)-1 and s[j] == s[j + 1]:
      count += 1
      print(s[j+1])
      j += 1
    else:
      if count == 1:
        result += s[j]
      else:

        result +=  str(count) + s[j]
      j += 1
      count = 1
  return result

print(compress(string))