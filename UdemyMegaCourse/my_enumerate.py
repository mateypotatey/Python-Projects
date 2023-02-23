"""Writing my own enumerate function to get the index position of a given number/letter/value in a list"""

while True:

    student_grades = [9.1, 8.8, 7.5, 7.3, 9.2, 9.1, 8.8, 9.1, 9.1, 7.5]

    print(student_grades)
    all_indices = []

    search = float(input("Which value would you like to search for? "))
    
    # need to copy it so I don't modify the original
    copied_grades = student_grades

    # make sure the number is in the list
    if search in student_grades:

        # loop through each value in the list
        for grade in copied_grades:
            if search == grade:
                # identify and copy out the given index of the match
                list_index = copied_grades.index(search)
                all_indices.append(list_index)

                # over-write the copied-list (excl already indexed positions) 
                copied_grades[list_index] = None
                
    else:
        print("Value not found.")

    
    print(all_indices)


