"""The first program of the Udemy Python Mega Course.
Just a re-cap of the lessons so far with lists, for loops, while loops and string modifiers"""

my_list = []

def sentence_maker():
    while True:
        statement = input("Say something: ")
        if statement == "\end":
            break
        else:
            if statement[-1] == "." or statement[-1] == "!" or statement[-1] == "?":
                my_list.append(statement.capitalize())
            elif statement.lower().startswith(("why", "how", "when", "what", "does", "do", "would", "is")):
                my_list.append(statement.capitalize() + "?")
            else:
                my_list.append(statement.capitalize() + ".")
    
    print(" ".join(my_list))

sentence_maker()