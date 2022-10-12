"""Create a program that asks the user for a number and then prints out a list of all
the divisors of that number. (If you don’t know what a divisor is, it is a number that
divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

num = int(input("Please give me a number and I will tell you what numbers it is divisible by: "))

divisor_list = []

for i in range(1,num +1):
    if num % i == 0:
        divisor_list.append(i)

print(divisor_list)

print([i for i in range(1, num + 1) if num % i == 0]) # list comprehension method instead

# test code because I couldn't get the code working until realising I had numbers in wrong % order
# list_num = []
# for i in range(10):
#     if i % 2 == 0:
#         list_num.append(i)
#         print(i)
#
# print(list_num)