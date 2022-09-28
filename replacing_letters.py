newString = []
secret_word = "giraffe"
hidden_word = ""

print(secret_word)
secret_word = list(secret_word)

guess = input("What character would you like to replace? ")
position = ([pos for pos, char in enumerate(secret_word) if char == guess])

#print("You have chosen the letter " + guess + " which is found in position " + str(position))

replace_letter = input("\nEnter the letter that you would like to replace with? ")

if len(position) > 1:
    i = 0
    while i < len(position):
        new_position = int(position[i]) #need to have the position of the integer as 0. The problem is when there is two positions... Then I need to loop through it. Maybe an if statement?
        secret_word[new_position] = replace_letter # list_hidden_word[new_position] = replace_letter
        i = i + 1

else:
    position = int(position[0]) #need to have the position of the integer as 0. The problem is when there is two positions... Then I need to loop through it. Maybe an if statement?
    secret_word[position] = replace_letter # secret_word[position] = replace_letter to just replace the letter in the known word and show it
    
secret_word = "".join(secret_word) # secret_word = "".join(secret_word)

print(secret_word) #change to secret_word if the above statements also show secret_word and then you'll change the individual letters.