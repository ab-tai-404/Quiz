from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial",20 ,"italic")

class QuizInterface:
    def __init__(self):
        self.score  = 0

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg = THEME_COLOR ,pady=20 ,padx=20)
        self.label_score = Label(text = f"score : {self.score}", bg = THEME_COLOR , fg= "white")
        self.label_score.grid(row = 0 , column=1 )

        self.canvas  = Canvas(height=250,width=300)
        self.question_text = self.canvas.create_text(150,125,fill= THEME_COLOR , text = "adddddddddddddddd  \n ddddddhmed mohsin ",font=FONT)
        self.canvas.grid(column=0 , row=1,columnspan=2  ,pady=20)


        image_false = PhotoImage(file="images/false.png")
        image_true = PhotoImage(file="images/true.png")

        self.b_false = Button(image=image_true)
        self.b_false.grid(row=2, column=0 )

        self.b_false = Button(image= image_false )
        self.b_false.grid(row = 2 , column=1)
        self.window.mainloop()


a = QuizInterface()