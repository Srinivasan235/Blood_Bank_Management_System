from tkinter import *
import sqlite3
from Fullscrn import *
from Admin import *
from tkinter import messagebox
import re



def delet(d):
    obj4 = Tk()
    obj4.title("Delete page")
    obj4.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")
    Frame1 = Frame(obj4)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete User Records", fg='black', font=("Courier", 25), width=200,command=lambda :byemail(obj4))
    delete2 = Button(Frame1, background="#d9d9d9", text="Delete Donor Records", fg='black', font=("Courier", 25), width=300,command=lambda :gyemail(obj4))
    delete3 = Button(Frame1, background="#d9d9d9", text="Delete Receiver Records", fg='black', font=("Courier", 25), width=200,command=lambda :kyemail(obj4))
    delete4 = Button(Frame1, background="#d9d9d9", text="Delete Blood Inventory", fg='black', font=("Courier", 25), width=200,command=lambda :byblood(obj4))

    delete1.place(relx=0.35, rely=0.25, height=53, width=400)
    delete2.place(relx=0.35, rely=0.35, height=53, width=400)
    delete3.place(relx=0.35, rely=0.45, height=53, width=400)
    delete4.place(relx=0.35, rely=0.55, height=53, width=400)

    full11 = FullScreenApp(obj4)
    obj4.mainloop()

def byemail(a):
    a.destroy()
    d = Tk()
    d.title("Delete page")

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(d)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200,command=lambda :UserDel(email2.get(),d))
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11=FullScreenApp(d)
    d.mainloop()


def UserDel(email,d):
    conn = sqlite3.connect("Blood_Bank.db")
    c = conn.cursor()
    c.execute("Select * FROM User WHERE Email=(?)",(email,))
    rec=c.fetchone()
    if rec is None:
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "No such record exists")
        window.destroy()


    else:
        c.execute("DELETE FROM User WHERE Email=(?)", (email,))
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Deleted")
        window.destroy()


        d.destroy()
        conn.commit()


def gyemail(a):
    a.destroy()
    d = Tk()
    d.title("Delete page")

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(d)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200,command=lambda :gserDel(email2.get(),d))
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11=FullScreenApp(d)
    d.mainloop()


def gserDel(email,d):
    conn = sqlite3.connect("Blood_Bank.db")
    c = conn.cursor()
    c.execute("Select * FROM Receiver WHERE Email=(?)",(email,))
    rec=c.fetchone()
    if rec is None:
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "No such record exists")
        window.destroy()

    else:
        c.execute("DELETE FROM Receiver WHERE Email=(?)", (email,))
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Deleted")
        window.destroy()
        d.destroy()
        conn.commit()


def kyemail(a):
    a.destroy()
    d = Tk()
    d.title("Delete page")

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(d)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200,command=lambda :kserDel(email2.get(),d))
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11=FullScreenApp(d)
    d.mainloop()


def kserDel(email,d):
    conn = sqlite3.connect("Blood_Bank.db")
    c = conn.cursor()
    c.execute("Select * FROM Donor WHERE Email=(?)",(email,))
    rec=c.fetchone()
    if rec is None:
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "No such record exists")
        window.destroy()
    else:
        c.execute("DELETE FROM Donor WHERE Email=(?)", (email,))
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Deleted")
        window.destroy()
        d.destroy()
        conn.commit()



def byblood(a):
    a.destroy
    e = Tk()
    e.title("Delete page")

    Frame1 = Frame(e)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    b = StringVar(Frame1)
    pblood = Label(e, text="Select Your Blood Group ")
    pblood.configure(background="#d9d9d9", font=("Times", 10))
    pblood.place(relx=0.30, rely=0.37, height=33, width=200)
    values = ["A Positive",
              'A Negative',
              'B Positive',
              'B Negative',
              'AB Positive',
              'AB Negative',
              'O Positive',
              'O Negative']
    b.set('Select Your Blood Type')
    dropdown = OptionMenu(e, b, *values)
    dropdown.place(relx=0.47, rely=0.37, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200,command=lambda :Bloodel(b.get(),e))
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11 = FullScreenApp(e)
    e.mainloop()


def Bloodel(blood,e):
    conn = sqlite3.connect("Blood_Bank.db")
    c = conn.cursor()
    c.execute("Select * FROM Blood_Inventory WHERE Blood_Group=(?)",(blood,))
    rec=c.fetchone()
    if rec is None:
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "No such record exists")
        window.destroy()
    else:
        c.execute("DELETE FROM Blood_Inventory WHERE Blood_Group=(?)", (blood,))
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Deleted")
        window.destroy()
        e.destroy()
        conn.commit()