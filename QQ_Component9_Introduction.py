# Quiz Quest Component 9 Introduction

# To Do
# - Ask user if they would like to read the instructions
#  - if not print introduction
#  - if yes then go straight to the bulk of the code

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


yes_no_for_string_check = ["yes","no"] # List for string checker
print("********* Welcome to the times tables practice program ********* ") # Nice title/welcome displayed
# Ask the user if they want to read instructions
introduction = string_check("Would you like to read the instructions(Recommended for first time users)",
                            yes_no_for_string_check)
# If answer is yes then display introduction if not then continue on with the main code
if introduction == "yes":
    print()
    print("Instructions \n"
          "- You can chose the range of numbers of each side of the question \n"
          "- If you want to do one times tables put the lowest and highest of one side of the equation as the same number\n"
          "- You can chose to answer questions continuously or set a certain amount of questions you want to answer \n"
          "- You then have to answer questions until you answer all the questions given or if you enter the exit code(1111)")
    print()
    # Stops the rest of the code appearing so that the user can read the instructions
    input("Press <enter> to continue")