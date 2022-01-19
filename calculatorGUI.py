import tkinter

root = tkinter.Tk()
root.title("Simple Calculator")

def buttonAdd():
    return

entryField = tkinter.Entry(root, width=20, borderwidth = 3)
button1 = tkinter.Button(root, text="1", padx = 20, pady = 5, command=buttonAdd)
button2 = tkinter.Button(root, text="2", padx = 20, pady = 5, command=buttonAdd)
button3 = tkinter.Button(root, text="3", padx = 20, pady = 5,command=buttonAdd)
button4 = tkinter.Button(root, text="4", padx = 20, pady = 5,command=buttonAdd)
button5 = tkinter.Button(root, text="5", padx = 20, pady = 5, command=buttonAdd)
button6 = tkinter.Button(root, text="6", padx = 20, pady = 5, command=buttonAdd)
button7 = tkinter.Button(root, text="7", padx = 20, pady = 5, command=buttonAdd)
button8 = tkinter.Button(root, text="8", padx = 20, pady = 5, command=buttonAdd)
button9 = tkinter.Button(root, text="9", padx = 20, pady = 5, command=buttonAdd)
button0 = tkinter.Button(root, text="0", padx = 51, pady = 5, command=buttonAdd)

entryField.grid(row=0, column=0, columnspan=3, ipady = 10)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0, columnspan = 2)

root.mainloop()