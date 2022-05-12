
from tkinter import *
from PIL import Image
import tkinter as tk

def move_left(event):
    canvas.move(myimage, -15, 0)
def move_right(event):
    canvas.move(myimage, 15, 0)

window = tk.Tk()
window.geometry("600x600")
window.configure(bg='black')

window.bind("<Right>",move_right)
window.bind("<Left>",move_left)

canvas = tk.Canvas(window,width=500,height=500,bg='#b000ff')
canvas.place(relwidth=0.8, relheight=0.9, relx=0.09, rely=0.05)


image = Image.open("rockit.PNG")
new_image = image.resize((50,50))
new_image.save('image1.png')
photo = PhotoImage(file='image1.png')
myimage = canvas.create_image(225,480,image=photo, anchor=NW)

#if photo
#label = tk.Label(canvas,text="oh word", bg="Blue",font=("ariel 7",25), width=20,height=10).pack()

window.mainloop()