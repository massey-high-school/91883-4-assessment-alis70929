# Quiz Quest Component 5 Summary

# To Do
# - Store the generated questions, the users answer, the actual answer and whether or not the user got it right
# - Display the stored data from each round in a nice table

questions = ["2 x 3", "3 x 6"] # Stores questions
actual_answers = [6, 18] # Stores correct answers
users_answers = [9, 18] # Stores users answer
correct_incorrect = ["correct  ", "incorrect"] # Stores if they were correct or incorrect


print("Question #|Question |     Users Answer    |    Correct Answer      |Correct?  |") # Display top of table
listcount = 0 # Which question summary needs to be displayed
for item in actual_answers:
    print("Question {}|  {}  |         {}          |          {}            |{}   |".format(listcount + 1 , questions[listcount] ,users_answers[listcount], actual_answers[listcount], correct_incorrect[listcount]))
    listcount += 1
