import tkinter as tk

# create the main window
root =  tk.Tk()
root.title("simple calculator")

# entry widget to show the calculation
entry = tk.Entry(root, width=35,borderwidth=5)
entry.grid(row=0, columnspan=4, padx=10, pady=10)

#Button click event
def button_click(number):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current + str(number))

def button_clear():
    entry. delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "error")
#button definutions
button = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('+',4,2),('=',4,3),
]

#create the button in a loop
for(text,row,col) in button:
    if text == '=':
        tk.Button(root, text=text, padx=30, pady=20, command=button_equal).grid(row=row,column=col)

    else:
        tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t)).grid(row=row,column=col)

#clear button
tk.Button(root, text="Clear", padx=100, pady=20, command=button_clear).grid(row=5, column=0, columnspan=4)

#start the GUI Eevent loop
root.mainloop()
