from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Home Page")
root.configure(background='white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 5*screen_width/6
height = 5*screen_height/6
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

def openListPage():
    os.system('python listPage.py')

#เปิดหน้าreal-time face regconition
def openFaceReg():
    print("Open face regconition page!")

line1 = Frame(root, width=width, bg='white')
line1.pack()
myLabel = Label(line1, padx=width/5, text="Smart Clock for\nFace Recognition in classroom", bg='#E2E2E2', fg='#5A5A5A', font =(None, int(height//10)))
myLabel.pack(side=TOP)
space1 = Label(root, text=' ',bg='white')
space1.pack()


load = Image.open("faceImage.gif")
load = load.resize((int(width*0.20), int(width*0.20)), Image.ANTIALIAS)
face_img = ImageTk.PhotoImage(load)
load = Image.open("faceButton.gif")
load = load.resize((int(width*0.42), int(width*0.06)), Image.ANTIALIAS)
face_btn = ImageTk.PhotoImage(load)
load = Image.open("listImage.gif")
load = load.resize((int(width*0.20), int(width*0.20)), Image.ANTIALIAS)
list_img = ImageTk.PhotoImage(load)
load = Image.open("listButton.gif")
load = load.resize((int(width*0.24), int(width*0.06)), Image.ANTIALIAS)
list_btn = ImageTk.PhotoImage(load)
left = Frame(root, width=int(width/2), bg='white')
left.pack(padx=(60,30), side=LEFT)
right = Frame(root, width=int(width/2), bg='white')
right.pack(padx=(20,150), side=RIGHT)
faceLabel = Label(left, image=face_img, borderwidth=0)
faceButton = Button(left, image=face_btn, command=openFaceReg, borderwidth=0)
listLabel = Label(right, image=list_img, borderwidth=0)
listButton = Button(right, image=list_btn, command=openListPage, borderwidth=0)
faceLabel.pack()
faceButton.pack()
listLabel.pack()
listButton.pack()
root.mainloop()
