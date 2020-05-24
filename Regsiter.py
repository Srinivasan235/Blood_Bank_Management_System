# ( from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
import re
from Login import *
import sqlite3
from Fullscrn import *

from Login import *


def register(a):
    loot = Tk()
    name2 = StringVar()
    page2 = IntVar()
    l_id = StringVar()
    Password_box = StringVar()
    a.destroy()
    loot.title("Blood Bank")
    loot.geometry("500x500+120+120")
    loot.configure(background="grey")
    loot.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")

    Frame1 = Frame(loot)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.01, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Registration Form", font=("Times", 25), width=1000)

    name1 = Label(Frame1)
    name1.place(relx=0.30, rely=0.15, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter Name:", font=("Times", 10), width=1000)
    name2 = Entry(loot)
    name2.place(relx=0.47, rely=0.16, height=33, width=200)

    psex = Label(Frame1)
    psex.place(relx=0.30, rely=0.25, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Select Sex of Patient ", font=("Times", 10))
    v = StringVar(Frame1, value="Male")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male", font=("Times", 10))
    radiobutton1.place(relx=0.50, rely=0.25)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female", font=("Times", 10))
    radiobutton2.place(relx=0.60, rely=0.25)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other", font=("Times", 10))
    radiobutton3.place(relx=0.70, rely=0.25)

    page1 = Label(Frame1)
    page1.place(relx=0.30, rely=0.35, height=33, width=200)
    page1.configure(background="#d9d9d9", text="Enter Age:", font=("Times", 10))
    page2 = Entry(loot)
    page2.place(relx=0.47, rely=0.35, height=33, width=200)

    phonenumber1 = Label(Frame1)
    phonenumber1.place(relx=0.30, rely=0.45, height=33, width=200)
    phonenumber1.configure(background="#d9d9d9", text="Enter Phone Number:", font=("Times", 10), width=1000)
    phonenumber2 = Entry(loot)
    phonenumber2.place(relx=0.47, rely=0.46, height=33, width=200)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Set Login_ID/Email_ID :", font=("Times", 10), width=1000)
    l_id = Entry(loot)
    l_id.place(relx=0.47, rely=0.54, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.30, rely=0.65, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Set Password: ", font=("Times", 10), width=1000)
    Password_box = Entry(loot, show="*")
    Password_box.place(relx=0.47, rely=0.63, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.30, rely=0.75, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Confirm Password ", font=("Times", 10), width=1000)
    Password_box1 = Entry(loot, show="*")
    Password_box1.place(relx=0.47, rely=0.73, height=33, width=200)

    Button1 = Button(Frame1, background="#d9d9d9", text="Login", fg='black', font=("Times", 25), width=200,
                     command=lambda: page(loot))
    Button1.place(relx=0.65, rely=0.87, height=43, width=200)
    Button1.configure()

    Button_Submit = Button(Frame1, text="Register", padx=30, pady=10, font=("Times", 20),
                           command=lambda: loginbob(name2.get(), v.get(), page2.get(), phonenumber2.get(), l_id.get(),
                                                    Password_box.get(), Password_box1.get(), loot))
    Button_Submit.place(relx=0.35, rely=0.87, height=45, width=300)

    full3 = FullScreenApp(loot)
    loot.mainloop()


conn = sqlite3.connect("Blood_Bank.db")
c = conn.cursor()


def insert(l, v, n, pno, a, b):
    c.execute(
        "CREATE TABLE IF NOT EXISTS User(Name TEXT NOT NULL,Sex TEXT,Age INTEGER NOT NULL,PhoneNumber INTEGER,Email TEXT PRIMARY KEY,Password TEXT NOT NULL)")
    c.execute("INSERT INTO User VALUES(?,?,?,?,?,?)", (l, n, a, b, pno, v))
    conn.commit()


def loginbob(l, v, n, pno, a, b, c, d):
    co.execute('Select Email from User where Email=(?)', (a,))
    already = co.fetchone()

    if not (re.search("[A-Za-z_ ]", l)):
        window = Tk()
        window.withdraw()
        messagebox.showerror("popup", "Name should only contain character")
        window.destroy()



    elif not (re.search("\d", n)):
        window = Tk()
        window.withdraw()
        messagebox.showerror("popup", "Age should contain only integer values")
        window.destroy()

    elif not (re.search(r'[789]\d{9}$', pno)):
        window = Tk()
        window.withdraw()
        messagebox.showerror("popup", "PhoneNumber should be of 10 digits and it should start with only 7,8 and 9")
        window.destroy()


    elif not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", a)):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "email is invalid")
        window.destroy()



    elif not (already==None):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "Email already Present")
        window.destroy()


    elif not (re.search("[\w@$&_!]{8,14}", b)):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "password is weak or too short")
        window.destroy()


    elif not (c == b):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "your passwords do not match")
        window.destroy()

    else:
        if(int(n)<18):
            window = Tk()
            window.withdraw()
            messagebox.showwarning("popup", "Age must be above 18!")
            window.destroy()
        else:
            insert(l, v, n, pno, a, b)
            root1 = Tk()
            d.destroy()
            root1.title("Blood Bank")
            # root1.geometry("500x500+120+120")
            root1.configure(background="grey")
            Frame1 = Frame(root1)
            Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
            Frame1.configure(borderwidth="2", background="#BD081C", width=500)
            label2 = Label(Frame1)
            label2.place(relx=0.10, rely=0.15, height=93, width=1000)
            label2.configure(background="#d9d9d9", text="Do You Want To Donate Or Request?", font=("Times", 25),
                             width=1200)
            Frame2 = Frame(Frame1)
            Frame2.place(relx=0.35, rely=0.3, relheight=0.50, relwidth=0.30)
            Button3 = Button(Frame2)
            Button3.place(relx=0.25, rely=0.30, height=53, width=200)
            Button3.configure(background="#d9d9d9", text="Donate", font=("Courier", 25), width=200,
                              command=lambda: donate(root1, a))
            Button4 = Button(Frame2, background="#d9d9d9", text="Request", fg='black', font=("Courier", 25),
                             width=200,
                             command=lambda: receive(root1, a))
            Button4.place(relx=0.25, rely=0.50, height=53, width=200)
            Button4.configure()
            full7 = FullScreenApp(root1)
            root1.mainloop()

