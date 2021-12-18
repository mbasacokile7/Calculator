from tkinter import *

# This is the first thing you do, when using Tkinter
root = Tk()
root.title("Simple Calculator")

# To use Tkinter, its a 2 step process:
# 1. Define what you want(Widgets)
# 2. Put it on the screen using grid() or pack()

# Add an entry widget
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5,  padx=10, pady=20)


# Command Functions

def button_click(number):
    # Get the entry and put it in a variable called current
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_click_point():
    global f_num
    global math
    math = "Create Decimal Number"

    f_num = int(e.get())
    e.delete(0, END)



def button_click_x10():
    global f_num
    global math
    math = "Times by 10"

    f_num = int(e.get())
    e.delete(0, END)



def button_multiply():
    # Get the current entry as the first number
    first_number = e.get()
    # Create a global variables
    global f_num
    global math
    math = "Multiplication"
    # Convert the first number to integer
    if "." in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    # Delete Entry in order to add new entry
    e.delete(0, END)


def button_add():
    first_number = e.get()
    # Create a global variables
    global f_num
    global math
    math = "Addition"
    # Convert the first number to integer
    if "." in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    # Delete Entry in order to add new entry
    e.delete(0, END)


def button_minus():
    first_number = e.get()
    # Create a global variables
    global f_num
    global math
    math = "Subtraction"
    # Convert the first number to integer

    if "." in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    # Delete Entry in order to add new entry
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    # Create a global variables
    global f_num
    global math
    math = "Division"
    # Convert the first number to integer
    if "." in first_number:
        f_num = float(first_number)
    else:
        f_num = int(first_number)
    # Delete Entry in order to add new entry
    e.delete(0, END)


def button_ans():

    if button_clearf():
        answer = result
        if "." in answer:
            e.delete(0, END)
            e.insert(0, float(answer))
        else:
            e.delete(0, END)
            e.insert(0, int(answer))



def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "Addition":
        result = f_num + int(second_number)
        e.insert(0, result )

    if math == "Subtraction":
        result = f_num - int(second_number)
        e.insert(0, result)

    if math == "Division":
        result = f_num / int(second_number)
        e.insert(0, result)

    if math == "Multiplication":
        result = f_num * int(second_number)
        e.insert(0, result)

    if math == "Times by 10":
        result = f_num * (10**(int(second_number)))
        e.insert(0, reslut)

    if math == "Create Decimal Number":
        result = str(f_num) + "." + str(second_number)
        e.insert(0, result)




def button_del():
    # Get the current entry
    current_entry = e.get()
    # Get the length of the string
    length = len(current_entry)
    # Delete from the second last 1 to the last one
    e.delete(length - 1, END)


def button_clearf():
    e.delete(0, END)



#Define Buttons

## Number Buttons
button_1 = Button(root, text = "1", padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx=40, pady=20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx=40, pady=20, command = lambda: button_click(0))


# Buttons with specific functions
button_dot = Button(root, text = ".", padx=40, pady=20, command = button_click_point)
button_x10 = Button(root, text = "x10", padx=35, pady=20, command = button_click_x10)

button_del = Button(root, text = "DEL", padx=45, pady=20, command = button_del)
button_clear = Button(root, text = "Clear", padx=45, pady=20, command = button_clearf)


button_multiplication = Button(root, text = "*", padx=55, pady=20, command = button_multiply)
button_division = Button(root, text = "/", padx=55, pady=20, command = button_divide)
button_addition = Button(root, text = "+", padx=55, pady=20, command = button_add)
button_subtraction = Button(root, text = "-", padx=55, pady=20, command = button_minus)

button_answer = Button(root, text = "Ans", padx=50, pady=20, command = button_ans)
button_equal = Button(root, text = "=", padx=50, pady=20, command = button_equal)


# Put the buttons on the screen

# First Row of numbers

button_7.grid(row=1, column = 0)
button_8.grid(row=1, column = 1)
button_9.grid(row=1, column = 2)

# Second Row of numbers
button_4.grid(row=2, column = 0)
button_5.grid(row=2, column = 1)
button_6.grid(row=2, column = 2)

# Third Row of Numbers
button_1.grid(row=3, column = 0)
button_2.grid(row=3, column = 1)
button_3.grid(row=3, column = 2)

# Last Row for 0 and Equal Sign
button_0.grid(row=4, column = 0)
button_dot.grid(row = 4, column=1)
button_x10.grid(row = 4, column=2)

# First Row of Function Keys
button_del.grid(row=1, column=3, columnspan = 1)
button_clear.grid(row=1, column=4, columnspan = 1)

# Second Row of Function Keys
button_multiplication.grid(row=2,column=3, columnspan = 1)
button_division.grid(row=2, column=4, columnspan = 1)

# Third Row
button_addition.grid(row=3, column=3, columnspan = 1)
button_subtraction.grid(row=3, column=4, columnspan = 1)

# Fourth Row

button_answer.grid(row=4, column=3, columnspan = 1)
button_equal.grid(row=4, column=4, columnspan = 1)


