# Quiz Quest Complete Program v1, Putting Components Together as i go

# To Do
# - Add components to this code, make sure they work together properly
# - Components added
#   - 1, 2, 3, 4, 5, 6, 7

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
            # If response is the exit code return the exit code to main code
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

# This function is used to add borders to statements and space them out evenly
def qq_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


# Main code goes here

# This is the a list for the string checker
yes_no_for_string_check = ["yes", "no"]

# Stores results of each round so it can be displayed at the end
questions = [] # Stores each question
actual_answers = [] # Stores the correct answer of each question
users_answers = [] # Stores the users answers
correct_incorrect = [] # Stores if they were correct or incorrect

# Ask user which times table they would like to practice ( all 12 or a specific one)
all_or_specific = string_check("All Times tables?:", yes_no_for_string_check)
if all_or_specific == "no":
    specific_times_table = intcheck("Which Times Table?:", 1, 12)  # Here the user chooses a specific times table
    print("You have chosen to do the {} times tables".format(specific_times_table)) # Displays which times table they chose
else:
    print("You have chosen to do all times tables") # Displays if they have chosen all times table

# Ask user wheher they want to answer questions continuously or a specific amount
continuous = string_check("Continuous?: ", yes_no_for_string_check)
if continuous == "no":
    questions_to_ask = intcheck("Amount of questions?: ", 1)  # Here the user chooses a specific amount of questions
    print("You have chosen to do {} questions".format(questions_to_ask))  # Display how many questions the user chose
else:
    questions_to_ask = 1  # Sets up the variable questions to ask for later use
    print("you have chosen continuous")  # Dipslay to user taht they have chosen continuous

questions_answered = 0 # Reset questions answered to 0
# Loops questions until user has answered the amount of questions chosen
while questions_answered < questions_to_ask:
    # If user chose continuous amke it so questions answered will never catch up to questions asked
    if continuous == "yes":
        questions_to_ask += 1 # Adds one to questions to ask so that the questions loop continuously

    # count how many questions the user has answerd
    questions_answered += 1

    # Says what question the user is on
    qq_statement("### Question {} ###".format(questions_answered), "#")
    # Sets the first number in the equation
    if all_or_specific == "no":
        num1 = specific_times_table # The first number in the equation will be the chosen times table if the user chose to do so
    else:
        num1 = random.randint(1, 12) # Random between 1 -12 if the user chose to do all 12 at once

    num2 = random.randint(1,12) # The second number in the equation will always be random between 1 - 12

    # Calclulating the answer to the generated question
    actual_answer = num1 * num2
    # Stores actual answer for this question
    actual_answers.append(actual_answer)

    # Display Question
    print("{} x {} = ?".format(num1, num2))
    # Stores the question
    questions.append("{} x {}".format(num1, num2))

    # Ask user for their answer
    user_answer = intcheck("What is the answer?:", 1)
    # Stores users answer for this question
    users_answers.append(user_answer)

    # If exit code is entered change the conditions so the loop ends
    if user_answer == 1111:
        questions_answered = questions_to_ask
    # If user gets it right congratulate them, if not tell them right answer
    elif user_answer == actual_answer:
        qq_statement("| You got it right, Good Job |", "-") # Congratulation for getting it right
        correct_incorrect.append("Correct") # Stores that the user was correct for this question
    else:
        qq_statement("XXX You got it wrong the right answer is {} XXX".format(actual_answer), "X")# Telling them the right answer because they got it wrong
        correct_incorrect.append("Incorrect") # Stores that the user was incorrect for this question

# The summary of the users performance
listcount = 0  # to figure out what question the summary needs to print
print("Question  #|Question |Users Answer|Correct Answer|Correct?  |")  # Prints the top of the table

# Creates a summary table
for item in correct_incorrect:
    # Creates a row that is evenly spaced and has the question number, the question, the users answer for that question, the actual answer and if the user was correct or incorrect
    print("Question {1:<{0}}| {3:<{2}} | {5:<{4}} | {7:<{6}} |{9:<{8}}|".format(2,listcount + 1 , 7 ,questions[listcount] ,10 ,users_answers[listcount],12, actual_answers[listcount],10, correct_incorrect[listcount]))
    listcount += 1 # Make it so the next question summary row is printed

