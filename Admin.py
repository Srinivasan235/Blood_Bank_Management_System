import sqlite3
from tkinter import *
from Fullscrn import *
from Regsiter import *
from Create_User import *
from Show_Tables import *
from Delete_Record import *
from Update_User import *
from Update_Receiver import *
from Update_Donor import *
from Update_Blood import *
from PIL import Image

def admin(b):
    obj = Tk()
    obj.title("Admin Page")
    b.destroy()
    Frame1 = Frame(obj)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)
    obj.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")

    create = Button(Frame1, background="#d9d9d9", text="Create", fg='black', font=("Courier", 25), width=200, command=lambda:Create_User(obj))
    show = Button(Frame1, background="#d9d9d9", text="Show Records", fg='black', font=("Courier", 25), width=300, command=lambda:sho(obj))
    update = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Courier", 25), width=200, command=lambda:updte(obj))
    delete = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Courier", 25), width=200, command=lambda:delet(obj))

    create.place(relx=0.40, rely=0.05, height=53, width=300)
    show.place(relx=0.40, rely=0.15, height=53, width=300)
    update.place(relx=0.40, rely=0.25, height=53, width=300)
    delete.place(relx=0.40, rely=0.35, height=53, width=300)

    full8 = FullScreenApp(obj)
    obj.mainloop()



def updte(c):
    obj3 = Tk()
    obj3.title("Update page")
    Frame1 = Frame(obj3)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    update1 = Button(Frame1, background="#d9d9d9", text="Update User", fg='black', font=("Courier", 25), width=200, command=lambda : user11(obj3))
    update2 = Button(Frame1, background="#d9d9d9", text="Update Donor", fg='black', font=("Courier", 25), width=300, command=lambda : donor11(obj3))
    update3 = Button(Frame1, background="#d9d9d9", text="Update Receiver", fg='black', font=("Courier", 25), width=200, command=lambda : receiver11(obj3))
    update4 = Button(Frame1, background="#d9d9d9", text="Update Blood Inventory", fg='black', font=("Courier", 25), width=200, command=lambda : blood11(obj3))

    update1.place(relx=0.35, rely=0.25, height=53, width=400)
    update2.place(relx=0.35, rely=0.35, height=53, width=400)
    update3.place(relx=0.35, rely=0.45, height=53, width=400)
    update4.place(relx=0.35, rely=0.55, height=53, width=400)

    full11 = FullScreenApp(obj3)
    obj3.mainloop()