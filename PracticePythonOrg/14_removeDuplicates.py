"""Write a program (function!) that takes a list and returns a new list that contains all the elements of
the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""

list = ["apples", "oranges", "bananas", "apples", "blueberries", "oranges", "pineapple"]

new_set = set(list)
print(new_set)

def remove_duplicates(list):
    non_dupe_list = []
    for word in list:
        if word not in non_dupe_list:
            non_dupe_list.append(word)
    return non_dupe_list

print(remove_duplicates(list))
