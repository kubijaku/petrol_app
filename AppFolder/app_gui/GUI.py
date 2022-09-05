import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import ttk
# import sys
# sys.path.append('/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder')
from data_from_website import data


def BlurringPhoto(photo):
    convertd_photo = photo.convert('RGB')
    blured_photo = convertd_photo.filter(ImageFilter.GaussianBlur(2))
    new_photo = ImageTk.PhotoImage(blured_photo)
    return new_photo

def RegionTableShow():
    RegionTree = ttk.Treeview(root)
    RegionTree['columns'] = ("Name", "95","Status95", "98","Status98", "ON","StatusON", "ON+","StatusON+", "LPG","StatusLPG" )
    RegionTree.column("#0", width=0, stretch=NO)
    RegionTree.column("Name", width=25, minwidth=20)
    for Column in RegionTree['columns'][2:]:
        RegionTree.column(Column, width=25, minwidth=20 )
    return RegionTree


root = Tk()
root.geometry('880x400')

#Opening and Blurring photo
bg = Image.open(r"/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/myimage.gif")
blurred_bg = BlurringPhoto(bg)

#Creating Base Canvas
base_canvas = Canvas(root, width=880, height=400, bd=0, highlightthickness=0)
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
    bg1 = Image.open(r"/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/myimage.gif")
    resized_bg = bg1.resize((e.width, e.height) , Image.Resampling.LANCZOS) #Resize the image
    blurred_bg = BlurringPhoto(resized_bg)
    base_canvas.create_image(0, 0, anchor="nw", image=blurred_bg)

    #Moving text and changning its size
    base_canvas.delete("TITLE")
    title_size = min(e.width, e.height)/10
    base_canvas.create_text(int(e.width/2), int(e.height/10), text="Petrol App", tags="TITLE", font=('Apple Chancery', int(title_size), 'italic'), fill='#FF0000')

    #adding Region table

    RegionTable = RegionTableShow()
    # new_img = Image.fromarray(data.ToList(data.Data.Region_data), 'RGB')
    # img = ImageTk.PhotoImage(new_img)
    # base_canvas.create_image(25, 25, anchor="nw", image=img)
    label = Label(base_canvas, text="Kuba")
    label.pack()
    base_canvas.create_window(25,25,anchor="nw", window=label)






root.bind('<Configure>', Screen_Resizer)
root.mainloop()