# Quiz Quest  statement  generator

# To Do
# - Ctrl C the code from higher lower, change it to fit qui quest


# Functions go here
# gives statements a border of selected character
def qq_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()


# Main Code here
qq_statement("| You got it right, Good Job |", "-")  # Correct feedback statement

qq_statement("XXX You got it wrong the right answer is 27 XXX", "X")  # Incorrect feedback statement

qq_statement("### Question 1 ###", "#") # Question statement

