# Quiz Quest Component 3 Generate and display question

# To do
# - Based on user input generate a question,
#  - All times table choice will make it so both sides of the equation will have a random number between 1 - 12
#  - specific times table choice will make it so only one side of the equation is randomly generated
# - Get an answer for generated question
# - Display Generated Question and answer(For Testing Purposes)


# Imports go here
import random
print("Num1 Range")
low1 = int(input("Low"))
high1 = int(input("High"))
print("Num2 range")
low2 = int(input("Low"))
high2 = int(input("High"))
# Main Code goes here

# Ask user which times table they would like to practice ( all 12 or a specific one)


# Loop here for testing purposes
for item in range(0,5):
    # Sets the first number in the equation

    num1 = random.randint(low1,high1) # The first number in the equation will be randomly generated between the range given above for num 1
    num2 = random.randint(low2,high2) # The second number in the equation will always be random between the range given above for num 2

    # Calclulating the answer to the generated question
    actual_answer = num1 * num2

    # Display Question and Answer
    print("{} x {} = {}".format(num1, num2, actual_answer))

