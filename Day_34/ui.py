from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.quiz = quiz

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150,125,width=280,text="Gela", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.correct)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text=f"Your final score: {self.quiz.score}")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            
    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


