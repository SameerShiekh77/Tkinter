import random
from tkinter import *  

root = Tk()
root.title("Number guessing game")
root.geometry('400x400')

class NumberGuessing:
    #Variables_that_stores_Entry_values
    num1 = IntVar()
    num1.set("")
    num2 = IntVar()
    num2.set("")
    guessedNumber=IntVar()

    #It_stores_the_random_Number
    lives = 5
    value = random.randint(0, 99)

    #Function_For_Checking_And_Generating_Random_No
    def check(self):
        
       

        #Condition_that_checks_random_no_matches_guessed_no_or_not
        if self.guessedNumber.get() == self.value:

            #If_matches_result_label_text_changed_to_given_text
            self.ResultLabel.configure(text= "Wow You are Right")
        elif self.guessedNumber.get() > self.value:
            self.lives -= 1
            #If_not_matches_result_label_text_changed_to_given_text_and_random_no
            self.ResultLabel.configure(text=f"Enter lower number\nYou have {self.lives} lives left" )
        elif self.guessedNumber.get() < self.value:
            self.lives -= 1
            #If_not_matches_result_label_text_changed_to_given_text_and_random_no
            self.ResultLabel.configure(text=f"Enter higher number\nYou have {self.lives} lives left" )
        if self.lives == 0:
            self.ResultLabel.configure(text="\nGame Over your lives has finished ")
            self.btn._displayof(DISABLED)

    #When_the_class_called_this_functions_runs_first
    def __init__(self):
        #Fonts_for_Label_&_Entry_Boxes
        self.lfont = ('Times', 16)
        
        #_Label_FROM
        self.Label1= Label(root, text="From 0 to 99", font=self.lfont, foreground="red")
        self.Label1.grid(row=0, column=0, sticky='ne', padx=5, pady=5)


        #Label_Guess_Any_Number
        self.Label3= Label(root, text="Guess The Number", font=self.lfont, foreground="darkViolet")
        self.Label3.grid(row=3, columnspan=2, pady=10)

        #Entry_Box_For_Number_Guessing
        self.entry3= Entry(root, textvariable=self.guessedNumber, font=self.lfont, foreground="darkorchid")
        self.entry3.grid(row=4, columnspan=2, pady=10, padx=5)

        #Button_That_Check_The_Value_Matches_Random_No_OR_Not
        self.btn = Button(root, text="Check", font=self.lfont, foreground="darkviolet", command=self.check)
        self.btn.grid(row=5, columnspan=3, pady=10,)

        #Label_For_Showing_Result
        self.ResultLabel= Label(root, text="", font=self.lfont, foreground="darkViolet")
        self.ResultLabel.grid(row=6, columnspan=2, pady=10, padx=5)

        root.mainloop()

#Calling_The_Class
NumberGuessing()