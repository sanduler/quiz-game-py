# Ruben Sanduleac

# TODO: Add asking Question
# TODO: Add checking if the answer is valid
# TODO: Add checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_in_list):
        self.question_number = 0
        self.question_list = question_in_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        input(f"{self.question_number}:{current.text}(True/False): ")
