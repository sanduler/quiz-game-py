# Ruben Sanduleac
# QuizBrain class used to initialize the initial score, check if there are more
# questions in the list. Continue to the next question and check the answer if its
# valid.
import html


class QuizBrain:
    """Default constructor used to initialize the score to '0', question number to '0'
    and set the question in the list to self"""

    def __init__(self, question_in_list):
        self.current = None
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
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"{self.question_number}:{q_text}(True/False): ")
        # self.check_answer(user_answer, self.current.answer)

    def check_answer(self, usr_ans):
        """check the users input by comparing the users answer to the actual answer. still_has_questions
        incrementing their score if answered correctly."""
        cr_quest_answer = self.current.answer
        if usr_ans.lower() == cr_quest_answer.lower():
            self.score += 1
            return True
        else:
            return False
