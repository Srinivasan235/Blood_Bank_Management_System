import sqlite3
from tkinter import *
from sqlite3 import *
from Fullscrn import *


def blood11(a):
    a.destroy()
    b = Tk()
    b.title("Update Blood Inventory")
    b.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")

    Frame1 = Frame(b)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    blood = StringVar(Frame1)
    pblood = Label(b, text="Select Blood Group Required")
    pblood.configure(background="#d9d9d9", font=("Times", 10))
    pblood.place(relx=0.26, rely=0.47, height=33, width=200)
    values = ["A Positive",
              'A Negative',
              'B Positive',
              'B Negative',
              'AB Positive',
              'AB Negative',
              'O Positive',
              'O Negative']
    blood.set('Select Blood Type')
    dropdown = OptionMenu(b, blood, *values)
    dropdown.place(relx=0.42, rely=0.47, height=33, width=200)

    update1 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                     command=lambda: blood22(b, blood.get()))
    update1.place(relx=0.47, rely=0.57, height=43, width=200)
    update1.configure()

    full11 = FullScreenApp(b)
    b.mainloop()


conn = sqlite3.connect("Blood_Bank.db")
co = conn.cursor()


def blood22(a, blood):

    co.execute("SELECT No_of_Bags,Cost_per_Bag FROM Blood_Inventory WHERE Blood_Group=(?)", (blood,))
    details = co.fetchall()

    a.destroy()
    c = Tk()
    c.title("Update Blood Info")

    Frame1 = Frame(c)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    det = Label(Frame1, text=details, font=("Times", 10), width=1000)
    det.place(relx=0.27, rely=0.05, height=33, width=600)

    no_bags1 = Label(Frame1)
    no_bags1.place(relx=0.30, rely=0.45, height=33, width=200)
    no_bags1.configure(background="#d9d9d9", text="Enter No of Bags", font=("Times", 10), width=1000)
    no_bags2 = Entry(c)
    no_bags2.place(relx=0.47, rely=0.45, height=33, width=200)

    cost1 = Label(Frame1)
    cost1.place(relx=0.30, rely=0.55, height=33, width=200)
    cost1.configure(background="#d9d9d9", text="Enter Cost Per Bag", font=("Times", 10), width=1000)
    cost2 = Entry(c)
    cost2.place(relx=0.47, rely=0.55, height=33, width=200)

    update1 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                     command=lambda: display1(blood, no_bags2.get(), cost2.get(), c))
    update1.place(relx=0.47, rely=0.67, height=43, width=200)

    full11 = FullScreenApp(c)
    c.mainloop()


def update1(blood, no_bags, cost):
    co.execute("UPDATE User SET No_of_Bags=(?),Cost_per_Bag=(?) WHERE Blood_Group=(?)",
               (int(no_bags), int(cost), str(blood)))
    conn.commit()


def display1(blood, no_bags, cost, a):
    update1(blood, no_bags, cost)
    a.destroy()
    d = Tk()

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    data1 = Label(Frame1)
    data1.place(relx=0.30, rely=0.45, height=33, width=500)
    data1.configure(background="#d9d9d9", text="Data Updated", font=("Times", 10), width=1000)

    full11 = FullScreenApp(d)
    d.mainloop()