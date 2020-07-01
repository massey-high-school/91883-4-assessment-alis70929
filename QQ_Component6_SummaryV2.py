# Quiz Quest Component 5 Summary V2 make the columns nicer

# To Do
# - Store the generated questions, the users answer, the actual answer and whether or not the user got it right
# - Display the stored data from each round in a nice table, without it making the columns out of shape.

questions = ["2 x 3", "3 x 6","12 x 12"]  # Stores each question
actual_answers = [6 , 18, 144]  # Stores the correct answer for each question
users_answers = [9 , 18, 144]  # Stores the users answer for each question
correct_incorrect = ["Correct", "Incorrect", "Correct"]  # Stores wheter or not they are correct

listcount = 0 # To count which questions summary needs to be generated
print("Question  #|Question |Users Answer|Correct Answer|Correct?  |")# Displays the top of the summary table


for item in actual_answers: # loops until there is no more question summary to display
    # Generates a row that displays a summary for the question listcount is on, with even
    print("Question {1:>{0}}| {3:<{2}} | {5:<{4}} | {7:<{6}} |{9:<{8}}|".format(2,listcount + 1 ,
                                                                                7 ,questions[listcount] ,
                                                                                10 ,users_answers[listcount],
                                                                                12, actual_answers[listcount],
                                                                                10, correct_incorrect[listcount]))


    listcount +=1 # generate the next question summary row

# results
print()
# How many correct as a fraction
print("{}/{} questions were answered incorrectly".format(correct_incorrect.count("Incorrect"), len(correct_incorrect)))
# How many incorrect as a fraction
print("{}/{} questions were answered correctly".format(correct_incorrect.count("Correct"),len(correct_incorrect)))