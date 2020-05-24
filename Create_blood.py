from tkinter import *
from sqlite3 import *
from Fullscrn import *

def create_blood(a):
    moot = Tk()
    name2 = StringVar()
    page2 = IntVar()
    l_id = StringVar()
    Password_box = StringVar()
    a.destroy()
    moot.title("Create User")
    moot.geometry("500x500+120+120")
    moot.configure(background="grey")
    moot.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")

    Frame1 = Frame(moot)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.10, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Create New User", font=("Times", 25), width=1000)

    blood_type1 = Label(Frame1)
    blood_type1.place(relx=0.30, rely=0.25, height=33, width=200)
    blood_type1.configure(background="#d9d9d9", text="Enter Blood Group :", font=("Times", 10), width=1000)
    blood_type2 = Entry(moot)
    blood_type2.place(relx=0.47, rely=0.26, height=33, width=200)

    no_bags1 = Label(Frame1)
    no_bags1.place(relx=0.30, rely=0.35, height=33, width=200)
    no_bags1.configure(background="#d9d9d9", text="Enter No of Bags :", font=("Times", 10), width=1000)
    no_bags2 = Entry(moot)
    no_bags2.place(relx=0.47, rely=0.35, height=33, width=200)

    cost_bag1 = Label(Frame1)
    cost_bag1.place(relx=0.30, rely=0.45, height=33, width=200)
    cost_bag1.configure(background="#d9d9d9", text="Cost per Bag :", font=("Times", 10), width=1000)
    cost_bag2 = Entry(moot)
    cost_bag2.place(relx=0.47, rely=0.45, height=33, width=200)

    submit = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Courier", 25), width=200)
    submit.place(relx=0.37, rely=0.55, height=53, width=300)

    full13=FullScreenApp(moot)
    moot.mainloop()