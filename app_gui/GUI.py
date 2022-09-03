from tkinter import *
from PIL import Image, ImageTk, ImageFilter

def BlurringPhoto(photo):
    convertd_photo = photo.convert('RGB')
    blured_photo = convertd_photo.filter(ImageFilter.GaussianBlur(2))
    new_photo = ImageTk.PhotoImage(blured_photo)
    return new_photo

root = Tk()
root.geometry('880x400')

#Opening and Blurring photo
bg = Image.open(r"/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")
blurred_bg = BlurringPhoto(bg)

#Creating Base Canvas
base_canvas = Canvas(root, width=880, height=400)
base_canvas.pack(fill="both", expand=True)

#Adding Background
base_canvas.create_image(0,0, image=blurred_bg, anchor="nw")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Adding Title
title_size = min(screen_width,screen_height)/10
base_canvas.create_text(int(screen_width/2), int(screen_height/10), text="Petrol App", tags="TITLE", font=('Apple Chancery', int(title_size),'italic'),fill='#FF0000')

def Screen_Resizer(e):
    global bg1, resized_bg, blurred_bg
    #Chnaging size of Background
    bg1 = Image.open("/Users/jakubkubicki/PycharmProjects/petrol_app/images/myimage.gif")
    resized_bg = bg1.resize((e.width, e.height) , Image.Resampling.LANCZOS) #Resize the image
    blurred_bg = BlurringPhoto(resized_bg)
    base_canvas.create_image(0, 0, anchor="nw", image=blurred_bg)

    #Moving text and changning its size
    base_canvas.delete("TITLE")
    title_size = min(e.width, e.height)/10
    base_canvas.create_text(int(e.width/2), int(e.height/10), text="Petrol App", tags="TITLE", font=('Apple Chancery', int(title_size), 'italic'), fill='#FF0000')



root.bind('<Configure>', Screen_Resizer)
root.mainloop()