# Quiz Quest Component 2 - Integer Checker

# To Do
# - Get Integer Input from user
# - Make sure its valid for the given scenario


# Functions go here
def intcheck(question, low = None, high = None):
    valid = False
    # Error messages
    if low is not None and high is not None:  # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None:  # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None:  # Error message if only high variable is given
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
# Loop for testing purposes
loop = True
while loop:
    # What times table would you like to do question
    #times_table_choice = intcheck("Which times table would you like to practice?(1 to 12 times tables): ", 1, 12)
    #print("So you have chosen to do the {} times tables".format(times_table_choice))

    # Users answer to questions
    user_answer = intcheck("What is your answer: ", 1)

    # How many questions the user wants to do
    #amount_of_questions = intcheck("How many questions: ", 1)