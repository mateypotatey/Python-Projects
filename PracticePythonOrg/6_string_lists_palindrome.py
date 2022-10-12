"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

word = input("Give me a word and I will check if it is a palindrome: ").lower()

reverse_word = []

for x in word:
    reverse_word.insert(0, x)

reverse_word = "".join(reverse_word)

if reverse_word == word:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} is not a palindrome")

#more elegant/shorter solutions from the solutions comments:

str1 = "abba"
print ("palindrome") if str1==str1[::-1] else print("not a palindrome\n")

def palindrome(s):
    return s == s[::-1] #this reverses the list

input_string = input("Enter any string: ")
if palindrome(input_string):
    print("It's a palindrome")
else:
    print("It's not a palindrome")


def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 - i]
    return x


word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
