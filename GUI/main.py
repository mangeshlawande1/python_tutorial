from tkinter import *


# widgets : GUI elements:Buttons, textboxes, labels, images

# windows : serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance od window 
window.geometry("420x420")
window.title("Bro code first GUI Program ")

# icon =  PhotoImage(file="logo.png")
# window.iconphoto(True,icon)
window.config(background="Black");
window.mainloop() # place window on computer screen listen for events 
