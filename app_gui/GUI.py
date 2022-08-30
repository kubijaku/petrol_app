from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry('880x400')

bg = ImageTk.PhotoImage( file="/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")

base_canvas = Canvas(root, width=880, height=400)
base_canvas.pack(fill="both", expand=True, )
base_canvas.create_image(0,0, image=bg, anchor="nw")

def resizer(e):
    global bg1, resized_bg, new_bg
    bg1 = Image.open("/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")
    resized_bg = bg1.resize((e.width, e.height) , Image.Resampling.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    base_canvas.create_image(10, 10, anchor=NW, image=new_bg)
    base_canvas.create_text(int(e.width/2), int(e.height/2), text="Petrol App")


root.bind('<Configure>', resizer)
root.mainloop()