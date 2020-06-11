# Quiz Quest Component 3 Generate and display question

# To do
# - Based on user input generate a question,
#  - All times table choice will make it so both sides of the equation will have a random number between 1 - 12
#  - specific times table choice will make it so only one side of the equation is randomly generated
# - Get an answer for generated question
# - Display Generated Question and answer(For Testing Purposes)


# Imports go here
import random

# Main Code goes here

# Ask user which times table they would like to practice ( all 12 or a specific one)
all_or_specific = input("All Times tables?:")
if all_or_specific == "no":
    specific_times_table = int(input("Which Times Table?:")) # Here the user chooses a specific times table

# Loop here for testing purposes
for item in range(0,5):
    # Sets the first number in the equation
    if all_or_specific == "no":
        num1 = specific_times_table # The first number in the equation will be the chosen times table if the user chose to do so
    else:
        num1 = random.randint(1, 12) # Random if the user chose to do all 12 at once

    num2 = random.randint(1,12) # The second number in the equation will always be random

    # Calclulating the answer to the generated question
    actual_answer = num1 * num2

    # Display Question and Answer
    print("{} x {} = {}".format(num1, num2, actual_answer))

