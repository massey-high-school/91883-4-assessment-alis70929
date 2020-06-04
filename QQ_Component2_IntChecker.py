# Quiz Quest Component 2 - Integer Checker

# To Do
# - Get Integer Input from user
# - Make sure its valid for the given scenario

#Functions go here
def intcheck(low = None,high = None, errormessage):
    valid = False
    # Error messages
    if low is not None and high is not None: # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None: # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None: # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else: # Error message if no variables are given
        error = "please enter a whole number"


    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error) # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error) # If it is too high print error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()


# Main code goes here

# Loop What times table would you like to do question until user gives a valid answer
times_tables_choice_valid = False
while times_tables_choice_valid == False:
    times_tables_choice = input("Which times table up to 12 would you like to practice or would you like to practice all of them together")
    if times_tables_choice.lower() == "all" or times_tables_choice.lower() == "a":
        print("You have chosen ")