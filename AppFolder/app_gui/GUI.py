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

def RegionTableShow2(data_array, screen_width, screen_height):
    Text_Size = int((min(screen_width,screen_height))/33)
    for row_index, row in enumerate(data_array):
        for index, element in enumerate(row):
            if index == 0:
                base_canvas.create_text((screen_width/20)*(index+2), (screen_height/22)*(row_index+5), text=element, tags="RegionTable",font=( "Helvetica", int(Text_Size),'italic'))
            else:
                base_canvas.create_text((screen_width/20)*(index+3), (screen_height/22)*(row_index+5), text=element, tags="RegionTable",font=( "Helvetica", int(Text_Size),'italic'))

def OpenEye(screen_width, screen_height):
    screen_width=max(screen_width,100)
    screen_height=max(screen_height,100)
    # eye = ImageTk.PhotoImage(file="/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/open_eye.png")
    eye = Image.open(r"/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/open_eye.gif")
    resized_eye = eye.resize((int(screen_width / 30), int(screen_height / 25)), Image.Resampling.LANCZOS)  # Resize the image
    final_eye = ImageTk.PhotoImage(resized_eye)
    return final_eye

def CloseEye(screen_width, screen_height):
    # eye = ImageTk.PhotoImage(file="/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/open_eye.png")
    eye = Image.open(r"/Users/jakubkubicki/PycharmProjects/petrol_app/AppFolder/images/closed_eye.gif")
    resized_eye = eye.resize((int(screen_width / 30), int(screen_height / 25)), Image.Resampling.LANCZOS)  # Resize the image
    final_eye = ImageTk.PhotoImage(resized_eye)
    return final_eye


def Click_CloseEye():
    base_canvas.delete("OpenEye")
    # Showing general data
    screen_width = root.winfo_reqheight()
    screen_height = root.winfo_reqheight()
    final_eye = OpenEye(screen_width, screen_height)
    Eye_Button = Button(base_canvas, image=final_eye, borderwidth=0, width=screen_width / 50, height=screen_height / 50, command=Click_OpenEye)
    Eye_Button.pack()
    base_canvas.create_window(0, 0, anchor="nw", window=Eye_Button, tags="CloseEye")

    Region_array = data.ToList(data.Data.Region_data)
    RegionTableShow2(Region_array,screen_width,screen_height)
    Eye = "Open"

def Click_OpenEye():
    base_canvas.delete("CloseEye")
    # Showing general data
    Region_array = data.ToList(data.Data.Region_data)
    RegionTableShow2(Region_array,screen_width,screen_height)
    Eye = "Open"


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

#
# final_eye = OpenEye(screen_width,screen_height)
# Eye_Button = Button(base_canvas, image=final_eye, borderwidth=0, width=screen_width / 50, height=screen_height / 50)
# Eye_Button.pack()
# base_canvas.create_window(0, 0, anchor="nw", window=Eye_Button, tags="OpenEye")


#Showing general data
Region_array = data.ToList(data.Data.Region_data)
RegionTableShow2(Region_array,screen_width,screen_height)


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


    #Adding Region table
    Region_array = data.ToList(data.Data.Region_data)
    base_canvas.delete("RegionTable")
    RegionTableShow2(Region_array, e.width, e.height)

    # #Changing Eye
    # # base_canvas.delete("OpenEye")
    # final_eye = OpenEye(e.width, e.height)
    # Eye_Button = Button(base_canvas, image=final_eye, borderwidth=0, width=e.width / 50, height=e.height / 50)
    # # Eye_Button.pack()
    # # base_canvas.create_window(0, 0, anchor="nw", window=Eye_Button, tags="OpenEye")








root.bind('<Configure>', Screen_Resizer)
root.mainloop()