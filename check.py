'''from tkinter import *

def on_click(label):
   label.destroy()

label = Label(text=" Deleting a Label in Python Tkinter", font=('Helvetica 15'))
label.pack(pady=20)

widget = Button(None, text='Hello event world',command=on_click)
widget.pack()

label.bind('<Double-1>', on_click)              # bind double left clicks
widget.mainloop()
'''
# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

def on_click():
   label.destroy()

# Create a Label widget
label = Label(win, text=" Deleting a Label in Python Tkinter", font=('Helvetica 15'))
label.pack(pady=20)

# Add a Button to Show/Hide Canvas Items
ttk.Button(win, text="Delete", command=on_click).pack()

win.mainloop()