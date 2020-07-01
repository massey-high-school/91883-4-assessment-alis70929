# Quiz Quest Complete Program v1, Putting Components Together as i go

# To Do
# - Add components to this code, make sure they work together properly
# - Components added
#   - 1, 2, 3, 4, 5, 6, 7, 8, 9.

# Imports are here
import random


# Functions go here
# This function was made by Mrs Gottschalk, It checks if a string is valid for the given list(to_check)
def string_check(question, to_check):
    # Loops until a valid answer is given
    valid = False
    while not valid:
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

# Introduction
print("********* Welcome to the times tables practice program ********* ") # Title
# Asks if they want to read the instructions
introduction = string_check("Would you like to read the instructions(Recommended for first time users)",
                            yes_no_for_string_check)

# If they do want to read the instructions then display the instructions otherwise continue to main code
if introduction == "yes":
    print()
    print("Instructions \n"
          "- You can chose the range of numbers of each side of the question \n"
          "- If you want to do one times table put the lowest and highest of one side of the equation as the same number\n"
          "- You can chose to answer questions continuously or set a certain amount of questions you want to answer \n"
          "- You then have to answer questions until you answer all the questions given or if you enter the exit code(1111)")
    print()
    # Stops the rest of the code appearing so that the user can read the instructions
    input("Press <enter> to continue")

# Loops code until the user dosent want to play again
keepgoing = "yes"
while keepgoing == "yes":
    # Stores results of each round so it can be displayed at the end
    questions = []  # Stores each question
    actual_answers = []  # Stores the correct answer of each question
    users_answers = []  # Stores the users answers
    correct_incorrect = []  # Stores if they were correct or incorrect

    print()

    # Ask user the range of each number in the question
    print("What range of numbers would you like the left number in the question to be")
    low1 = intcheck("Lowest possible number:",1)
    high1 = intcheck("Highest possible number:",low1)
    print()
    print("What range of numbers would you like the right number in the question to be")
    low2 = intcheck("Lowest possible number:", 1)
    high2 = intcheck("Highest possible number:", low2)

    # Ask user wheher they want to answer questions continuously or a specific amount
    print()
    continuous = string_check("Would you like to answer questions continuously?:", yes_no_for_string_check)
    if continuous == "no":
        questions_to_ask = intcheck("Then how many questions do you want to answer: ", 1)  # Here the user chooses a specific amount of questions
        # Display how many questions the user chose
        print("You have chosen to do {} questions".format(questions_to_ask))
    else:
        questions_to_ask = 1  # Sets up the variable questions to ask for later use
        print("you have chosen continuous")  # Display to user that they have chosen continuous

    # Tells the user that they can exit at any point using the exit code

    qq_statement("!!! At any time when you are answering questions you can put in 1111 instead of an answer to immediately exit. !!!", "!")

    input("Press <enter> to continue")
    questions_answered = 0  # Reset questions answered to 0
    # Loops questions until user has answered the amount of questions chosen
    while questions_answered < questions_to_ask:
        # If user chose continuous make it so questions answered will never catch up to questions asked
        if continuous == "yes":
            questions_to_ask += 1  # Adds one to questions to ask so that the questions loop continuously

        # count how many questions the user has answerd
        questions_answered += 1

        # Says what question the user is on
        qq_statement("### Question {} ###".format(questions_answered), "#")

        # Ssts number in the equations
        num1 = random.randint(low1,high1)  # The first number in the equation randomly generated
        num2 = random.randint(low2, high2)  # The second number in the equation

        # Calculating the answer to the generated question
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
            qq_statement("| You got it right, Good Job |", "-")  # Congratulation for getting it right
            correct_incorrect.append("Correct")  # Stores that the user was correct for this question
        else:
            # Telling them the right answer because they got it wrong
            qq_statement("XXX You got it wrong the right answer is {} XXX".format(actual_answer), "X")
            correct_incorrect.append("Incorrect")  # Stores that the user was incorrect for this question

    # The summary of the users performance
    listcount = 0  # to figure out what question the summary needs to print
    print("Question  #|Question |Users Answer|Correct Answer|Correct?  |")  # Prints the top of the table

    # Creates a summary table
    for item in correct_incorrect:
        # Creates a row that is evenly spaced and has the question number, the question,
        # the users answer for that question, the actual answer and if the user was correct or incorrect
        print("Question {1:>{0}}| {3:<{2}} | {5:<{4}} | {7:<{6}} |{9:<{8}}|".format(2, listcount + 1,
                                                                                    7, questions[listcount],
                                                                                    10, users_answers[listcount],
                                                                                    12, actual_answers[listcount],
                                                                                    10, correct_incorrect[listcount]))
        listcount += 1  # Make it so the next question summary row is printed

    print() # Makes a nice space between the table and the summary statistics
    # Summary Statistics
    print("{}/{} questions were answered incorrectly".format(correct_incorrect.count("Incorrect"), len(correct_incorrect)))
    print("{}/{} questions were answered correctly".format(correct_incorrect.count("Correct"),len(correct_incorrect)))

    # Give them nice feedback if they get it all correct
    if correct_incorrect.count("Correct") == len(correct_incorrect):
        qq_statement("!!! Well Done, You answered all the questions correctly !!!","!")

    print()
    # ask user if they want to use the program again
    keepgoing = string_check("Would you like to play again(Yes or No)", yes_no_for_string_check)

print("Thank you for using the program")
