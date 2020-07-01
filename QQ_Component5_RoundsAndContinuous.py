# Quiz Quest Component 5 Rounds/Continuous system

# To Do
# - Change between rounds and continuous
# - Make sure continuous never ends and rounds ends at the specified amount

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
            if response == 1111:
                return response
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

# Main code here
yes_no_for_string_check = ["yes","no"] # list for string checker
continuous = string_check("Continuous?: ", yes_no_for_string_check) # Checks if answer for continuous is yes or no
# Depending on answer to the question above display appropiate response
if continuous == "no":
    questions_to_ask = intcheck("Amount of questions?: ", 1) # Set the amount of questions user wants to answer
    print("You have chosen to do {} questions".format(questions_to_ask)) # Display the amount of questions they want to answer
else:
    questions_to_ask = 1 # Sets the variable to be used later
    print("you have chosen continuous")# Appropiate feedback

# Loop for amount of questions the user wants to answer or continuously
questions_answered = 0 # stores how many questions the user has answered
while questions_answered < questions_to_ask:
    # If continuous was chosen make sure questions answered never catches up to questions to answer ore else the loop will stop
    if continuous == "yes":
        questions_to_ask += 1
    questions_answered += 1 # adds this question to questions answeres
    print("Question {}".format(questions_answered)) # displays what question the user is on
    user_answer = intcheck("What is your answer?") # Ask user for their answer
    # User enters 1111 then cut out of loop
    if user_answer == 1111:
        questions_answered = questions_to_ask

# A nice farewleel message
print("Thank you for playing")





