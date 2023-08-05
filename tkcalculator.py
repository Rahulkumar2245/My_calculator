from tkinter import *
# Create the main window
window = Tk()
# window.geometry('200x300')
window.title("Calculator coded by Rahul")
window.configure(bg="pink")

#button_click function is called when a number button is pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

#button_clear function clears the entry widget when the "C" button is pressed
def button_clear():
    entry.delete(0, END)

#button_equal function is executed when the 'equals' button is pressed. It evalutes the 
#expression in the entry widget using the 'eval' and displays the result
def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0,END)
    entry.insert(END, result)

# Create an Entry widget to display the result
entry = Entry(window, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create number buttons
#"lambda " function is used to pass the button text as an argument to the 'button_click' function
button_1 = Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create operator buttons
button_add = Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_equal = Button(window, text="=", padx=40, pady=10, command=button_equal)
button_clear = Button(window, text="Clear", padx=30, pady=10, command=button_clear)

# Position buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

# Run the main loop
window.mainloop()
