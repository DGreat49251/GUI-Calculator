'''GUI Calculator using Python'''
'''Python program to create a Graphical User Interface based Standard Calculator using Tkinter module.'''

from tkinter import *   # import everything from tkinter module

expression = ""     # globally declare the expression variable

def press(num):     # Function to update expression in the text entry box
	global expression   # point out the global expression variable
	expression = expression + str(num)  # concatenation of string
	equation.set(expression)    # update the expression by using set method

def equalpress():   # Function to evaluate the final expression
	try:    # Put that code inside the try block which may generate the error
		global expression
		total = str(eval(expression))   # eval function evaluate the expression and str function convert the result into string
		equation.set(total)
		expression = ""     # initialze the expression variable by empty string
	except: # if error is generate then handle by the except block
		equation.set(" error ")
		expression = ""

def clear():    # Function to clear the contents of text entry box
	global expression
	expression = ""
	equation.set("")

# Driver code
if __name__ == "__main__":
	tk = Tk()  # create a GUI window
	tk.configure(background="brown")     # set the background colour of GUI window
	tk.title("Standard Calculator")      # set the title of GUI window
	tk.geometry("270x150")     # set the configuration of GUI window

	equation = StringVar()  # StringVar() is the variable class we create an instance of this class
	expression_field = Entry(tk, textvariable=equation)    # create the text entry box for showing the expression.
	expression_field.grid(columnspan=4, ipadx=70)   # grid method is used for placing the widgets at respective positions in table like structure.

	#creating Buttons and place at a particular location inside the root window .
	#when user press the button, the command or function affiliated to that button is executed.
	b1 = Button(tk, text=' 1 ', fg='black', bg='gray',command=lambda: press(1), height=1, width=7)
	b1.grid(row=2, column=0)

	b2 = Button(tk, text=' 2 ', fg='black', bg='gray',command=lambda: press(2), height=1, width=7)
	b2.grid(row=2, column=1)

	b3 = Button(tk, text=' 3 ', fg='black', bg='gray',command=lambda: press(3), height=1, width=7)
	b3.grid(row=2, column=2)

	b4 = Button(tk, text=' 4 ', fg='black', bg='gray',command=lambda: press(4), height=1, width=7)
	b4.grid(row=3, column=0)

	b5 = Button(tk, text=' 5 ', fg='black', bg='gray',command=lambda: press(5), height=1, width=7)
	b5.grid(row=3, column=1)

	b6 = Button(tk, text=' 6 ', fg='black', bg='gray',command=lambda: press(6), height=1, width=7)
	b6.grid(row=3, column=2)

	b7 = Button(tk, text=' 7 ', fg='black', bg='gray',command=lambda: press(7), height=1, width=7)
	b7.grid(row=4, column=0)

	b8 = Button(tk, text=' 8 ', fg='black', bg='gray',command=lambda: press(8), height=1, width=7)
	b8.grid(row=4, column=1)

	b9 = Button(tk, text=' 9 ', fg='black', bg='gray',command=lambda: press(9), height=1, width=7)
	b9.grid(row=4, column=2)

	b0 = Button(tk, text=' 0 ', fg='black', bg='gray',command=lambda: press(0), height=1, width=7)
	b0.grid(row=5, column=0)

	p = Button(tk, text=' + ', fg='black', bg='pink',command=lambda: press("+"), height=1, width=7)
	p.grid(row=2, column=3)

	m = Button(tk, text=' - ', fg='black', bg='pink',command=lambda: press("-"), height=1, width=7)
	m.grid(row=3, column=3)

	mul = Button(tk, text=' * ', fg='black', bg='pink',command=lambda: press("*"), height=1, width=7)
	mul.grid(row=4, column=3)

	div = Button(tk, text=' / ', fg='black', bg='pink',command=lambda: press("/"), height=1, width=7)
	div.grid(row=5, column=3)

	eq = Button(tk, text=' = ', fg='black', bg='yellow',command=equalpress, height=1, width=7)
	eq.grid(row=5, column=2)

	clear = Button(tk, text='Clear', fg='white', bg='black',command=clear, height=1, width=7)
	clear.grid(row=6, column=3)

	dec= Button(tk, text='.', fg='black', bg='light blue',command=lambda: press('.'), height=1, width=7)
	dec.grid(row=5, column=1)
	
	tk.mainloop()  # start the GUI