# Ruben Sanduleac
# QuizUI class used to initialize the GUI for the program.
# QuizUI uses tkinter as the frontend method of displaying the
# Quiz.
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#406882"


class QuizUI:
    """
    QuizUI class responsible for the UI elements objects.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """Constructor initializes the window, canvas, score labels, question text
        The constuctor also call the ui buttons method to create buttons"""
        # create a quiz_brain object from QuizBrain class that gets passed from the main class
        self.quiz = quiz_brain
        # intilizes the buttons to do nothing
        self.wrong_button = None
        self.right_button = None
        # set the score initially to 0
        self.score = 0
        # create a window object
        self.window = Tk()
        # set the tittle of the UI
        self.window.title("Quizzer")
        # set the theme of the window to the global theme
        self.window.configure(bg=THEME_COLOR)
        # config the padding between elements
        self.window.config(padx=20, pady=20)
        # f string for the label to display the score on the main window
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(font=("Arial", 20, "italic"))
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # create a canvas object
        self.canvas = Canvas(width=300, height=250, bg="white")
        # config the question parameters
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
        """Create ui buttons for correct and incorrect
        Images are passed throughinto this method"""
        self.right_button = Button(image=correct_image, highlightthickness=0, bd=0, command=self.is_true)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=incorrect_image)
        self.wrong_button.config(highlightthickness=0, bd=0, command=self.is_false)
        self.wrong_button.grid(row=2, column=1)

    def get_new_question(self):
        """This function places a new question on the canvas.
        1. the canvas question starts at white
        2. if there are questions the score is incremented and this function gets called
        based on the users answer True/False.
        3. IF there are no questions remaining the buttons get disabled and
        the program lets the user know of the final score."""
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
        """check the answer using the feedback functions
        and the answer "True" gets sent to the QuizBrain class"""
        answer = self.quiz.check_answer("True")
        self.feedback(answer)

    def is_false(self):
        """check the answer using the feedback functions
        and the answer "False" gets sent to the QuizBrain class"""
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, ans: bool):
        """feedback function responsible for giving feedback to the user if the
        user answers correctly the canvas will turn green else it will turn red. After short delay (800)
        the program tries to get a new question."""
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(800, self.get_new_question)
