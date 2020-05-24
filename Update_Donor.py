import sqlite3
from tkinter import *
from sqlite3 import *
from Fullscrn import *
from tkinter import messagebox
import re


def donor11(a):
    a.destroy()
    b = Tk()
    b.title("Update Donor")
    b.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")

    Frame1 = Frame(b)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(b)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    update1 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                     command=lambda: donor22(b, email2.get()))
    update1.place(relx=0.47, rely=0.57, height=43, width=200)
    update1.configure()

    full11 = FullScreenApp(b)
    b.mainloop()

conn = sqlite3.connect("Blood_Bank.db")
co = conn.cursor()

def donor22(a, email):
    co.execute('Select Email from Donor where Email=(?)', (email,))
    already = co.fetchone()

    if not (already):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Account Non-Existent")
        window.destroy()


    elif not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "email is invalid")
        window.destroy()
    else:
        co.execute("SELECT Blood_Group FROM Donor WHERE Email=(?)", (email,))
        details = co.fetchall()

        a.destroy()
        c = Tk()
        c.title("Update Donor Info")

        Frame1 = Frame(c)
        Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        Frame1.configure(borderwidth="2", background="#BD081C", width=500)

        det = Label(Frame1, text=details, font=("Times", 10), width=1000)
        det.place(relx=0.27, rely=0.05, height=33, width=600)

        blood = StringVar(Frame1)
        pblood = Label(c, text="Select Blood Group Required")
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
        dropdown = OptionMenu(c, blood, *values)
        dropdown.place(relx=0.42, rely=0.47, height=33, width=200)

        update11 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                          command=lambda: display2(blood.get(), email, c))
        update11.place(relx=0.47, rely=0.67, height=43, width=200)

        full11 = FullScreenApp(c)
        c.mainloop()


def update2(blood, email):
    co.execute("UPDATE Donor SET Blood_Group=(?) WHERE Email=(?)",
               (blood,email))
    conn.commit()

def display2(blood,email,a):
    update2(blood,email)
    a.destroy()
    d=Tk()

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    data1 = Label(Frame1)
    data1.place(relx=0.30, rely=0.45, height=33, width=500)
    data1.configure(background="#d9d9d9", text="Data Updated:", font=("Times", 10), width=1000)

    full11 = FullScreenApp(d)
    d.mainloop()