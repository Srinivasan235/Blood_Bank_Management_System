from tkinter import *
from sqlite3 import *
import sqlite3


from Fullscrn import *


def sho(b):
    obj5 = Tk()
    obj5.title("Show page")
    obj5.iconbitmap(r"C:\Users\LENOVO\PycharmProjects\Blood_Bank_Management_System\admin.ico")
    Frame1 = Frame(obj5)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    show1 = Button(Frame1, background="#d9d9d9", text="Show User Table", fg='black', font=("Courier", 25), width=200,
                   command=lambda: User(obj5))
    show2 = Button(Frame1, background="#d9d9d9", text="Show Donor Table", fg='black', font=("Courier", 25), width=300,
                   command=lambda: Donor(obj5))
    show3 = Button(Frame1, background="#d9d9d9", text="Show Receiver Table", fg='black', font=("Courier", 25),
                   width=200, command=lambda: Receive(obj5))
    show4 = Button(Frame1, background="#d9d9d9", text="Show Blood Inventory", fg='black', font=("Courier", 25),
                   width=200, command=lambda: Blood(obj5))

    show1.place(relx=0.35, rely=0.25, height=53, width=400)
    show2.place(relx=0.35, rely=0.35, height=53, width=400)
    show3.place(relx=0.35, rely=0.45, height=53, width=400)
    show4.place(relx=0.35, rely=0.55, height=53, width=400)

    full11 = FullScreenApp(obj5)
    obj5.mainloop()


conn = sqlite3.connect("Blood_Bank.db")
c = conn.cursor()


def User(r):
    l = Tk()

    c.execute("SELECT * FROM User")
    records = c.fetchall()
    Frame1 = Frame(l)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", width=500)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" User Table :", font=("Times", 10), width=1000)


    lb1=Listbox(Frame1)

    lb1.insert(END, "\n")
    for i in range (len(records)):

        lb1.insert(END, records[i][0])
        lb1.insert(END, records[i][1])
        lb1.insert(END, records[i][2])
        lb1.insert(END, records[i][3])
        lb1.insert(END, records[i][4])
        lb1.insert(END, records[i][5])
        lb1.insert(END,"=======================================")

    lb1.place(relx=0.02,rely=0.02,relheight=0.94, relwidth=0.96)

    conn.commit()
    full11 = FullScreenApp(l)
    l.mainloop()


def Receive(r):
    m = Tk()

    c.execute("SELECT * FROM Receiver")
    records = c.fetchall()
    Frame1 = Frame(m)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", width=500)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Receiver Table :", font=("Times", 10), width=1000)
    lb1 = Listbox(Frame1)

    lb1.insert(END, "\n")
    for i in range(len(records)):
        lb1.insert(END, records[i][0])
        lb1.insert(END, records[i][1])
        lb1.insert(END, records[i][2])
        lb1.insert(END, records[i][3])
        lb1.insert(END, records[i][4])
        lb1.insert(END, records[i][5])
        lb1.insert(END, records[i][6])
        lb1.insert(END, "=======================================")
        lb1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    conn.commit()
    full11 = FullScreenApp(m)
    m.mainloop()


def Blood(r):
    n = Tk()

    c.execute("SELECT * FROM Blood_Inventory")
    records = c.fetchall()
    Frame1 = Frame(n)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", width=500)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Blood_Inventory Table :", font=("Times", 10), width=1000)

    lb1 = Listbox(Frame1)

    lb1.insert(END, "\n")
    for i in range(len(records)):
        lb1.insert(END, records[i][0])
        lb1.insert(END, records[i][1])
        lb1.insert(END, records[i][2])
        lb1.insert(END, "=======================================")
        lb1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)



    conn.commit()
    full11 = FullScreenApp(n)
    n.mainloop()


def Donor(r):
    o = Tk()

    c.execute("SELECT * FROM Donor")
    records = c.fetchall()
    Frame1 = Frame(o)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", width=500)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Donor Table :", font=("Times", 10), width=1000)

    lb1 = Listbox(Frame1)

    lb1.insert(END, "\n")
    for i in range(len(records)):
        lb1.insert(END, records[i][0])
        lb1.insert(END, records[i][1])
        lb1.insert(END, records[i][2])
        lb1.insert(END, records[i][3])

        lb1.insert(END, "=======================================")
        lb1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    conn.commit()
    full11 = FullScreenApp(o)
    o.mainloop()
