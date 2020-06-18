# Quiz Quest Component 5 Summary no colour

# To Do
# - Store the generated questions, the users answer, the actual answer and whether or not the user got it right
# - Display the stored data from each round in a nice table

questions = ["2 x 3", "3 x 6"]
actual_answers = ["6", "18"]
users_answers = ["9", "18"]
correct_incorrect = ["correct","incorrect"]

listcount = 0
print("Question #|Question|Users Answer|Correct Answer|Correct? |")
for item in actual_answers:
    print("Question {}|    {}   |         {}           |          {}            |{} |".format(listcount + 1, users_answers[listcount], actual_answers[listcount],correct_incorrect[listcount]))
