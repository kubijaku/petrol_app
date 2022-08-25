from tkinter import *

root = Tk()
root.geometry('880x400')

title = Label(root, text='Petrol App')
title.pack()

bg = PhotoImage( file="/Users/jakubkubicki/PycharmProjects/petrol_app/images/petrol_background.png")
Label(root, text='app')

photo_label = Label( root, image=bg )
photo_label.place( x=0, y=0, relwidth=1, relheight=1)

root.mainloop()