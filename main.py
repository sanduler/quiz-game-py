# Ruben Sanduleac
# Description: Main file for the quiz-game. The main goal of is to load all the questions from the data.py
#              Then, through the use of OOP to expand the data.py without touching the logic of the code.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

# create a blank list for the questions
question_bank = []
# use a for loop to go through every single question and answer in the data.py
for question in question_data:
    # finds the 'question' key from data.py
    question_text = question["question"]
    # finds the 'correct_answer' key from data.py
    question_answer = question["correct_answer"]
    # pass the question and the answer to the Question class and initialize the variable
    new_question = Question(question_text, question_answer)
    # add the return from the class back to the list 'question_bank'
    question_bank.append(new_question)


# initialize the QuizBrain class by passing the question bank
quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

# if the quiz still has questions the continue to the next question
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the Quiz")
# print the final score
print(f"You're final score: {quiz.score}/{quiz.question_number}")
