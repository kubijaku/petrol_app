from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry('880x400')

bg = ImageTk.PhotoImage( file="/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")

base_canvas = Canvas(root, width=880, height=400)
base_canvas.pack(fill="both", expand=True, )
base_canvas.create_image(0,0, image=bg, anchor="nw")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
text_size = min(screen_width,screen_height)/10
base_canvas.create_text(440, 50, text="Petrol App", tags="TITLE", font=('Apple Chancery', int(text_size),'italic'))

def resizer(e):
    global bg1, resized_bg, new_bg
    bg1 = Image.open("/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")
    resized_bg = bg1.resize((e.width, e.height) , Image.Resampling.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    base_canvas.create_image(10, 10, anchor=NW, image=new_bg)
    base_canvas.delete("TITLE")
    text_size = min(e.width, e.height)/10
    base_canvas.create_text(int(e.width/2), int(e.height/8), text="Petrol App", tags="TITLE", font=('Apple Chancery', int(text_size), 'italic'))


root.bind('<Configure>', resizer)
root.mainloop()