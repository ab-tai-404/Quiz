from tkinter import Tk ,Canvas,Label ,Button,PhotoImage ,DISABLED
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial",20 ,"italic")


class QuizInterface:
    def __init__(self , quiz : QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg = THEME_COLOR ,pady=20 ,padx=20)
        self.label_score = Label(text = f"score : {self.quiz.score}", bg = THEME_COLOR , fg= "white" )
        self.label_score.grid(row = 0 , column=1 )

        self.canvas  = Canvas(height=250,width=300)
        self.question_text = self.canvas.create_text(150,125,fill= THEME_COLOR ,
                                                     text = f"{self.quiz.next_question()}" ,font=FONT,width=250)
        self.canvas.grid(column=0 , row=1,columnspan=2  ,pady=20)


        image_false = PhotoImage(file="images/false.png")
        image_true = PhotoImage(file="images/true.png")
        # False Button
        self.b_false = Button(image= image_false  ,command=self.answer_false)
        self.b_false.grid(row=2, column=0 )
        # True Button
        self.b_true = Button(image= image_true,command=self.answer_true )
        self.b_true.grid(row = 2 , column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.label_score.config(text=f"score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=f"{q_text}")
        else :
            self.b_true["state"] = DISABLED
            self.b_false["state"] = DISABLED
            self.canvas.itemconfig(self.question_text , text ="THE END" ,font = ("Arial",30 ,"italic") )

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,answer):
        color ="green" if answer else "red"
        self.canvas.config(background=color)
        self.canvas.after(1000 , lambda: self.get_next_question())



