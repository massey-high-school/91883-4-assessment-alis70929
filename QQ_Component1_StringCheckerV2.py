# Quiz Quest Component 1 String Checker v1 (Mrs Gottschalks Code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario


# This function was made by Mrs Gottschalk
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



# Main Routine

yes_no_for_string_check = ["yes","no"] # This is a list to enter into the string checker function

# Ask user question and check if answer is yes or no
times_table_all = string_check("Would you like to do all 12 times tables at once?", yes_no_for_string_check)
# Gives Appropiate feedback based on users response
if times_table_all == "yes":
    print("You have chosen to practice all times tables at once")
else:
    print("You have chosen to do a specific times tables")
print()

# Ask user question and check if answer is yes or no
continuous = string_check("Would you like to answer questions continuously?", yes_no_for_string_check)
# Gives Appropiate feedback based on users response
if continuous == "yes":
    print("You have chosen to do questions continuously")
else:
    print("You have chosen to do a specific amount of rounds")
print()


