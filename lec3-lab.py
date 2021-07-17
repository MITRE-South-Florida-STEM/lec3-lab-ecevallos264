# 1.
# Manipulate the string variable s to output the correct variations.
s = "6.00 is 6.0001 and 6.0002"

# a. Manipulate s to print out '62'
print(s[6] + s[2])

# b. Manipulate s to print out every other character starting in position 4
print(s[4:len(s):2])

# c. Manipulate s to print out the characters in positions 2 - 10 backwards
print(s[10:2:-1])

# 2.
# Complete this double for loop
s = "mit u rock"


# TODO for loop over the character in the 1st position through the end of the string s
for char1 in s[1:len(s)]:
  # TODO for loop over the character in the 0th position through the second from the last position in the string
  for char2 in s[0:len(s)-1]:
    # TODO Check if char1 comes before char2 in the alphabet
     if ord(s[char1]) < ord(s[char2]):
      # TODO Print out char1 comes first and print the value of char1
      print("char 1 comes first " + s[char1])
#     else:
      # TODO Print out char2 comes first and print the value of char2
      print("char 2 comes first " + s[char2])
# Hint: To get the numeric position of the letter in the alphabet use the ord() function
