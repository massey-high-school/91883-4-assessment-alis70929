# Quiz Quest Complete Program, Putting Components Together as i go

# To Do
# - Add components to this code, make sure they work together properly
# - Components added
#   - 1, 2, 3

# Imports are here
import random

# Functions go here
# This function was made by Mrs Gottschalk, It checks if a string is valid for the given list(to_check)
def string_check(question, to_check):
    # Loops until a valid answer is given
    valid = False
    while valid == False:
        # Asks question
        response = input(question).lower()

        for item in to_check:
            # If the users  response is in the list given(to_check)
            if response == item:
                # return the response to the main code
                return response
            # If the users response is the first letter of one of the items in to_check
            elif response == item[0]:
                # return the whole word to the main code
                return item
        print("Please enter Yes/No")


# This function checks if an integer input is valid for the scenario given
def intcheck(question, low=None, high=None):
    valid = False
    # Error messages
    if low is not None and high is not None:  # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low, high)
    elif low is not None and high is None:  # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None:  # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else:  # Error message if no variables are given
        error = "please enter a whole number"

    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error)  # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error)  # If it is too high print error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()

# Main code goes here

# This is the a list for the string checker
yes_no_for_string_check = ["yes", "no"]

# Ask user which times table they would like to practice ( all 12 or a specific one)
all_or_specific = string_check("All Times tables?:", yes_no_for_string_check)
if all_or_specific == "no":
    specific_times_table = intcheck("Which Times Table?:", 1, 12) # Here the user chooses a specific times table

# Gap for rounds loop
# Sets the first number in the equation
if all_or_specific == "no":
    num1 = specific_times_table # The first number in the equation will be the chosen times table if the user chose to do so
else:
    num1 = random.randint(1, 12) # Random if the user chose to do all 12 at once

num2 = random.randint(1,12) # The second number in the equation will always be random

# Calclulating the answer to the generated question
actual_answer = num1 * num2

# Display Question and Answer
print("{} x {} = {}".format(num1, num2, actual_answer))

