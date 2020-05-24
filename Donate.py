from tkinter import *
from Fullscrn import *
from tkinter import messagebox

import datetime
now = datetime.datetime.now()
today=now.strftime("%Y-%m-%d")

import sqlite3

def donate(a,c):
    root2 = Tk()
    a.destroy()
    root2.geometry("500x500+120+120")
    root2.title("Blood Bank")
    root2.geometry("500x500+120+120")
    root2.configure(background="grey")
    root2.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\icon.ico")


    Frame1 = Frame(root2)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.01, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Enter Donor Details", font=("Times", 25), width=1400)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Date:", font=("Times", 10), width=1000)

    Label3 = Label(Frame1)
    Label3.place(relx=0.47, rely=0.55, height=33, width=200)
    Label3.configure(background="#d9d9d9", text=now.strftime("%Y-%m-%d"), font=("Times", 10), width=1000)

    b = StringVar(Frame1,value="Empty")

    pblood = Label(root2, text="Select Your Blood Group ")
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
    dropdown = OptionMenu(root2, b, *values)
    dropdown.place(relx=0.47, rely=0.37, height=33, width=200)



    Button_Submit = Button(Frame1, text="Submit", padx=30, pady=10, font=("Times", 20), command=lambda: display(c,b.get(),root2))
    Button_Submit.place(relx=0.35, rely=0.64, height=45, width=300)

    full5=FullScreenApp(root2)
    root2.mainloop()

conn=sqlite3.connect("Blood_Bank.db")
c=conn.cursor()

def add(e,b):
    c.execute("UPDATE Blood_Inventory SET No_of_Bags=No_of_Bags+1 where Blood_Group=(?)",(b,))
    c.execute("INSERT INTO Donor (Email,Blood_Group,Date) VALUES(?,?,?)",(e,b,today))
    conn.commit()

def display(e,b,d):
    if not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", e)):
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "email is invalid")
        window.destroy()

    elif b == 'Select Your Blood Type':
        window = Tk()
        window.withdraw()
        messagebox.showwarning("popup", "entry empty!")
        window.destroy()

    else:
        add(e,b)
        o = Tk()
        Frame1 = Frame(o)
        Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        Frame1.configure(borderwidth="2", width=500)

        Label1 = Label(Frame1)
        Label1.place(relx=0.10, rely=0.25, height=100, width=1000)
        Label1.configure(background="#d9d9d9", text=" Blood Donated Successfully", font=("Times", 50), width=1000)
        Label3 = Label(Frame1)
        Label3.place(relx=0.10, rely=0.45, height=100, width=500)
        Label3.configure(background="#d9d9d9", text="Blood Group: ", font=("Times", 30), width=1000)
        Label2 = Label(Frame1)
        Label2.place(relx=0.40, rely=0.45, height=100, width=500)
        Label2.configure(background="#d9d9d9", text=b, font=("Times", 50), width=1000)
        full11 = FullScreenApp(o)
        o.mainloop()