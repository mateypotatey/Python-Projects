"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)"""
import random

x = random.sample(range(1,100), 10)
y = random.sample(range(1,100), 15)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []

for element in a:
    for num in b:
        if num == element not in common_list:
            common_list.append(num)


print(common_list)
print()
print(x)
print(y)
print([num for num in y if num in x]) # one liner code. didn't get solution myself.
