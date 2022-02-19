# Ruben Sanduleac
# QuizBrain class used to initialize the initial score, check if there are more
# questions in the list. Continue to the next question and check the answer if its
# valid.

class QuizBrain:
    """Default constructor used to initialize the score to '0', question number to '0'
    and set the question in the list to self"""
    def __init__(self, question_in_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_in_list

    def still_has_questions(self):
        """check there is still questions by comparing the length of the list to the current length
        question number"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """check on which question we are currently, then increment the question.
        Receive the users answer to then check the answer in the check_answer"""
        current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}:{current.text}(True/False): ")
        self.check_answer(user_answer, current.answer)

    def check_answer(self, usr_ans, cr_quest_answer):
        """check the users input by comparing the users answer to the actual answer. still_has_questions
        incrementing their score if answered correctly."""
        if usr_ans.lower() == cr_quest_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("The answer is wrong.")
        # print the correct answer if answered incorrecty
        print(f"The correct answer was: {cr_quest_answer}")
        # print current general score over the question number
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
