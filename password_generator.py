import string
import random
from tkinter import *


def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    pswdLength = inpValue.get()
	## shuffling the characters
    random.shuffle(characters)
	
	## picking random characters from the list
    password = []
    for i in range(pswdLength):
        password.append(random.choice(characters))

	## shuffling the resultant password
    random.shuffle(password)

	## converting the list to string
	## printing the lis
    Label(root,text="".join(password)).grid()


## characters to generate password from

root = Tk()
root.geometry("654x400")
root.title("Password Generator")
root.maxsize(800,750)
root.minsize(252,352)

## length of password from the user

length = Label(root,text="Enter password length: ")
length.grid(row=0,column=0)


inpValue =IntVar()
inpValue.set("")


inp = Entry(root,textvariable=inpValue)
inp.grid(row=0,column=1)

btn = Button(root,text="Generate Password",command=generate_random_password)
btn.grid(row=0,column=2)

root.mainloop()
