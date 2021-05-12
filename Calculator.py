#Using Tkinter to make functional calculator

from tkinter import *

win = Tk()  
win.geometry("333x360")  
win.resizable(0, 0) 
win.title("JustACalculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""



input_text = StringVar()

input_frame = Frame(win, width=500, height=50, bd=2,
                    highlightbackground="black", highlightcolor="white", highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'),
                    textvariable=input_text, width=50, bg="#eee", bd=2, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=18)

btns_frame = Frame(win, width=312, height=272.5, bg="black")

btns_frame.pack()

# 1st row of the calculator buttons

clear = Button(btns_frame, text="Clear",font='Helvetica 9 bold', fg="black", width=34, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="÷", fg="black", width=10, height=3, bd=2, bg="#fffbdf",
                cursor="spider", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# 2nd row of the calculator buttons

seven = Button(btns_frame, text="7",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
              cursor="spider", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
                  cursor="spider", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# 3rd row of the calculator buttons

four = Button(btns_frame, text="4", font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
              cursor="spider", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
              cursor="spider", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
             cursor="spider", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-",font='Helvetica  9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# 4th row of the calculator buttons

one = Button(btns_frame, text="1",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
             cursor="spider", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
             cursor="spider", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+",font='Helvetica 9 bold', fg="black", width=10, height=3, bd=2, bg="#fffbdf",
              cursor="spider", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# 5th row of the calculator buttons

zero = Button(btns_frame, text="0", font='Helvetica 9 bold', fg="black", width=22, height=3, bd=2, bg="#fffbdf", cursor="spider",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1
              )

decimal = Button(btns_frame, text=".",font='Helvetica 9 bold',  fg="black", width=10, height=3, bd=2, bg="#fffbdf",
               cursor="spider", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=",font='Helvetica 9 bold',  fg="black", width=10, height=3, bd=2, bg="#fffbdf",
                cursor="spider", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
