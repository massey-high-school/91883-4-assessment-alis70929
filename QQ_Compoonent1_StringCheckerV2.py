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
        print("Please enter Yes/No")



# Main Routine

yes_no_for_string_check = ["yes","no"]
times_table_all = string_check("Would you like to do all 12 times tables at once?", yes_no_for_string_check)
if times_table_all == "yes":
    print("You have chosen to practice all times tables at once")
else:
    print("You have chosen to do a specific times tables")
print()
continuous = string_check("Would you like to answer questions continuously?", yes_no_for_string_check)
if continuous == "yes":
    print("You have chosen to do questions continuously")
else:
    print("You have chosen to do a specific amount of rounds")
print()


