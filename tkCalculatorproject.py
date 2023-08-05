import tkinter as tk

#button_click function is called when a number button is pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

#button_clear function clears the entry widget when the "C" button is pressed
def button_clear():
    entry.delete(0, tk.END)

#button_equal function is executed when the equals button is pressed. It evalutes the 
#expression in the entry widget using the 'eval' function and displays the result
#if an error occurs during evaluation,it displays "Error" in the entry widget.
def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator coded by Rahul")

# Create the entry widget for displaying the input and result
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define the buttons
buttons = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("C", 5, 0),
    ("%", 5, 1)
]

# Create the buttons and place them on the grid
#"lambda " function is used to pass the button text as an argument to the 'button_click' function
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=40, pady=20, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

# Create the clear button so that calls the button_clear function when clicked
clear_button = tk.Button(window, text="Clear", padx=20, pady=10, command=button_clear)
clear_button.grid(row=5, column=2,columnspan=2)

# Create the equals button so that calls the button_clear function when clicked
equals_button = tk.Button(window, text="=", padx=40, pady=20, command=button_equal)
equals_button.grid(row=4, column=2)

# Start the main event loop
window.mainloop()
