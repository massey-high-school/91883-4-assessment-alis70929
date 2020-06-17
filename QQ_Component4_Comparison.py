# Quiz Quest Component 4 Comparing Users answer to the actual answer

# To Do
# - Compare users answer to actual answer, Give appropiate feedback
#  - If the user gets it right congratulate them
#  - If they get it wrong tell them they are wrong and what the right answer is.

# The chosen numbers in equation, For testing purposes its preset but in actual program willl be randomly generated
num1 = 5
num2 = 3
# Calculating answer for question
answer = num1 * num2
# Display question
print("{} x {} = ?".format(num1, num2))

for item in range(0, 2):
    # Ask user for their answer
    user_answer = int(input("What is the answer?:"))

    # If user gets it right congratulate them, if not tell them right answer
    if user_answer == answer:
        print("Wow, very nice you got it right. Well done.")
    else:
        print("Oh no, you got it wrong, The right answer is {}".format(answer))