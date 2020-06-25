# Quiz Quest Component 8 ask user if they want to play again

# To Do
# - Ask user if they want to play again
#  - if yes code loops again
#  - if no then code ends


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
            # If the users response is the first letter of one of the words in to_check
            elif response == item[0]:
                # return the whole word to the main code
                return item
        print("Please enter Yes/No")

yes_no_for_string_check = ["yes", "no"]
keepgoing = "yes"
while keepgoing == "yes":

    keepgoing = string_check("Would you like to play again(Yes or No)",yes_no_for_string_check)
