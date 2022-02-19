from tkinter import *
THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.configure(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # pull the two images for the button and pass them into the ui_buttons function
        right_image = PhotoImage(file="./img/true.png")
        wrong_image = PhotoImage(file="./img/false.png")
        self.ui_buttons(right_image, wrong_image)
        # center the window upon opening
        self.window.eval('tk::PlaceWindow . center')
        # loop the main window to stay open
        self.window.mainloop()

    def ui_buttons(self, correct_image, incorrect_image):
        self.right_button = Button(image=correct_image, highlightthickness=0, bd=0)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=incorrect_image)
        self.wrong_button.config(highlightthickness=0, bd=0)
        self.wrong_button.grid(row=2, column=1)