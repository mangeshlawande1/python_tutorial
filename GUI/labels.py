from tkinter import *

# label = an area widget thata holds text and /or an image eithin a window 

window = Tk()

photo =PhotoImage(file='logo.png', )
label = Label(window, 
              text="Hello World !!", 
              font=("Arial",40,"bold"),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image = photo,
              compound = 'bottom'
              )

# label.place(x=100,y=100)
label.pack()

window.mainloop()
