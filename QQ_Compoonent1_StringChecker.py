# Quiz Quest Component 1 String Checker v1 (My code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario

def string_check(question,):

    valid = False
    while valid == False:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes/No")


# Main Routine
times_table_all = string_check("Would you like to do all 12 times tables at once?")
if times_table_all == "yes":
    print("You have chosen to practice all times tables at once")
elif times_table_all == "no":
    print("You have chosen to do a specific times tables")

continuous = string_check("Would you like to answer questions continuously?")
if continuous == "yes":
    print("You have chosen to do questions continuously")
elif continuous == "no":
    print("You have chosen to do a specific amount of rounds")