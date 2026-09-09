from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.window = Tk()
        self.quizbrain = quizbrain
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", fg= "white", bg=THEME_COLOR, font=("Arial", 10, "italic"))
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0, borderwidth=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Szöveg", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, command=self.true_pressed, activebackground=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0, command=self.false_pressed, activebackground=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizbrain.still_has_questions():
            self.score_text.config(text=f"Score: {self.quizbrain.score}")
            self.canvas.itemconfig(self.quiz_text, fill=THEME_COLOR)
            q_text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.quiz_text, text= q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text= "You reached the end\n"
                                                         f"Your final score is: {self.quizbrain.score}")

    def true_pressed(self):
        if self.quizbrain.still_has_questions():
            self.give_feedback(self.quizbrain.check_answer("True"))

    def false_pressed(self):
        if self.quizbrain.still_has_questions():
            self.give_feedback(self.quizbrain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.quiz_text, fill= "white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.quiz_text, fill= "white")
        self.window.after(1000, self.get_next_question)