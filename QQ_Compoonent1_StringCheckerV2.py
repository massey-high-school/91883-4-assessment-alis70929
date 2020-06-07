# Quiz Quest Component 1 String Checker v1 (Mrs Gottschalks Code)

# To Do
# - Get string input from user
# - Check if it is valid in the given scenario

def StringCheck(question,):

    valid = False
    while valid == False:
        response = input(question)

        if response.lower() == "yes" or response.lower() == "y":
            return "yes"
        elif response.lower() == "no" or response.lower() == "n":
            return "no"
        else:
            print("Please enter Yes/No")


