from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank  = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    

quiz = QuizBrain(question_bank)
while quiz.still_has_question(): #if quiz still has question remaining.
    quiz.next_question()
# Define the box and print the statement inside it
print('''#################################
#       You have completed       #
#            the QUIZ!           #
#################################''')
quiz_score = quiz.score  # Example score, replace with `quiz.score`
quiz_total = quiz.question_number  # Example total, replace with `quiz.question_number`
print(f"#   Your final score was : {quiz_score}/{quiz_total}   #")
print("#################################")

