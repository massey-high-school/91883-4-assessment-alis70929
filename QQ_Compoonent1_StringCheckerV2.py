# Quiz Quest Component 1 String Checker v1 (Mrs Gottschalks Code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario


# This function was made by Mrs Gottschalk
def string_check(question, to_check):

    valid = False
    while valid == False:
        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item




# Main Routine

yes_no_for_string_check = ["yes","no"]


