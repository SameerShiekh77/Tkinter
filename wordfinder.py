from tkinter import *
from tkinter import messagebox
import random
again_play = 'y'

score = 0
# hidden words list
beginner_word_list = ['mic', 'mouse', 'notes', 'binary', 'octave', 'list']
moderate_word_list = ['ascii', 'Argument', 'Arrays',
    'Dictionary', 'decimal', 'interpreter']
advance_word_list = ['Algorithm', 'Boolean', 'Desktop',
    'Tkinter', 'django framework', 'compilation']

# generate random number
random_number = random.randint(0, len(beginner_word_list)-1)

# randomly initialize special word
simple_word = beginner_word_list[random_number]
moderate_word = moderate_word_list[random_number]
advance_word = advance_word_list[random_number]
lives = 5
value = ""

def finder():
    global lives
    global again_play
    frm = Frame(root)
    frm.grid(row=4, column=2)
    # starting game
    while again_play == 'y':
        # initalize user lives and scores
        for i in range(0,lives):
            user_word = StringVar()

            if userInput.get() == 1:
                Label(frm, text=f"\nFind a word from this list: {beginner_word_list}\nFind a word which I hidden in this program: ").grid(
                    row=3, column=1)
                user_input = Entry(frm, textvariable=user_word)
                user_input.grid(row=4, column=1)
                val = user_word.get()
                print(val)
                enterBtn = Button(frm, text='Find',command=lambda: matchAnswer(val))
                enterBtn.grid(row=4, column=2)



            elif userInput.get() == 2:
                Label(frm, text=f"\nFind a word from this list: {moderate_word_list}\nFind a word which I hidden in this program: ").grid(
                    row=3, column=1)
                user_input = Entry(frm, textvariable=user_word)
                user_input.grid(row=4, column=1)
                val = user_word.get()
                enterBtn = Button(frm, text='Find',command=lambda: matchAnswer(val))
                enterBtn.grid(row=4, column=2)

              
            elif userInput.get() == 3:
                Label(frm, text=f"\nFind a word from this list: {advance_word_list}\nFind a word which I hidden in this program: ").grid(
                    row=3, column=1)
                user_input = Entry(frm, textvariable=user_word)
                user_input.grid(row=4, column=1)
                val = user_word.get()
                enterBtn = Button(frm, text='Find',command=lambda: matchAnswer(val))
                enterBtn.grid(row=4, column=2)

              
    
def matchAnswer(a):
    global lives
    if (a == simple_word.lower()) or (a == moderate_word.lower()) or (a == advance_word.lower()):
        messagebox.showinfo("Winner!!", "Congratulation!! You Find Right Word")
        # score += 10
                # again_play = input("Do you want to play again? (if yes then press 'y' )")
    elif lives>=0:
        lives -=1
        messagebox.showinfo('Try Again',f"Try Again!!! You Just left {lives} lives\n")
    else:
        if userInput.get() == 1:
            print(f"Game Over!!! The Word is {simple_word}")
            # again_play = input(
            #     "Do you want to play again? (if yes then press 'y' )")

        elif userInput.get() == 2:
            print(f"Game Over!!! The Word is {moderate_word}")
            # again_play = input(
            #     "Do you want to play again? (if yes then press 'y' )")

        elif userInput.get() == 3:
            print(f"Game Over!!! The Word is {advance_word}")
            # again_play = input(
            #     "Do you want to play again? (if yes then press 'y' )")

root = Tk()
root.title("Find a word game")
root.geometry("741x1000")


# initialize variable for again play
again_play = 'y'

score = 0

# starting game
Label(root,text="*************** WELCOME TO FIND A WORD GAME ***********************\n\n",font='Times 24 bold').grid(row=0,column=0,columnspan=10)

# Game Start from choice
gameOption = Label(root,text="Choose Game Level: \nPress 1 for Beginners\nPress 2 for Moderate\nPress 3 for Advance\n\n\n")
gameOption.grid(row=1,column=2)

userInput = IntVar()
userInput.set("")
gameChoice = Entry(root,textvariable=userInput)
gameChoice.grid(row=2,column=2)

btn = Button(root,command=finder,text='Enter')
btn.grid(row=2,column=3)
 


root.mainloop()
