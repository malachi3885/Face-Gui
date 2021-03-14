from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Student List")
root.configure(background='white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 5*screen_width/6
height = 5*screen_height/6
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

def search():
    print(1)
    tree.delete(*tree.get_children())
    if(inputBox.get() == ''):
        for i in range(1, studentCount+1):
            ID = IDArray[i-1]
            name = nameArray[i-1]
            tree.insert("", END, values=(str(i)+".", ID, name))
    else:
        j=1
        for i in range(1, studentCount+1):
            if(inputBox.get().lower() in IDArray[i-1].lower() 
            or inputBox.get().lower() in nameArray[i-1].lower()):
                ID = IDArray[i-1]
                name = nameArray[i-1]
                tree.insert("", END, values=(str(j)+".", ID, name))
                j+=1
#line1
line1 = Frame(root, width=width)
line1.pack()
# exitButton = Button(line1, text='exit')
# exitButton.pack(side=LEFT)
myLabel = Label(line1, padx=width/5, text="Student List", bg='#E2E2E2', fg='#5A5A5A', font =(None, int(height/10)))
myLabel.pack(side=TOP)
space1 = Label(root, text=' ', bg='white')
space1.pack()
#line2
searchBar = Frame(root, width=width, bg='white')
searchBar.pack()
inputBox = Entry(searchBar, width=int(width/50), font=(None,int(4*height/100)), bg='#F1F1F1',bd=0)
inputBox.config(highlightthickness=0)
inputBox.pack(side=LEFT)
space2 = Label(searchBar, text='  ', bg='white')
space2.pack(side=LEFT)
searchButton = Button(searchBar, text='Search', command=search, bg='white',bd=1,pady=1)
searchButton.config(highlightthickness=0,highlightbackground='white')
searchButton.pack(side=LEFT)
text = StringVar()
countLabel = Label(searchBar, textvariable=text, font=(None,int(3*height/100)), bg='white')
countLabel.pack(side=LEFT)
space3 = Label(searchBar, text=' '* int(width/20), bg='white')
space3.pack()
space4 = Label(root, text=' ', bg='white')
space4.pack()

s = ttk.Style()
s.configure('Treeview.Heading', rowheight=100, font=(None,int(4*height/105)))
s.configure('Treeview', rowheight=int(7*height/100), font=(None,int(4*height/100)))


TableMargin = Frame(root, width=int(width))
TableMargin.pack(side=BOTTOM)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Order", "ID", "Name"), height=400, selectmode="extended",  yscrollcommand=scrollbary.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
tree.heading('Order', text="", anchor=W)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=int(2*width/30))
tree.column('#2', stretch=NO, minwidth=0, width=int(10*width/30))
tree.column('#3', stretch=NO, minwidth=0, width=int(12*width/30))
tree.pack()
studentCount = 0
IDArray = [0] * 100
nameArray = [0] * 100
with open('name.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        IDArray[studentCount] = row['ID']
        nameArray[studentCount] = row['Name']
        studentCount += 1
text.set("   Total Students: " + str(studentCount))
for i in range(1, studentCount+1):
    ID = IDArray[i-1]
    name = nameArray[i-1]
    tree.insert("", END, values=(str(i)+".", ID, name))

root.mainloop()
