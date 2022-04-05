from tkinter import *



def check():
    
    # initialize sum1
    sum1 = 0
    number = inpVal.get()
    # find the sum1 of the cube of each digit
    temp = number
    while temp > 0:
        digit = temp % 10
        # print(digit)
        sum1 += digit ** 3
        temp //= 10
        # display the result
    if number == sum1:
        Label(root,text=f"{number} is an Armstrong number").grid(row=3,column=3,columnspan=10)
    else:
        Label(root,text=f"{number} is not an Armstrong number",font='Arial 15 italic bold').grid(row=3,column=5,columnspan=10)
root = Tk()
root.title("Armstrong Number")
root.geometry("666x355")
root.maxsize(800,600)
root.minsize(255,153)

head = Label(root,text="Armstrong Number",font='Times 24 bold')
head.grid(row=0,column=5,columnspan=10)

num = Label(root,text='Enter a number',font='Times 15')
num.grid(row=1,column=0)

inpVal = IntVar()
inpVal.set("")
inp  = Entry(root,textvariable=inpVal)
inp.grid(row=1,column=1)

btn = Button(root, text='Check',command=check)
btn.grid(row=2,column=1)






root.mainloop()