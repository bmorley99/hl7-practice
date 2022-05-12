import tkinter as tk
from tkinter import filedialog, Text
import os
import parser
from tkinter import *

root = tk.Tk()
root.title("Pathing App")
apps = []
root.geometry("400x600")

if os.path.isfile('Save.txt'):
    with open("Save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def Label():
    for app in apps:
        global label
        label = tk.Label(frame, text=app, bg="#FFB6C1",font="ariel 7", wraplength=300)
        label.pack()

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("executables","*.exe"),("Text files", "*.txt"),('JPG files', '*.jpg'),("all files","*.*")))
    apps.append(filename)
    print(filename)
    Label()

def runApp():
    for app in apps:
        os.startfile(app)

def close():
    root.destroy()
    root.quit()

def delete():
    fileVariable = open('Save.txt', 'r+')
    fileVariable.truncate(0)
    fileVariable.close()
    print(delete)

def Labdelete():
    global label
    label.destroy()

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked

canvas = tk.Canvas(root, height=1000, bg="#263D42").place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="lightblue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
#rlex and rely are the x and y cordiandates indication of the paddling to help center the white box we have just created
buttonClicked  = False


openfile = tk.Button(root, text="Open", padx=10, pady=5, fg="Black", bg="#FFB6C1", command=addApp).place(relwidth=0.17, relheight=0.07, relx=0.13, rely=.81)

runApps = tk.Button(root, text="Run", padx=10, pady=2, fg="Black", bg="#FFB6C1", command=runApp).place(relwidth=0.17, relheight=0.07, relx=0.32, rely=.81)

Delete = tk.Button(root, text="Delete", fg="Black", bg="#FFB6C1",command=lambda: [Labdelete(), delete(),callback()]).place(relwidth=0.17, relheight=0.07, relx=.51, rely=.81)

Clear = tk.Button(root, text="Close", fg="Black", bg="#FFB6C1",command=close).place(relwidth=0.17, relheight=0.07, relx=.70, rely=.81)

Label()

root.mainloop()
if buttonClicked == False:
    with open("Save.txt","w") as f:
        for app in apps:
            f.write(app + ',')


