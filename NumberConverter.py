# Rikki Weinberger - Assignment 1

from num2words import num2words # imports the num2words module

# function replaces numbers with their string representation
def replace_numbers_with_words(text): # parameter is the user input passed in
    result = "" # stores the final modified string
    temp = "" # temporarily stores digits 

# loops through each character of the input string
    for char in text:
        if char.isdigit(): # if the char is a number
            temp += char  # adds number to temp (can build up multi-digit numbers)
        else:
            if temp: # if temp contains a number
                result += num2words(int(temp))  # converts the number in temp to words and appends it to result
                temp = ""  # resets temp for next number
            result += char  # appends a non-numeric character to result

    if temp: # after loop, if there is leftover in temp (meaning a number was last in the string)
        result += num2words(int(temp))  # converts and appends the last number found to result

    return result # returns the complete string with the numbers changed to words


# takes in user input
user_input = input("Enter a sentence: ")

# passes the user input to the replace_numbers_with_words function, and receives function output
result = replace_numbers_with_words(user_input)

# prints the final string result
print(result)


