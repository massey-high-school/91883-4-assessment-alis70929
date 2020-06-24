# Quiz Quest Component 5 Summary no colour

# To Do
# - Store the generated questions, the users answer, the actual answer and whether or not the user got it right
# - Display the stored data from each round in a nice table



questions = ["2 x 3", "3 x 6","12 x 12"]
actual_answers = [6 , 18, 144]
users_answers = [9 , 18, 144]
correct_incorrect = ["Correct", "Incorrect", "Correct"]

listcount = 0
print("Question # |Question |Users Answer|Correct Answer|Correct?  |")

for item in actual_answers:
    print("Question {1:<{0}}| {3:<{2}} | {5:<{4}} | {7:<{6}} |{9:<{8}}|".format(2,listcount + 1 , 7 ,questions[listcount] ,10 ,users_answers[listcount],12, actual_answers[listcount],10, correct_incorrect[listcount]))
    listcount +=1
