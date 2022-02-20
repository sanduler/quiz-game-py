from tkinter import *

import feedback as feedback

from quiz_brain import QuizBrain
import data
THEME_COLOR = "#406882"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.wrong_button = None
        self.right_button = None
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.configure(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(font=("Arial", 20, "italic"))
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # pull the two images for the button and pass them into the ui_buttons function
        right_image = PhotoImage(file="./img/true.png")
        wrong_image = PhotoImage(file="./img/false.png")
        self.ui_buttons(right_image, wrong_image)
        self.get_new_question()
        # center the window upon opening
        self.window.eval('tk::PlaceWindow . center')
        # loop the main window to stay open
        self.window.mainloop()

    def ui_buttons(self, correct_image, incorrect_image):
        self.right_button = Button(image=correct_image, highlightthickness=0, bd=0, command=self.is_true)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=incorrect_image)
        self.wrong_button.config(highlightthickness=0, bd=0, command=self.is_false)
        self.wrong_button.grid(row=2, column=1)

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You reached the end of the Quiz!\n"
                                        f"Final Score: {self.quiz.score}/{self.quiz.question_number}")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def is_true(self):
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def is_false(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, ans:bool):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(800, self.get_new_question)